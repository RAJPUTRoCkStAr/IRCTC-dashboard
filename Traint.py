import streamlit as st
from streamlit_lottie import st_lottie
from Datacollect import traintimetable 
from lott import lottie_timetable
def traint():
    st.header("Train Time Table",divider='rainbow')
    col1,col2 = st.columns([4,2])
    with col1:
        st.write('Our project offers an intuitive train timetable system designed for ease of use and accuracy. By simply entering a train number, users can instantly access the complete timetable for that train, including detailed information on departure and arrival times, platform numbers, and any delays. The system covers all major cities, providing comprehensive and up-to-date schedules to assist travelers in planning their journeys efficiently. The user-friendly interface ensures that even first-time users can navigate the system with ease. Whether you are a daily commuter or a first-time traveler, our tool simplifies the process of finding and understanding train schedules, making travel planning more straightforward and less stressful. Enjoy reliable and precise train timetable information at your fingertips.')
    with col2:
        st_lottie(lottie_timetable, speed=1, reverse=True, loop=True, quality='medium', height=280, width=580, key=None)
    traint_num = st.number_input('Train Number',value=None,format='%d')
    if st.button('Get Train Time Table'):
        if traint_num:
            with st.spinner(f"Fetching Time Table of train number :red-background[{int(traint_num)}] :tram:"):
                df = traintimetable(traint_num)
                st.dataframe(df,hide_index=True,use_container_width=True,height=900)
        else:
            st.warning('Please provide train number')
