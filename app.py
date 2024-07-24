import streamlit as st
from streamlit_option_menu import option_menu
import Home,Traint,Pnrst,Faredetai,Trainh,Trains,Importan,Alltrain,Seatavai,TTrain

st.set_page_config(
                page_title="Irctc-Dashboard",
                page_icon="🚆",
                layout="wide")
class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })
    def run():
        with st.sidebar:      
                app = option_menu(
                        menu_title="Main Menu",
                        options=[
                                'Home',
                                'Train Time Table',
                                'Train Between Station',
                                'PNR Status',
                                'Fair Details',
                                'Seat Availablity',
                                'Train Running Status',
                                'Train Running History',
                                'IMPORTANT STATIONS & TRAINS',
                                'Station Information',
                                ],
                                icons=['house-fill', 
                                       'train-front-fill',
                                       'train-front-fill',
                                       'ticket-detailed',
                                       'currency-rupee',
                                       'person-vcard',
                                       'clock',
                                       'hourglass',
                                       'star',
                                       'card-text'],
                                menu_icon="cast"
                        ) 
        if app == "Home":
            Home.home()
        if app == "Train Time Table":
          Traint.traint()
        if app == "PNR Status":
          Pnrst.pnrst()  
        if app == "Fair Details":
          Faredetai.faredetail()
        if app == "Train Running History":
          Trainh.trainhist()
        if app == "Train Running Status":
          Trains.train_st()   
        if app == "IMPORTANT STATIONS & TRAINS":
          Importan.imp()
        if app == "Station Information":
          Alltrain.station_inf()
        if app == 'Seat Availablity':
          Seatavai.seatav()
        if app == 'Train Between Station':
          TTrain.ttraint()
    run()   
