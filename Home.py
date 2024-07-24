import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from lott import lottie_me,lottie_home,lottie_over
from Stsocialicon import SocialMediaIcons
def home():
    st.subheader("Welcome to the IRCTC Dashboard 👋",divider='rainbow')
    col1,col2 = st.columns([3,3])
    with col1:
        st.write('The IRCTC Dashboard project aims to streamline the travel experience for Indian Railway passengers with a robust, user-friendly platform. Key features include real-time updates on train schedules and statuses, seamless booking services for tickets and amenities, instant PNR status checks, comprehensive route and schedule information, personalized user accounts for efficient management, timely alerts and notifications, and dedicated customer support. By integrating these features, the IRCTC Dashboard enhances convenience and accessibility, ensuring a smooth journey for millions of travelers across India.')
        st.write("From booking tickets to checking train schedules and more, we've got you covered.")
        st.write("Explore essential features and services for seamless railway navigation.")
    with col2:
        st_lottie(lottie_home, speed=1, reverse=True, loop=True, quality='medium', height=380, width=580, key=None)
    tab = option_menu(None, ["Overview 🗒️", "About Me 👨‍💻", "Future Enhancements 📈"], orientation="horizontal",icons=['journal','person-workspace','journal-code'])
    if tab == "Overview 🗒️":
        col3,col4 = st.columns([4,2])
        with col3:     
            st.subheader("Overview: 🗒️")
            st.markdown("- **PNR Status Check:** Quickly verify your ticket status with PNR number.")
            st.markdown("- **Train Time Checking:** Check real-time train schedules and departure times.")
            st.markdown("- **Train Timing Prediction:** Predict train arrival and departure times.")
            st.markdown("- **Booking Services:** Easily book tickets, meals, and more.")
            st.markdown("- **User Account:** Manage bookings and preferences conveniently.")
            st.subheader("How to Use:")
            st.markdown("1. Navigate to the 'Home' section to explore about the page.")
            st.markdown("2. Go to 'PNR Status' to check the status of your ticket with PNR number.")
            st.markdown("3. Visit 'Train Time Checking' to view real-time schedules and departure times.")
            st.markdown("4. Go to 'Train Timing Prediction' to predict train arrival and departure times.")
        with col4:
            st_lottie(lottie_over, speed=1, reverse=True, loop=True, quality='medium', height=480, width=580, key=None)
    elif tab == "About Me 👨‍💻":
        col5,col6 = st.columns([3,3])
        with col5:
            st.subheader("About Me: 👨‍💻")
            st.write("Hi there 👋, I'm Sumit Kumar Singh, the creator of the IRCTC Dashboard.")
            st.write("👨‍💻 A passionate Full Stack and Python Developer from India.")
            st.write("⚡ Fun fact: I enjoy coding so much that sometimes I feel like I'm in my own world of algorithms!")
            st.write("🚀 Always exploring new technologies and building cool projects.")
            st.write("🎨 Love creating clean, efficient, and user-friendly designs.")
            st.write("Let's connect and collaborate on exciting projects! 🤝")
            expander = st.expander("Contact me 📱",expanded=False,icon=":material/contact_page:") 
            with expander:
                social_media_links = [
                "https://www.instagram.com/sumit_kumarsingh22?utm_source=qr&igsh=Manufacturing==",
                "https://github.com/RAJPUTRoCkStAr",
                "https://www.linkedin.com/in/sumit-singh-773921262/",
                "https://x.com/Sumit92293207",
                "https://www.kaggle.com/sumitkumarsingh22002",
                ]
                sizes = ['lg','lg','lg','lg','lg','lg']
                SocialMediaIcons(social_media_links=social_media_links,sizes=sizes).generate_icons()
                st.write("📫 Reach me: sumitsingh9441@gmail.com")
        with col6:
            st_lottie(lottie_me,speed=1,reverse=True,loop=True,quality='medium',height=None,width=None,key=None)
    elif tab == "Future Enhancements 📈":  
        st.subheader("Future Enhancements: 📈")
        st.write("- Real-time Train Status Updates: Implement real-time updates on train statuses, including delays, cancellations, and platform changes, to provide users with the most current information.")
        st.write("- Personalized Recommendations: Utilize machine learning algorithms to offer personalized recommendations for travel packages, local attractions, and dining options based on user preferences and past bookings.")
        st.write("- Integration with Mobile Platforms: Create a mobile app version of the dashboard for seamless access on smartphones and tablets, ensuring users can manage their travel plans on the go.")
        st.write("- Enhanced User Authentication: Implement secure user authentication methods such as biometric verification or two-factor authentication (2FA) to enhance account security and personalized experiences.")
        st.write("- Voice Assistant Integration: Integrate voice recognition technology to allow users to interact with the dashboard hands-free, providing information and booking services through natural language commands.")
        st.write("- Feedback and Rating System: Incorporate a feedback system where users can rate their travel experiences, provide suggestions, and share reviews, helping to improve service quality and user satisfaction.")
        st.write("- Social Media Integration: Allow users to share their travel plans, experiences, and reviews directly from the dashboard to social media platforms, enhancing user engagement and promoting the dashboard organically.")
    st.write("⭐Feel free to explore the app and stay tuned for future updates!")