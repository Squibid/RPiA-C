# check pkg manager
declare -A osInfo;
osInfo[/etc/redhat-release]=yum
osInfo[/etc/arch-release]=pacman
osInfo[/etc/gentoo-release]=emerge
osInfo[/etc/SuSE-release]=zypp
osInfo[/etc/debian_version]=apt-get
osInfo[/etc/alpine-release]=apk

for f in ${!osInfo[@]}; do
    if [[ -f $f ]];then
        pkgMngr=${osInfo[$f]}
    fi
done

#update system
if [ $pkgMngr == 'yum' ]; then
  sudo yum update
if [ $pkgMngr == 'pacman' ]; then
  sudo pacman -Syu
if [ $pkgMngr == 'emerge' ]; then
  emaint -a sync && emerge --ask --verbose --update --deep --newuse @world
if [ $pkgMngr == 'zypp' ]; then
  sudo zypper update
if [ $pkgMngr == 'apt-get' ]; then
  sudo apt-get update && sudo apt-get upgrade
if [ $pkgMngr == 'apk' ]; then
  apk update && apk add --upgrade apk-tools
fi

#pkg list
pkgList = cat pkgs
