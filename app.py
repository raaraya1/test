import streamlit as st
import subprocess

subprocess.call(["apt-get update"])
out = subprocess.call(["ls"]).stdout.read()
st.write(str(out))

#python setup.py install
