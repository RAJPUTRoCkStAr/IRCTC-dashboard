import streamlit as st
from streamlit_lottie import st_lottie
from Datacollect import trainbtst 
from lott import lottie_Trainbwstation
def ttraint():
    st.header("Train Time Table with station :train2: ",divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write('Our project includes a "Train Between Stations" feature, allowing users to find trains operating between two specified stations. By entering the departure and destination station names, users can access a list of available trains, including departure and arrival times, travel duration, and train types. The system provides comprehensive details for each train, such as class options and days of operation. The user-friendly interface ensures quick and easy searches, helping travelers plan their journeys efficiently. This tool is designed to offer reliable and up-to-date information, making it simpler to find and choose the best travel options between any two stations.')
    with col2:
        st_lottie(lottie_Trainbwstation, speed=1, reverse=True, loop=True, quality='medium', height=380, width=580, key=None)
    fromsta = st.text_input('from Station Name')
    tosta = st.text_input(' to Station Name')
    if st.button('Get Train Time Table'):
        if fromsta and tosta:
            with st.spinner(f"Fetching Time Table of station from :red-background[{fromsta}] to :red-background[{tosta}]  :tram:"):
                df = trainbtst(fromsta,tosta)
                st.dataframe(df,hide_index=True,use_container_width=True)
        else:
            st.warning('Please provide station code')