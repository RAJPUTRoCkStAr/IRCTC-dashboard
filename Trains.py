import streamlit as st
from Datacollect import train_running_status, add_months
from streamlit_lottie import st_lottie
from lott import lottie_livetrain
import datetime

def train_st():
    st.header("Train Running Status 🚆", divider='rainbow')

    col1, col2 = st.columns([3, 3])

    with col1:
        st.write("""
            This feature provides real-time updates on train movements. By entering the train number and date, 
            users can access current information about the train's location, estimated arrival and departure times 
            at upcoming stations, and any delays. The system offers accurate and up-to-date details, ensuring travelers 
            are well-informed about their journey's progress. The interface is designed for ease of use, allowing for quick 
            tracking of train status and helping users adjust their plans as needed. This tool is essential for staying informed 
            about train schedules and ensuring a smooth travel experience.
        """)
    
    with col2:
        st_lottie(lottie_livetrain, speed=1, reverse=True, loop=True, quality='medium', height=380, width=680, key=None)

    today = datetime.date.today()
    five_months = add_months(today, 5)

    trains_no = st.number_input('Train Number', value=None, format='%d')
    trains_date = st.date_input('Train Date', min_value=today, max_value=five_months)

    if st.button('Spot Your Train'):
        if trains_no and trains_date:
            with st.spinner(f"Fetching data for train number {int(trains_no)} on date {trains_date.strftime('%d %b %Y')}..."):
                df = train_running_status(trains_no, trains_date)
                if df is not None and not df.empty:
                    st.dataframe(df, hide_index=True, use_container_width=True, height=900)
                else:
                    st.error("No data found for the provided train number and date. Please check the details and try again.")
        else:
            st.warning("Please provide both train number and train date.")

