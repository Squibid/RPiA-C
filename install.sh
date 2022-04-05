#!/bin/bash
# check pkg manager based on current distro
declare -A osInfo;
osInfo[/etc/arch-release]=pacman
osInfo[/etc/debian_version]=apt-get

for f in ${!osInfo[@]}; do
    if [[ -f $f ]];then
        pkgMngr=${osInfo[$f]}
    fi
done

#update system im too lazy to add other pkg managers
if [ $pkgMngr == 'pacman' ]; then
  sudo pacman -Syu
  sudo pacman -S git
if [ $pkgMngr == 'apt-get' ]; then
  sudo apt-get update && sudo apt-get upgrade
  sudo apt-get install git
else:
  echo "Your not running a distro with one of the package managers in the program please add it by editing the install script or create an issue on the git repo"
  exit
fi

#compile needed packages
git clone https://github.com/xorg62/tty-clock.git && cd tty-clock && sudo make clean install
git clone https://github.com/dunst-project/dunst.git && cd dunst && make && sudo make install
