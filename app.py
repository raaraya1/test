import streamlit as st
import subprocess
import os

st.write(os.getcwd())
#os.system("apt-get update")
#os.system("apt-get install build-essential libreadline-dev libz-dev libgmp3-dev lib32ncurses5-dev libboost-program-options-dev")
#subprocess.call('cd /app/test/scipoptsuite-7.0.2', shell=True)
#subprocess.call('ls', shell=True)
#os.system("cd build")
#os.system("pwd")
#os.system("apt-get install cmake")
#os.system("mkdir build")
#os.system("cd build")
os.system("cmake /app/test/scipoptsuite-7.0.2| tail -n +91")
os.system("ls")
#os.system("make")
#os.system("make install")



#os.system("sh setupscip.sh")
