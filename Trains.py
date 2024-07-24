import streamlit as st
from Datacollect import train_running_status 
from streamlit_lottie import st_lottie
from lott import lottie_livetrain
def train_st():
    st.header("Train Running Status :light_rail:",divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write('Our project includes a train running status tracker for real-time updates on train movements. By entering the train number, users can access current information about the trains location, estimated arrival and departure times at upcoming stations, and any delays. The system provides accurate and up-to-date details, ensuring travelers are well-informed about their journeys progress. The user-friendly interface makes it easy to track the trains status, helping users adjust their plans as needed. This tool is essential for staying informed about train schedules and ensuring a smooth travel experience')
    with col2 :
        st_lottie(lottie_livetrain, speed=1, reverse=True, loop=True, quality='medium', height=380, width=580, key=None)
    trains_no = st.number_input('Train Number',value=None,format='%d')
    trains_date = st.date_input('Train Date')
    if st.button('Spot your train'):
        if trains_no and trains_date:
            if trains_no  and trains_date:
                with st.spinner(f"Fetching data for train number :red-background[{int(trains_no)}] on date :red-background[{trains_date.strftime('%d %b %Y')}]:tram:"):
                    df = train_running_status(trains_no, trains_date)
                    st.dataframe(df,hide_index=True,use_container_width=True)
        else:
            st.warning("Please Provide train number and train date")