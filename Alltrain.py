import streamlit as st
from streamlit_lottie import st_lottie
from Datacollect import allTrains, allstation
from lott import lottie_impstt

def station_inf():
    st.header("Station Information and upcoming Trains :tram:", divider='rainbow')

    # Description and animation columns
    col1, col2 = st.columns([3, 3])
    with col1:
        st.write("""
    This feature provides comprehensive information about all trains scheduled at a selected station for the next 24 hours. By choosing a station, 
    you can view a complete list of trains arriving and departing within the next day. The system offers essential details such as train numbers, 
    departure and arrival times, platform assignments, and any expected delays. With a user-friendly interface, accessing this information is easy 
    and efficient, helping you plan your visits and connections effectively. This tool ensures you stay well-informed about train schedules and station 
    activities with clear and up-to-date details.
    """)
    with col2:
        st_lottie(lottie_impstt, speed=1, reverse=True, loop=True, quality='medium', height=380, width=680)

    train_code = st.text_input('Enter Train Code')

    def fetch_details(fetch_function, loading_message, success_message, empty_message, error_message):
        if train_code:
            with st.spinner(loading_message.format(train_code)):
                try:
                    df = fetch_function(train_code)
                    if df.empty:
                        st.write(empty_message)
                    else:
                        st.dataframe(df, hide_index=True, use_container_width=True)
                except Exception as e:
                    st.error(f"{error_message}: {e}")
        else:
            st.warning("Please enter a train code.")

    if st.button('Fetch Train Details'):
        fetch_details(allTrains, "Fetching data of upcoming train on :red-background[{}]:train2:", 
                      "Train details fetched successfully.", "No data.", "An error occurred")

    if st.button('Fetch Station Details'):
        fetch_details(allstation, "Fetching station details :red-background[{}]:train2:", 
                      "Station details fetched successfully.", "No data found for this train.", "An error occurred")
