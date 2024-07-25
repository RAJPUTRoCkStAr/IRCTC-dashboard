import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from lott import lottie_me, lottie_home, lottie_over
from Stsocialicon import SocialMediaIcons

def home():
    st.subheader("Welcome to the IRCTC Dashboard 👋", divider='rainbow')
    col1, col2 = st.columns([3,3])
    with col1:
        st.write(
            """
            The IRCTC Dashboard project aims to streamline the travel experience for Indian Railway passengers with a robust, user-friendly platform. 
            Key features include real-time updates on train schedules and statuses, seamless booking services for tickets and amenities, instant PNR status checks, 
            comprehensive route and schedule information, personalized user accounts for efficient management, timely alerts and notifications, and dedicated customer support. 
            By integrating these features, the IRCTC Dashboard enhances convenience and accessibility, ensuring a smooth journey for millions of travelers across India.
            """
        )
        st.write("From booking tickets to checking train schedules and more, we've got you covered.")
        st.write("Explore essential features and services for seamless railway navigation.")
    
    with col2:
        st_lottie(lottie_home, speed=1, reverse=True, loop=True, quality='medium', height=380, width=680, key=None)

    tab = option_menu(
        None, 
        ["Overview 🗒️", "About Me 👨‍💻", "Future Enhancements 📈"], 
        orientation="horizontal",
        icons=['journal', 'person-workspace', 'journal-code']
    )

    if tab == "Overview 🗒️":
        col3, col4 = st.columns([4, 2])

        with col3:     
            st.subheader("Overview: 🗒️",divider='rainbow')
            st.markdown("- **Train Time Table:** View detailed schedules for all trains.")
            st.markdown("- **Trains Between Stations:** Find trains between specific stations.")
            st.markdown("- **PNR Status:** Quickly verify your ticket status with PNR number.")
            st.markdown("- **Fare Details:** Get detailed fare information for different classes and trains.")
            st.markdown("- **Seat Availability:** Check seat availability for specific trains and dates.")
            st.markdown("- **Train Running Status:** Real-time updates on train running status.")
            st.markdown("- **Running History:** Historical data on train timings and performance.")
            st.markdown("- **Important Stations:** Information on key stations, including amenities and services.")
            st.markdown("- **Station Information:** Comprehensive data on all railway stations.")
            st.markdown("- **Train Information:** Detailed information on each train, including routes and schedules.")
            
            st.subheader("How to Use:",divider='rainbow')
            st.markdown("1. Navigate to the relevant section to access specific information.")
            st.markdown("2. Use 'Train Time Table' to view detailed schedules.")
            st.markdown("3. 'Trains Between Stations' helps you find available trains between your desired stations.")
            st.markdown("4. 'PNR Status' allows you to check your ticket status.")
            st.markdown("5. 'Fare Details' provides fare information for different trains and classes.")
            st.markdown("6. 'Seat Availability' helps you check available seats in specific trains.")
            st.markdown("7. 'Train Running Status' provides real-time updates on train status.")
            st.markdown("8. 'Running History' gives historical performance data for trains.")
            st.markdown("9. 'Important Stations' offers information on major stations.")
            st.markdown("10. 'Station Information' and 'Train Information' provide detailed data on all stations and trains.")

        with col4:
            st_lottie(lottie_over, speed=1, reverse=True, loop=True, quality='medium', height=480, width=580, key=None)

    elif tab == "About Me 👨‍💻":
        col5, col6 = st.columns([3, 3])

        with col5:
            st.subheader("About Me: 👨‍💻",divider='rainbow')
            st.write("Hi there 👋, I'm Sumit Kumar Singh, the creator of the IRCTC Dashboard.")
            st.write("👨‍💻 A passionate Full Stack and Python Developer from India.")
            st.write("⚡ Fun fact: I enjoy coding so much that sometimes I feel like I'm in my own world of algorithms!")
            st.write("🚀 Always exploring new technologies and building cool projects.")
            st.write("🎨 Love creating clean, efficient, and user-friendly designs.")
            st.write("Let's connect and collaborate on exciting projects! 🤝")

            expander = st.expander("Contact me 📱", expanded=False)
            with expander:
                social_media_links = [
                    "https://www.instagram.com/sumit_kumarsingh22?utm_source=qr&igsh=Manufacturing==",
                    "https://github.com/RAJPUTRoCkStAr",
                    "https://www.linkedin.com/in/sumit-singh-773921262/",
                    "https://x.com/Sumit92293207",
                    "https://www.kaggle.com/sumitkumarsingh22002",
                ]
                sizes = ['lg', 'lg', 'lg', 'lg', 'lg']
                SocialMediaIcons(social_media_links=social_media_links, sizes=sizes).generate_icons()
                st.write("📫 Reach me: sumitsingh9441@gmail.com")
        
        with col6:
            st_lottie(lottie_me, speed=1, reverse=True, loop=True, quality='medium', height=None, width=None, key=None)

    elif tab == "Future Enhancements 📈":  
        st.subheader("Future Enhancements: 📈",divider='rainbow')
        st.write("- **Train Time Table Prediction:** Implement predictive analytics to forecast train schedules based on historical data and real-time updates.")
        st.write("- **Comparing Time and Price:** Develop features to compare travel time and ticket prices across different trains and classes for optimal choices.")
        st.write("- **Tatkal Ticket Booking Automation:** Automate the process of booking Tatkal tickets to improve the chances of securing tickets during high demand periods.")
        st.write("- **Real-time Train Status Updates:** Implement real-time updates on train statuses, including delays, cancellations, and platform changes, to provide users with the most current information.")
        st.write("- **Personalized Recommendations:** Utilize machine learning algorithms to offer personalized recommendations for travel packages, local attractions, and dining options based on user preferences and past bookings.")
        st.write("- **Integration with Mobile Platforms:** Create a mobile app version of the dashboard for seamless access on smartphones and tablets, ensuring users can manage their travel plans on the go.")
        st.write("- **Enhanced User Authentication:** Implement secure user authentication methods such as biometric verification or two-factor authentication (2FA) to enhance account security and personalized experiences.")
        st.write("- **Voice Assistant Integration:** Integrate voice recognition technology to allow users to interact with the dashboard hands-free, providing information and booking services through natural language commands.")
        st.write("- **Feedback and Rating System:** Incorporate a feedback system where users can rate their travel experiences, provide suggestions, and share reviews, helping to improve service quality and user satisfaction.")
        st.write("- **Alert for Trains:** Implement alert notifications for changes in train schedules, seat availability, and more to keep users informed.")
        st.write("- **Social Media Integration:** Allow users to share their travel plans, experiences, and reviews directly from the dashboard to social media platforms, enhancing user engagement and promoting the dashboard organically.")
    
    st.write("⭐ Feel free to explore the app and stay tuned for future updates!")