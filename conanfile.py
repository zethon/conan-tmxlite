from conans import ConanFile, CMake, tools


class TmxliteConan(ConanFile):
    name = "tmxlite"
    version = "1.2.1"
    license = "Zlib license"
    author = "Adalid Claure <aclaure@gmail.com>"
    url = "https://github.com/zethon/conan-tmxlite"
    description = "A lightweight C++14 parsing library for tmx map files"
    topics = ("games", "rpg", "maps")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/fallahn/tmxlite.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="tmxlite")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]

