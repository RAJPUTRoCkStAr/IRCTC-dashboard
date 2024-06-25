import json
import requests
from streamlit_lottie import st_lottie
def load_lottiefile(filepath:str):
    with open (filepath, 'r') as f:
        return json.load(f)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_birtcoachmay = load_lottiefile("lotti/birtcoachmay.json")
lottie_firstpage = load_lottiefile("lotti/firstpage.json")
lottie_firstpag = load_lottiefile("lotti/firstpag.json")
lottie_livetrain = load_lottiefile("lotti/livetrain.json")
lottie_PNR = load_lottiefile("lotti/PNR.json")
lottie_seatavail = load_lottiefile("lotti/seatavial.json")
lottie_timetable = load_lottiefile("lotti/timetable.json")
lottie_Trainbwstation = load_lottiefile("lotti/Trainbwstation.json")
lottie_trainclasses = load_lottiefile("lotti/trainclasses.json")
lottie_me = load_lottiefile("lotti/Me.json")