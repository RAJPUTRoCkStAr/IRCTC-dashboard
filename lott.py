import json
import requests
from streamlit_lottie import st_lottie
def load_lottiefile(filepath:str):
    with open (filepath, 'r',encoding='utf-8') as f:
        return json.load(f)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_timetable = load_lottiefile("lotti/timetable.json")
lottie_firstpag = load_lottiefile("lotti/firstpag.json")
lottie_livetrain = load_lottiefile("lotti/livetrain.json")
lottie_PNR = load_lottiefile("lotti/pnr.json")
lottie_seatavail = load_lottiefile("lotti/seatavial.json")
lottie_home = load_lottiefile("lotti/home.json")
lottie_Trainbwstation = load_lottiefile("lotti/Trainbwstation.json")
lottie_trainclasses = load_lottiefile("lotti/trainclasses.json")
lottie_me = load_lottiefile("lotti/me.json")
lottie_over = load_lottiefile("lotti/overview.json")
lottie_fare = load_lottiefile("lotti/faredetails.json")
lottie_histo = load_lottiefile("lotti/trainhistor.json")
lottie_impstt = load_lottiefile("lotti/impstt.json")
lottie_searchstt = load_lottiefile("lotti/search.json")
