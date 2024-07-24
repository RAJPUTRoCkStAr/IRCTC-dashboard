import streamlit as st
import pandas as pd
from Datacollect import pnrsta
from lott import lottie_PNR
from streamlit_lottie import st_lottie

def pnrst():
    st.header('PNR Status Checker :ticket:',divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write('Our project includes a PNR status checker that allows users to quickly find the status of their train bookings. By entering a PNR number, users can access real-time updates on their reservation, including current status, seat allocation, and any changes or delays. The system provides clear and accurate information, ensuring that travelers are informed about their journeys details. With a user-friendly interface, accessing PNR status is simple and efficient, making travel planning more reliable and hassle-free. This tool helps users stay updated on their bookings and make informed decisions about their travel plans.')
    with col2:
        st_lottie(lottie_PNR, speed=1, reverse=True, loop=True, quality='medium', height=380, width=580, key=None)
    pnr_no = st.number_input('PNR Number',value=None,format='%d')
    if st.button('Check Status'):
        if pnr_no:
            with st.spinner(f'Fetching status :red-background[{int(pnr_no)}]:ticket:'):
                try:
                    result = pnrsta(pnr_no)
                    if result.get('status'):
                        data = result.get('data', {})
                        st.markdown("### Train Information")
                        train_info = {
                            "Train Name": data.get('TrainName', 'N/A'),
                            "Train Number": data.get('TrainNo', 'N/A'),
                            "Class": data.get('Class', 'N/A'),
                            "Boarding Station": data.get('BoardingStationName', 'N/A'),
                            "Departure": data.get('DepartureTime', 'N/A'),
                            "Arrival": data.get('ArrivalTime', 'N/A'),
                            "Duration": data.get('Duration', 'N/A'),
                            "Quota": data.get('Quota', 'N/A'),
                            "Reservation Upto": data.get('ReservationUptoName', 'N/A'),
                            "Source": data.get('SourceName', 'N/A'),
                            "Destination": data.get('DestinationName', 'N/A'),
                            "Expected Platform": data.get('ExpectedPlatformNo', 'N/A')
                        }                   
                        st.write(
                            f"""
                            <div class="card">
                                <h3>Train Information</h3>
                                {' '.join([f'<p><strong>{key}:</strong> {value}</p>' for key, value in train_info.items()])}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        st.markdown("### Passenger Information")
                        passenger_list = data.get('PassengerStatus', [])  
                        if passenger_list:
                            passenger_df = pd.DataFrame([{
                                "Number": p.get('Number', 'N/A'),
                                "Berth": p.get('Berth', 'N/A'),
                                "Booking Status": p.get('BookingStatus', 'N/A'),
                                "Current Status": p.get('CurrentStatus', 'N/A'),
                                "Prediction": p.get('Prediction', 'N/A')
                            } for p in passenger_list])
                            
                            st.dataframe(passenger_df)
                        st.markdown("### Ratings and Other Details")
                        ratings_info = {
                            "Food Rating": data.get('FoodRating', 'N/A'),
                            "Punctuality Rating": data.get('PunctualityRating', 'N/A'),
                            "Cleanliness Rating": data.get('CleanlinessRating', 'N/A'),
                            "Booking Fare": f"₹{data.get('BookingFare', 'N/A')}",
                            "Ticket Fare": f"₹{data.get('TicketFare', 'N/A')}"
                        } 
                        st.write(
                            f"""
                            <div class="card">
                                <h3>Ratings and Other Details</h3>
                                {' '.join([f'<p><strong>{key}:</strong> {value}</p>' for key, value in ratings_info.items()])}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    else:
                        st.error(result.get('message', 'An error occurred'))
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning('Please enter a PNR number.')
    