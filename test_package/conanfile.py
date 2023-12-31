import os
from conan import ConanFile
from os.path import join
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.build import can_run

class TestEfsw(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = "CMakeDeps", "CMakeToolchain"


    def requirements(self):
        self.requires(self.tested_reference_str)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        cmake_layout(self)

    def test(self):
        if can_run(self):
            if self.settings.os == "Windows":
                cmd = os.path.join(self.cpp.build.bindir, "test_package.exe")
            else:
                cmd = os.path.join(self.cpp.build.bindir, "test_package")

            self.run(cmd, env="conanrun")
