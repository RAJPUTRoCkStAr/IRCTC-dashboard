import streamlit as st
import pandas as pd
from Datacollect import faredetails  
from streamlit_lottie import st_lottie
from lott import lottie_fare

def clean_dataframe(df):
    """
    Ensure that the dataframe has unique column names.
    """
    cols = pd.Series(df.columns)
    for dup in cols[cols.duplicated()].unique(): 
        cols[cols[cols == dup].index.values.tolist()] = [dup + '_' + str(i) if i != 0 else dup for i in range(sum(cols == dup))]
    df.columns = cols
    return df

def filter_seat_types(df, seat_types):
    """
    Filter dataframe to include only specific seat types.
    """
    if 'Seat Type' in df.columns:
        return df[df['Seat Type'].isin(seat_types)]
    return pd.DataFrame()

def calculate_differences(df1, df2):
    """
    Calculate differences between two dataframes and return a dataframe with differences.
    Assumes df1 and df2 have the same structure.
    """
    try:
        # Clean the dataframes
        df1 = clean_dataframe(df1)
        df2 = clean_dataframe(df2)
        
        # Align the dataframes by columns
        df1 = df1.set_index('Seat Type')
        df2 = df2.set_index('Seat Type')
        
        # Calculate differences
        diff_df = df1 - df2
        diff_df.reset_index(inplace=True)
        
        return diff_df
    except Exception as e:
        return pd.DataFrame({"Error": [str(e)]})

def faredetail():
    st.header("Check Fare Details :money_with_wings:", divider='rainbow')
    col1, col2 = st.columns([3, 3])
    with col1:
        st.write('Our project includes a comprehensive ticket fare details feature. By entering multiple train numbers and route information, users can access specific fare details, including base fare, taxes, and additional charges for various classes of travel. The system provides a breakdown of costs for different seat types, such as sleeper, AC, and premium classes, and displays any available discounts or special offers. The user-friendly interface ensures that fare information is easy to understand and navigate, allowing travelers to plan their budgets effectively. This feature is designed to give clear, detailed fare information, helping users make informed decisions about their travel arrangements.')
    with col2:
        st_lottie(lottie_fare, speed=1, reverse=True, loop=True, quality='medium', height=380, width=580, key=None)

    train_numbers = st.text_area("Enter Train Numbers (comma separated):")
    arr_st = st.text_input("Enter From Station Code:")
    dep_st = st.text_input("Enter To Station Code:")

    seat_types = ['3A', '2A', '1A', 'SL']

    if st.button("Get Fare Details"):
        if train_numbers and arr_st and dep_st:
            train_numbers_list = [train.strip() for train in train_numbers.split(',')]
            results = {}
            differences = {}

            with st.spinner("Fetching data..."):
                for train_number in train_numbers_list:
                    df1, df2 = faredetails(train_number, arr_st, dep_st)
                    if not df1.empty and not df2.empty:
                        df1.columns = df1.iloc[0]
                        df1 = df1[1:].reset_index(drop=True)
                        df2.columns = df2.iloc[0]
                        df2 = df2[1:].reset_index(drop=True)
                        
                        # Filter dataframes to include only relevant seat types
                        df1 = filter_seat_types(df1, seat_types)
                        df2 = filter_seat_types(df2, seat_types)

                        results[train_number] = (df1, df2)
                        
                        # Calculate differences between the fare details
                        if len(results) > 1:
                            previous_train_number = train_numbers_list[train_numbers_list.index(train_number) - 1]
                            prev_df1, prev_df2 = results[previous_train_number]
                            diff = calculate_differences(prev_df2, df2)
                            differences[train_number] = diff
                    else:
                        results[train_number] = ("No data found or issue fetching data.", "No data found or issue fetching data.")
                
                st.subheader("Comparison of Fare Details :moneybag:", divider='rainbow')
                for train_number, (df1, df2) in results.items():
                    st.subheader(f"Train {train_number} Details :train:", divider='rainbow')
                    if isinstance(df1, str):
                        st.error(df1)
                    else:
                        st.dataframe(df1, hide_index=True, use_container_width=True)
                    
                    st.subheader(f"Train {train_number} Fare Details :moneybag:", divider='rainbow')
                    if isinstance(df2, str):
                        st.error(df2)
                    else:
                        st.dataframe(df2, hide_index=True, use_container_width=True)
                
                if len(differences) > 0:
                    st.subheader("Fare Differences Between Trains :chart_with_upwards_trend:", divider='rainbow')
                    for train_number, diff_df in differences.items():
                        st.subheader(f"Difference with Previous Train {train_number} :bar_chart:", divider='rainbow')
                        if diff_df.empty:
                            st.error("Error calculating differences.")
                        else:
                            st.dataframe(diff_df, hide_index=True, use_container_width=True)
        else:
            st.error("Please fill in all input fields.")
faredetail()