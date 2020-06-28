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
        # cmake.configure(source_folder="tmxlite/tmxlite")
        # cmake.build()

    def package(self):
        filelist = [
            'Config.hpp', 
            "FreeFuncs.hpp", 
            "ImageLayer.hpp", 
            "Layer.hpp", 
            "LayerGroup.hpp", 
            "Map.hpp", 
            "Object.hpp", 
            "ObjectGroup.hpp", 
            "Property.hpp", 
            "TileLayer.hpp", 
            "Tileset.hpp", 
            "Types.hpp", 
            "Types.inl"
        ]

        for h in filelist:
            self.copy(h, src="tmxlite/tmxlite/include/tmxlite", dst="include/tmxlite", keep_path=False)

        for h in ["Android.hpp", "Log.hpp"]:
            self.copy(h, src="tmxlite/tmxlite/include/tmxlite/detail", dst="include/tmxlite/detail", keep_path=False)
        
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]

