
"""A simple build system that just copies files to the build path."""

import os
import shutil
import stat

from rez.build_system import BuildSystem
from rez.build_process import BuildType

class DefaultBuildSystem(BuildSystem):
    """The default build system for python packages.

    Simply copies the package files to the build directory, sets binaries to
    executable mode, and optionally copies the build to the install directory.
    Don't use this if you need to compile c/c++ code or do anything custom.
    """

    def __init__(self, working_dir, opts=None, package=None, write_build_scripts=False,
                 verbose=False, build_args=[], child_build_args=[]):
        super(DefaultBuildSystem, self).__init__(working_dir,
            opts=opts,
            package=package,
            write_build_scripts=write_build_scripts,
            verbose=verbose,
            build_args=build_args,
            child_build_args=child_build_args)

    @classmethod
    def name(cls):
        """Return the name of the build system, eg 'make'."""
        return "default"

    @classmethod
    def is_valid_root(cls, path, package=None):
        """Return True if this build system can build the source in path."""
        # TODO: this should probably check something
        return True

    def build(self, context, variant, build_path, install_path, install=False,
              build_type=BuildType.local):
        """Implement this method to perform the actual build.

        Args:
            context: A ResolvedContext object that the build process must be
                executed within.
            variant (`Variant`): The variant being built.
            build_path: Where to write temporary build files. May be absolute
                or relative to working_dir.
            install_path (str): The package repository path to install the
                package to, if installing. If None, defaults to
                `config.local_packages_path`.
            install: If True, install the build.
            build_type: A BuildType (i.e local or central).

        Returns:
            A dict containing the following information:
            - success: Bool indicating if the build was successful.
            - extra_files: List of created files of interest, not including
                build targets. A good example is the interpreted context file,
                usually named 'build.rxt.sh' or similar. These files should be
                located under build_path. Rez may install them for debugging
                purposes.
            - build_env_script: If this instance was created with write_build_scripts
                as True, then the build should generate a script which, when run
                by the user, places them in the build environment.
        """
        ret = {'success': False}
        package_dir = self.package.name

        # python source
        src_py = os.path.join(self.working_dir, package_dir)
        dest_py = os.path.join(build_path, package_dir)

        # make sure to delete the old build first
        if os.path.exists(dest_py):
            shutil.rmtree(dest_py)
        shutil.copytree(src_py, dest_py)

        # binaries
        mode = (stat.S_IRUSR | stat.S_IRGRP |
                stat.S_IXUSR | stat.S_IXGRP)

        src_bin = os.path.join(self.working_dir, "bin")
        dest_bin = os.path.join(build_path, "bin")

        if os.path.exists(src_bin):
            if os.path.exists(dest_bin):
                shutil.rmtree(dest_bin)
            shutil.copytree(src_bin, dest_bin)

            for name in os.listdir(dest_bin):
                filepath = os.path.join(dest_bin, name)
                os.chmod(filepath, mode)

        if install:
            for name in ("bin", package_dir):
                src = os.path.join(build_path, name)
                dest = os.path.join(install_path, name)

                if not os.path.exists(src):
                    continue

                if os.path.exists(dest):
                    shutil.rmtree(dest)

                print(src)
                print(dest)
                shutil.copytree(src, dest)
                
        ret['success'] = True
        return ret


def register_plugin():
    return DefaultBuildSystem
