import streamlit as st
from Datacollect import train_running_history,add_months
from streamlit_lottie import st_lottie
from lott import lottie_histo
def trainhist():
    st.subheader('Train Running History :oncoming_bus:',divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write("""
    This feature provides a train running history tracker that offers detailed records of a train's past performance. By entering the train number, 
    users can access historical data, including previous departure and arrival times, delays, and on-time performance statistics. This system 
    delivers a comprehensive view of a train's reliability and punctuality over time. With an intuitive interface, users can easily navigate and 
    access valuable insights, helping them make informed decisions based on the train's track record. Ideal for analyzing trends and planning journeys, 
    this tool ensures a smooth and well-informed travel experience.
    """)

    with col2:
        st_lottie(lottie_histo, speed=1, reverse=True, loop=True, quality='medium', height=380, width=680, key=None)
    trainh_no = st.number_input('Train Number',value=None,format='%d')
    if st.button('Train Running History'):
        if trainh_no:
            with st.spinner(f"Fetching data for train number :red-background[{int(trainh_no)}] :tram:"):
                df = train_running_history(trainh_no)
                st.dataframe(df,hide_index=True,use_container_width=True,height=900)
        else:
            st.warning('Please provide a train number')