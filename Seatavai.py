import streamlit as st
import datetime
from streamlit_lottie import st_lottie
from Datacollect import seat_avail,add_months 
from lott import lottie_seatavail

def seatav():
    st.header("Train Seat Availability :seat:",divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write('Our project features a seat availability checker for train journeys. By entering the train number and travel date, users can quickly view the availability of seats across different classes, such as sleeper, AC, and premium categories. The system provides real-time updates on the number of seats available, along with options for reservation. The intuitive interface makes it easy to check availability and plan bookings accordingly. This tool ensures travelers have up-to-date information on seat options, helping them make informed decisions and secure their travel plans with confidence.')
    with col2:
        st_lottie(lottie_seatavail, speed=1, reverse=True, loop=True, quality='medium', height=280, width=580, key=None)
    from_station = st.text_input("From Station")
    to_station = st.text_input("To Station")
    today = datetime.date.today()
    five_months = add_months(today, 5)
    date = st.date_input("Date",max_value=five_months,min_value=today)
    if st.button("Check Availability"):
        if from_station and to_station and date:
            with st.spinner(f"Checking Seat Availability from :red-background[{from_station}] to :red-background[{to_station}] on :red-background[{date.strftime('%d %b %Y')}] :train2:"):
                formatted_date = date.strftime("%d-%m-%Y")
                dfs = seat_avail(from_station, to_station, formatted_date)
                if dfs:
                    st.write("Train Details:")
                    for idx, df in enumerate(dfs):
                        st.markdown(f"### Train {idx + 1}")
                        st.dataframe(df)
                else:
                    st.write("No data available or there was an error.")
        else:
            st.write("Please enter all fields.")

