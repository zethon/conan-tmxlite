#include <iostream>
#include <tmxlite/Map.hpp>

constexpr auto map_string = R"(<?xml version="1.0" encoding="utf-8"?>
<map version="1.0" orientation="orthogonal" width="1" height="1" tilewidth="8" tileheight="8">
  <layer name="untitled layer" width="1" height="1">
    <properties>
      <property name="@Description" value="" />
    </properties>
    <data encoding="xml">
      <tile gid="0" />
    </data>
  </layer>
</map>)";

int main() 
{
    tmx::Map map;
    map.loadFromString(map_string, "");
    std::cout << "map version: " << map.getVersion().upper << '\n';
    return 0;
}
