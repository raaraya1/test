import streamlit as st
import subprocess
import os

os.system("tar SCIPOptSuite-7.0.2.gz")
cmd =  "sh SCIPOptSuite-7.0.2-Linux-debian.sh"
os.system(cmd)





#python setup.py install
