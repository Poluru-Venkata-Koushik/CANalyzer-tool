import streamlit as st
import json
import time
import sys
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

with open('SessionData.json') as sessdata:
    sessionInfo = json.load(sessdata)

#st_autorefresh(interval=500)

def on_quit():
    status_box = st.status("Starting...", state='running')

    for i in range(5):
        status_box.write(f"Step {i+1}/5: processing...")
        time.sleep(1)

    status_box.write("Done!")
    status_box.empty()
    st.stop()

st.title(":rainbow[CAN]alyzer")

def onRegister():
    a = st.expander("Register ECU")
    a.text_input("ID")

sidebar1 = st.sidebar
sidebar1.title(" Tools")
sidebar1.button("Register ECU", use_container_width=True, on_click= onRegister)
sidebar1.button("Analyse CSV", use_container_width=True)
sidebar1.button("Quit", use_container_width= True, on_click=on_quit)

st.write("""
    ##### CAN Packet Structure  :
""")

packetStructure = st.columns(12)
packetStructure[0].text(" | SOF |")
packetStructure[1].text(" | ID |")
packetStructure[2].text(" | RTR |")
packetStructure[3].text(" | IDE |")
packetStructure[4].text(" | res |")
packetStructure[5].text(" | DLC |")
packetStructure[6].text(" | DAT |")
packetStructure[7].text(" | CRC |")
packetStructure[8].text(" |CRC'|")
packetStructure[9].text(" | ACK |")
packetStructure[10].text(" |ACK'|")
packetStructure[11].text(" | EOF |")


st.write("""
    ##### Registered ECUs :
""")


if st.button("Open User Input"):
    with st.expander("User Input (Simulated Modal)", expanded=True):
        name = st.text_input("Enter your name:")
        age = st.number_input("Enter your age:", min_value=0)
        st.write(f"Name: {name}, Age: {age}")


