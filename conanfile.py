from conan import ConanFile
from conan.tools.files import copy, get
from conan.tools.cmake import CMake, cmake_layout
from os.path import join
from conan.tools.scm import Git
import os

class Efsw(ConanFile):

    settings = 'os', 'compiler', 'build_type', 'arch'
    name = 'efsw'
    description = 'conan package for the Entropia Filesystem Watcher'
    url = 'https://github.com/firefalcom/conan-efsw'
    license = 'MIT'
    version = '2e73f8e96779a2895c6242d66cadb3a15aa5e192'
    options = {
        'shared': [True, False],
        'fPIC': [True, False],
    }
    default_options = {
        'shared':False,
        'fPIC':False
    }

    generators = "CMakeDeps", "CMakeToolchain"

    def layout(self):
        cmake_layout(self)


    def source(self):
        git = Git(self)
        git.clone(url="https://github.com/SpartanJ/efsw.git", target=".")
        git.checkout(commit=self.version)


    def build(self):
        cmake = CMake(self)
        options = {"STATIC_LIB":not self.options.shared, "CMAKE_POSITION_INDEPENDENT_CODE" : self.options.fPIC }
        cmake.configure(options)
        cmake.build()

    def package(self):
        includedir = os.path.join('include', 'efsw')

        copy(self, os.path.join(includedir, '*.h'), self.source_folder, join(self.package_folder, includedir), keep_path=False)
        copy(self, os.path.join(includedir, '*.hpp'), self.source_folder, join(self.package_folder, includedir), keep_path=False)
        copy(self, '*.a', self.source_folder, join(self.package_folder, "lib"), keep_path=False)
        copy(self, '*.so', self.source_folder, join(self.package_folder, "lib"), keep_path=False)
        copy(self, '*.lib', self.source_folder, join(self.package_folder, "lib"), keep_path=False)
        copy(self, '*.dll', self.source_folder, join(self.package_folder, "lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.libs = ["efsw"]

        if self.settings.os == "Macos":
            self.cpp_info.frameworks.extend( ["CoreFoundation", "CoreServices"] )
        elif self.settings.os == 'Linux':
            self.cpp_info.system_libs.append('pthread')
