import streamlit as st
import subprocess
import os

#cmd =  "sh SCIPOptSuite-7.0.2-Linux-debian.sh"
os.system("tar xvzf scipoptsuite-7.0.2.tgz")
os.system("cd scipoptsuite-7.0.2")
os.system("./configure")
os.system("make")
os.system("make gcg")

#os.system(cmd)


#python setup.py install
