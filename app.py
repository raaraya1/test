import streamlit as st
import subprocess
import os

st.write(os.getcwd())
#os.system("cd build")
#os.system("pwd")
#os.system("apt-get install cmake")
os.system("mkdir /app/test/scipoptsuite-7.0.2/build")
os.system("cmake /app/test/scipoptsuite-7.0.2/build | tail -n +91")
os.system("make /app/test/scipoptsuite-7.0.2/build")
os.system("make install")

#os.system("make")
#os.system("make install")



#os.system("sh setupscip.sh")
