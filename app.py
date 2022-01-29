import streamlit as st
import subprocess
import os

#cmd =  "sh SCIPOptSuite-7.0.2-Linux-debian.sh"
#os.system("cmake -Bbuild -H. [-DSOPLEX_DIR=/path/to/soplex]")
#os.system("cmake --build build")
os.system("tar xvzf scipoptsuite-7.0.2.tgz")
os.system("cd scipoptsuite-7.0.2")
os.system("cd scip")
os.system("mkdir build")
os.system("cd build")
os.system("cmake .. [-DSOPLEX_DIR=/path/to/soplex]")
os.system("make")
# optional: run a quick check on some instances
os.system("make check")
# optional: install scip executable, library, and headers
os.system("make install")




#python setup.py install
