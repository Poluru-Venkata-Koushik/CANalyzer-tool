import streamlit as st
import time

def on_quit():
    status_box = st.status("Starting...", state='running')

    for i in range(3):
        status_box.write(f"Step {i+1}/5: processing...")
        time.sleep(1)

    status_box.write("Done!")
    status_box.empty()
    st.stop()

st.title(":rainbow[CAN]alyzer")

sidebar1 = st.sidebar
sidebar1.title(" Tools")
sidebar1.button("Analyse CSV", use_container_width=True)
sidebar1.button("Quit", use_container_width= True, on_click=on_quit)

class OnQuit():
    def __init__(self):
        status_box = st.status("Starting...", state='running')

        for i in range(3):
            status_box.write(f"Step {i+1}/5: processing...")
            time.sleep(1)

        status_box.write("Done!")
        status_box.empty()
        st.stop()

class MainStuff():
    def __init__(self):
        st.title(":rainbow[CAN]alyzer")

OnQuit()
MainStuff()

ID = st.