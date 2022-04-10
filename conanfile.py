from conans import ConanFile, CMake, tools
import os, glob

class Efsw(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    name = 'efsw'
    url = 'https://github.com/firefalcom/conan-efsw'
    license = 'MIT'
    version = '2e73f8e96779a2895c6242d66cadb3a15aa5e192'
    options = {
        'shared': [True, False],
        'fPIC': [True, False],
    }
    default_options = (
        'shared=False',
        'fPIC=False'
    )
    generators = 'cmake'

    source_folder = 'source_folder'

    def sourcedir(self):
        return os.path.join(os.getcwd(), self.name)

    def source(self):
        git = tools.Git(folder=self.source_folder)
        git.clone("https://github.com/SpartanJ/efsw.git")
        git.checkout(self.version)

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.definitions["STATIC_LIB"] = not self.options.shared
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        includedir = os.path.join('include', 'efsw')
        src_includedir = os.path.join('efsw', includedir)

        self.copy(os.path.join(src_includedir, '*.h'), dst=includedir, keep_path=False)
        self.copy(os.path.join(src_includedir, '*.hpp'), dst=includedir, keep_path=False)
        self.copy('*.a', dst='lib')
        self.copy('*.so', dst='lib')
        self.copy('*.lib', dst='lib')
        self.copy('*.dll', dst='lib')

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.libs = tools.collect_libs(self)

        if self.settings.os == "Macos":
            self.cpp_info.frameworks.extend( ["CoreFoundation", "CoreServices"] )
        elif self.settings.os == 'Linux':
            self.cpp_info.libs.append('pthread')
