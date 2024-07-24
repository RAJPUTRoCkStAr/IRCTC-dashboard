import streamlit as st
import pandas as pd
from Datacollect import importanst
from streamlit_lottie import st_lottie
from lott import lottie_firstpag
def imp():
    st.subheader('All Important station and Train :train2:',divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write('Our project features an "Important Stations and Trains" tool that provides detailed information about key stations and their associated trains. Users can select any major station to view a comprehensive list of all trains arriving and departing within the next 24 hours. The system delivers essential details, including train numbers, departure and arrival times, platform assignments, and any delays. Additionally, users can access specific information about each important station, such as available facilities, services, and accessibility features. The intuitive interface ensures quick and easy access to up-to-date information, aiding travelers in planning their journeys and managing connections efficiently. This tool is designed to keep users well-informed and enhance their travel experience with clear and accurate data.')
    with col2:
        st_lottie(lottie_firstpag, speed=1, reverse=True, loop=True, quality='medium', height=380, width=580, key=None)
    train_numbers, train_names = importanst()
    df = pd.DataFrame({"Train Number": train_numbers, "Train Name": train_names})
    st.dataframe(df)