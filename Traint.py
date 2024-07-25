import streamlit as st
from streamlit_lottie import st_lottie
from Datacollect import traintimetable 
from lott import lottie_timetable
def traint():
    st.header("Train Time Table",divider='rainbow')
    col1,col2 = st.columns([4,2])
    with col1:
       st.write("""
    The train timetable feature offers an intuitive and accurate system designed for ease of use. By entering a train number, 
    you can instantly access the complete timetable for that train. This includes detailed information on departure and arrival times, 
    platform numbers, and any potential delays. Covering all major cities, the system provides comprehensive and up-to-date schedules 
    to help you plan your journeys efficiently. With a user-friendly interface, even first-time users can navigate the system effortlessly. 
    Whether you're a daily commuter or a first-time traveler, this tool simplifies the process of finding and understanding train schedules, 
    making travel planning more straightforward and less stressful. Enjoy reliable and precise train timetable information right at your fingertips.
    """)
    with col2:
        st_lottie(lottie_timetable, speed=1, reverse=True, loop=True, quality='medium', height=280, width=680, key=None)
    traint_num = st.number_input('Train Number',value=None,format='%d')
    if st.button('Get Train Time Table'):
        if traint_num:
            with st.spinner(f"Fetching Time Table of train number :red-background[{int(traint_num)}] :tram:"):
                df = traintimetable(traint_num)
                st.dataframe(df,hide_index=True,use_container_width=True,height=900)
        else:
            st.warning('Please provide train number')
