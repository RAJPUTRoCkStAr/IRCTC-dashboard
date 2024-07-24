import streamlit as st
from Datacollect import faredetails  
from streamlit_lottie import st_lottie
from lott import lottie_fare
def faredetail():
    st.header("Check Fare Details :money_with_wings:",divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write('Our project includes a comprehensive ticket fare details feature. By entering a train number or route information, users can access specific fare details, including base fare, taxes, and additional charges for various classes of travel. The system provides a breakdown of costs for different seat types, such as sleeper, AC, and premium classes, and displays any available discounts or special offers. The user-friendly interface ensures that fare information is easy to understand and navigate, allowing travelers to plan their budgets effectively. This feature is designed to give clear, detailed fare information, helping users make informed decisions about their travel arrangements.')
    with col2:
        st_lottie(lottie_fare, speed=1, reverse=True, loop=True, quality='medium', height=380, width=580, key=None)
    fairdet_no = st.text_input("Enter Train Number:")
    arr_st = st.text_input("Enter From Station Code:")
    dep_st = st.text_input("Enter To Station Code:")

    if st.button("Get Fare Details"):
        if fairdet_no and arr_st and dep_st:
            with st.spinner(f"Fetching data of :red-background[{fairdet_no}] from :red-background[{arr_st}] to :red-background[{dep_st}] :train2: "):
                df1, df2 = faredetails(fairdet_no, arr_st, dep_st)
                if not df1.empty and not df2.empty:
                    st.subheader("Train Details :train:",divider='rainbow')
                    df1.columns = df1.iloc[0] 
                    df1 = df1[1:].reset_index(drop=True)  
                    st.dataframe(df1,hide_index=True,use_container_width=True)
                    st.subheader("Fare Details :moneybag:",divider='rainbow')
                    st.dataframe(df2,hide_index=True,use_container_width=True)
                else:
                    st.error("No data found or there was an issue fetching data.")
        else:
            st.error("Please fill in all input fields.")