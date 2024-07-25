import streamlit as st
import pandas as pd
import plotly.express as px
from Datacollect import faredetails, trainbtst
from streamlit_lottie import st_lottie
from lott import lottie_fare, lottie_Trainbwstation

# Function to fetch train timetable
def fetch_timetable(fromsta, tosta):
    with st.spinner(f"Fetching timetable from {fromsta} to {tosta} :tram:"):
        timetable_df = trainbtst(fromsta, tosta)
        st.write("Timetable Data:")
        st.write(timetable_df.head())  # Display the first few rows for debugging
    return timetable_df

# Function to fetch fare details for multiple trains
def fetch_all_fares(train_no_list, arr_st, dep_st):
    fare_details_list = []
    for train_no in train_no_list:
        with st.spinner(f"Fetching fare details for train number {train_no} from {arr_st} to {dep_st} :red_train:"):
            fare_df1, fare_df2 = faredetails(train_no, arr_st, dep_st)
            if not fare_df2.empty:
                fare_df2['Train No'] = train_no  # Add train number to fare details
                fare_details_list.append(fare_df2)
                st.write(f"Fare Data for Train {train_no}:")
                st.write(fare_df2.head())  # Display the first few rows for debugging
    return pd.concat(fare_details_list) if fare_details_list else pd.DataFrame()

# Function to plot fare comparison using Plotly
def plot_fare_comparison(fare_df):
    if 'Travel Class' in fare_df.columns and 'Fare' in fare_df.columns:
        fig = px.bar(fare_df, x='Travel Class', y='Fare', color='Train No',
                     title='Fare Comparison by Travel Class for Different Trains',
                     labels={'Fare': 'Fare', 'Travel Class': 'Class'})
        fig.update_layout(xaxis_title='Class', yaxis_title='Fare')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Expected columns not found in fare details DataFrame.")

# Main function to run the Streamlit app
def main():
    st.header("Train Journey Information", divider='rainbow')

    # Train Time Table Section
    st.subheader("Train Time Table with station :train2: ", divider='rainbow')
    col3, col4 = st.columns([3, 3])
    
    with col3:
        st.write('Our project includes a "Train Between Stations" feature, allowing users to find trains operating between two specified stations. By entering the departure and destination station names, users can access a list of available trains, including departure and arrival times, travel duration, and train types. The system provides comprehensive details for each train, such as class options and days of operation. The user-friendly interface ensures quick and easy searches, helping travelers plan their journeys efficiently. This tool is designed to offer reliable and up-to-date information, making it simpler to find and choose the best travel options between any two stations.')
    
    with col4:
        st_lottie(lottie_Trainbwstation, speed=1, reverse=True, loop=True, quality='medium', height=380, width=580, key=None)

    fromsta = st.text_input('From Station Name')
    tosta = st.text_input('To Station Name')
    
    if st.button('Get Train Time Table'):
        if fromsta and tosta:
            timetable_df = fetch_timetable(fromsta, tosta)
            
            if timetable_df is not None and not timetable_df.empty:
                st.subheader("Available Trains")
                st.dataframe(timetable_df, hide_index=True, use_container_width=True)

                # Allow user to select a train for fare comparison
                if st.checkbox("Compare Fares for All Trains"):
                    train_no_list = timetable_df['Train No'].unique()
                    st.session_state.train_no_list = train_no_list
                    st.session_state.arr_st = fromsta
                    st.session_state.dep_st = tosta
            else:
                st.error("No timetable data found.")
        else:
            st.error("Please provide both station names.")

    if 'train_no_list' in st.session_state:
        st.subheader("Fare Comparison for Selected Trains")
        fare_df = fetch_all_fares(st.session_state.train_no_list, st.session_state.arr_st, st.session_state.dep_st)
        
        if fare_df is not None and not fare_df.empty:
            st.dataframe(fare_df, hide_index=True, use_container_width=True)
            plot_fare_comparison(fare_df)
        else:
            st.error("No fare details found.")

if __name__ == "__main__":
    main()
