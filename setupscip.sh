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

print "The SCIP Optimization Suite will be installed into the current folder."
installPrerequisites;
cd scipoptsuite-7.0.2
fcmake;
