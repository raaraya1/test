import streamlit as st
import subprocess
out = subprocess.call(["ls"]).read()
st.write(out)

#python setup.py install
