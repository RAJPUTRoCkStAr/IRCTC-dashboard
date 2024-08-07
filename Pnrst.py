import streamlit as st
import pandas as pd
from Datacollect import get_pnr_status
from lott import lottie_PNR
from streamlit_lottie import st_lottie

def pnrst():
    st.header('PNR Status Checker :ticket:',divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write("""
    This feature includes a PNR status checker that allows you to quickly find the status of your train bookings. By entering a PNR number, 
    you can access real-time updates on your reservation, including the current status, seat allocation, and any changes or delays. The system 
    provides clear and accurate information, ensuring you are well-informed about your journey details. With a user-friendly interface, checking 
    PNR status is straightforward and efficient, making travel planning more reliable and hassle-free. This tool helps you stay updated on your 
    bookings and make informed decisions about your travel plans.
""")

    with col2:
        st_lottie(lottie_PNR, speed=1, reverse=True, loop=True, quality='medium', height=380, width=680, key=None)
    pnr_no = st.text_input("Enter PNR Number:")
    if st.button("Fetch PNR Number"):
        if pnr_no:
            with st.spinner('Fetching PNR status...'):
                pnr_data = get_pnr_status(pnr_no)
                if pnr_data:
                    df = pd.DataFrame([pnr_data])
                    st.dataframe(df,hide_index=True,use_container_width=True)
                else:
                    st.error("Failed to fetch PNR status. Please try again.")