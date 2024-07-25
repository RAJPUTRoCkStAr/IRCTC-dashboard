import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from lott import lottie_searchstt
import pandas as pd
def get_stationt():
    st.header('Unified Station and Train Information System',divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write("""
    This feature integrates a comprehensive station and train database, built from extensive data scraping of all stations and train codes. 
    The system provides detailed information about each station, including its code, facilities, and services. Users can also access a complete 
    list of trains associated with each station, with real-time data on arrivals and departures for the next 24 hours. The tool displays train 
    numbers, departure and arrival times, platform information, and any delays. With a user-friendly interface, this system presents data clearly, 
    making travel planning efficient and ensuring users have access to the most accurate and up-to-date information available.
    """)
    with col2:
        st_lottie(lottie_searchstt, speed=1, reverse=True, loop=True, quality='medium', height=280, width=680, key=None)
    tabs = option_menu(None, ["Train", "Station"], orientation="horizontal")
    
    if tabs == "Train":
        st.subheader("All Type of train Detail",divider='rainbow')
        st.dataframe(pd.read_csv('./csvdata/traindata.csv', dtype={'Train Number': str}),hide_index=True,use_container_width=True,height=900)
    if tabs == "Station":
        st.subheader("All Type of station Detail",divider='rainbow')
        st.dataframe(pd.read_csv('./csvdata/trainavailability.csv'),hide_index=True,use_container_width=True,height=900)
        