import streamlit as st
import subprocess
import os

cmd =  "apt-get update"
os.system(cmd)

out = subprocess.call(["ls"]).stdout.read()
st.write(str(out))

#python setup.py install
