import streamlit as st
from Datacollect import train_running_history
from streamlit_lottie import st_lottie
from lott import lottie_histo
def trainhist():
    st.subheader('Train Running History :oncoming_bus:',divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write('Our project features a train running history tracker that provides detailed records of a trains past performance. By entering the train number, users can access historical data, including previous departure and arrival times, delays, and on-time performance statistics. This system offers a comprehensive view of a trains reliability and punctuality over time. The intuitive interface ensures easy navigation and access to valuable insights, helping travelers make informed decisions based on a trains track record. This tool is ideal for analyzing trends and planning journeys with confidence, ensuring a smooth and well-informed travel experience.')
    with col2:
        st_lottie(lottie_histo, speed=1, reverse=True, loop=True, quality='medium', height=380, width=580, key=None)
    trainh_no = st.number_input('Train Number',value=None,format='%d')
    if st.button('Train Running History'):
        if trainh_no:
            with st.spinner(f"Fetching data for train number :red-background[{int(trainh_no)}] :tram:"):
                df = train_running_history(trainh_no)
                st.dataframe(df,hide_index=True,use_container_width=True)
        else:
            st.warning('Please provide a train number')