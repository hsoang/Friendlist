import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from flask import Flask
from views import views


cred = credentials.Certificate("C:/Users/hoang/OneDrive/Documents/GitHub/Friendlist/credentials.json")
firebase_db = firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/")


def showCalendar():
    # cur_datetime = datetime.datetime.now()
    # year = cur_datetime.year
    # print(calendar.calendar(year))
    print("FIX")
    

def addEvent():
    print("FIX")




if __name__ == "__main__":
    # data = {"name": "Los Angeles", "state": "CA", "country": "USA"}
    # db.collection("cities").document("LA").set(data)
    app.run(debug = True, port = 8000)
