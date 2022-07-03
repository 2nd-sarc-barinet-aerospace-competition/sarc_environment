cmake_minimum_required(VERSION 2.8.3)
project(sarc_environment)

find_package(catkin REQUIRED COMPONENTS)

catkin_package()

install(
  DIRECTORY launch media models world_models worlds
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_install_python(PROGRAMS scripts/sarc_map.py scripts/sarc_low_map.py scripts/fall.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
