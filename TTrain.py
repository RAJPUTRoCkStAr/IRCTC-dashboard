import streamlit as st
from streamlit_lottie import st_lottie
from Datacollect import trainbtst
from lott import lottie_Trainbwstation

def ttraint():
    st.header("Train Time Table Between Stations 🚂", divider='rainbow')

    col1, col2 = st.columns([3, 3])

    with col1:
        st.write("""
    This feature allows you to find trains operating between two specified stations. By entering the departure and destination station names, 
    you can access a list of available trains, including departure and arrival times, travel duration, and train types. The system provides 
    detailed information for each train, such as class options and days of operation. With a user-friendly interface, you can quickly and easily 
    search for trains, helping you plan your journeys efficiently. This tool is designed to provide reliable and up-to-date information, 
    making it simpler to find and choose the best travel options between any two stations.
""")
    
    with col2:
        st_lottie(lottie_Trainbwstation, speed=1, reverse=True, loop=True, quality='medium', height=380, width=680, key=None)

    fromsta = st.text_input('From Station Name')
    tosta = st.text_input('To Station Name')

    if st.button('Get Train Time Table'):
        if fromsta and tosta:
            with st.spinner(f"Fetching Time Table for trains from {fromsta} to {tosta} 🚄"):
                df = trainbtst(fromsta, tosta)
                if df is not None and not df.empty:
                    st.dataframe(df, hide_index=True, use_container_width=True)
                else:
                    st.error('No train data found for the given stations. Please check the station names and try again.')
        else:
            st.warning('Please provide both departure and destination station names.')