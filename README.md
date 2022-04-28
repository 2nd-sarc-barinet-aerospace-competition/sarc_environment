# sarc_environment

## Description

An environment for simulating a burning forest, with the intention that teams can demonstrate their work in stage one of the SARC competition.

## Getting Started

### Dependencies

* Ubuntu 20.04
* Gazebo 11.10
* ROS Noetic
* MRS System (optional)
* NOTE: MRS documentation https://ctu-mrs.github.io/

### Installing

* Since this package gives you just the environment, you can use it however you like, as long as you already have Ubuntu, ROS Noetic and Gazebo 11.10. 
  We strongly recommend that you use MRS System, which installs everything you need.
* Installing MRS:
* At the link https://github.com/ctu-mrs/mrs_uav_system , go to the Installation section and choose one of the installation options,
  any of them will work, we recommend that you use the local option, that you just run the script and everything is automatically downloaded.
* NOTE: Please only install MRS on a newly installed Ubuntu, it will be an easy way
* With all that done, simply clone this package into a Catkin workspace (if you don't know what that is, http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
  and build. (If you have MRS, we recommend that you clone into the "workspace" folder that is in "home")

### Executing program

* If you don't have MRS, you can simply run the environment by going to the launch folder and running sarc.launch, using in the terminal
```
roslaunch sarc.launch
```
* Otherwise, if you do have MRS, go to the folder start and running start.sh, using in the terminal
```
./start.sh
```

### Will be added soon, STAY TUNED
* KC (aircraft) making a path on the map;
* MRS*, drones falling from KC (a free-fall mode will be added!)
* A type of tree with less computational consumption;
* A video explaining the package better.
