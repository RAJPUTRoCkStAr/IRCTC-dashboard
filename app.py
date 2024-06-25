import streamlit as st
from streamlit_lottie import st_lottie
from lott import lottie_me,lottie_firstpage
st.header("this is a good one")
lottie_firstpage = st_lottie(lottie_firstpage, speed=1, reverse=True, loop=True, quality='medium', height=180, width=180, key=None)