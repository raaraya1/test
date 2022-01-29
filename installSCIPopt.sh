#!/bin/bash
# This is an automated installer Script for the SCIP Optimization Suite including GCG.

RED='\033[0;31m'
W='\e[0m\n'
B='\n\e[1m'

function test(){
  while true; do

      printf "Running GCG on some sample instances...";
      cd gcg/
        if [ $1 = 1 ]
        then
          make gcg_check
        elif [ $1 = 2 ]
        then
          make test
        fi
      printf "${B}Done!${W}";
      break;;

  done
}

function fcmake(){
  printf "${B}Updating CMake${W}"
  sudo apt-get install cmake
  printf "${B}Compiling the SCIP Optimization Suite${W}"
  mkdir build
  cd build
  cmake .. | tail -n +91
  make
  printf "${B}Creating Executable${W}"
  make install
  test "1"
}

function fmake(){
  printf "${B}Updating Make${W}"
  sudo apt-get install make
  printf "${B}Compiling SCIP, SoPlex and ZIMPL${W}"
  make scipoptlib
  printf "${B}Compiling GCG${W}"
  make gcg
  printf "${B}Creating Executable${W}"
  make install
  test "2"
}

function installPrerequisites(){
  while true; do

      echo "Updating Package Manager..."
      sudo apt-get update
      echo "Installing prerequisites..."
      sudo apt-get install build-essential libreadline-dev libz-dev libgmp3-dev lib32ncurses5-dev libboost-program-options-dev
      break;;

  done
}

function install(){
  installPrerequisites;
  printf "${B}Initializing Installation...${W}"
  while [[ ! -f $SCIPtar || -z $SCIPtar ]]; do
    read -e -p " Please enter path to SCIP Optimization Suite tarball: " SCIPtar
  done
  SCIPtar=$(realpath $SCIPtar)
  printf " SCIP .tar found."

  if [[ -d ${SCIPtar%.tgz} ]]; then
    printf " Removing old folder: '${SCIPtar%.tgz}'\n"
    rm -r ${SCIPtar%.tgz}
  fi

  printf "${B}Unpacking SCIP Optimization Suite${W}"
  tar xvzf $SCIPtar > /dev/null 2>&1
  rm $SCIPtar
  cd ${SCIPtar%.tgz}
  printf "Done.\n"

  while true; do
      printf "${B}Install the SCIP Optimization Suite using...${W}"
                fcmake;
                  break;;

  done
}


while true; do
    printf "${B}The SCIP Optimization Suite will be installed into the current folder.${W}"
              install;
                break;;
      
done
