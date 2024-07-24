import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from lott import lottie_firstpag
def imp():
    st.subheader('All Important station and Train :train2:',divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write('Our project features an "Important Stations and Trains" tool that provides detailed information about key stations and their associated trains. Users can select any major station to view a comprehensive list of all trains arriving and departing within the next 24 hours. The system delivers essential details, including train numbers, departure and arrival times, platform assignments, and any delays. Additionally, users can access specific information about each important station, such as available facilities, services, and accessibility features. The intuitive interface ensures quick and easy access to up-to-date information, aiding travelers in planning their journeys and managing connections efficiently. This tool is designed to keep users well-informed and enhance their travel experience with clear and accurate data.')
    with col2:
        st_lottie(lottie_firstpag, speed=1, reverse=True, loop=True, quality='medium', height=380, width=580, key=None)
    tab = option_menu(None, ['🌟Stations','Rajdhani','Shatabdi','Garib_Rath','Duronto','Tourism','Special'], orientation="horizontal")
    if tab == '🌟Stations':
        st.subheader('Important_Stations',divider='rainbow')
        st.dataframe(pd.read_csv('./csvdata/istation.csv'),hide_index=True,use_container_width=True,height=900)
    elif tab == 'Rajdhani':
        st.subheader('Rajdhani',divider='rainbow')
        st.dataframe(pd.read_csv('./csvdata/raj.csv', dtype={'Train Number': str}),hide_index=True,use_container_width=True,height=900)
    elif tab == 'Shatabdi':
        st.subheader('Shatabdi',divider='rainbow')
        st.dataframe(pd.read_csv('./csvdata/shat.csv', dtype={'Train Number': str}),hide_index=True,use_container_width=True,height=900)
    elif tab == 'Duronto':
        st.subheader('Duronto',divider='rainbow')
        st.dataframe(pd.read_csv('./csvdata/dornto.csv', dtype={'Train Number': str}),hide_index=True,use_container_width=True,height=900)
    elif tab == 'Garib_Rath':
        st.subheader('Garib_Rath_Yuva',divider='rainbow')
        st.dataframe(pd.read_csv('./csvdata/garib.csv', dtype={'Train Number': str}),hide_index=True,use_container_width=True,height=900)
    elif tab == 'Tourism':
        st.subheader('Tourism',divider='rainbow')
        st.dataframe(pd.read_csv('./csvdata/torsim.csv', dtype={'Train Number': str}),hide_index=True,use_container_width=True,height=350)
    elif tab == 'Special':
        st.subheader('Special',divider='rainbow')
        st.dataframe(pd.read_csv('./csvdata/spec.csv', dtype={'Train Number': str}),hide_index=True,use_container_width=True,height=900)