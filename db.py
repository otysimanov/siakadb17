import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase


cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

firebaseConfig = {
    "apiKey": "AIzaSyDUFgEiCD0nbrjSF81ujDpnRg4I4yxMusE",
    "authDomain": "siakadb17.firebaseapp.com",
    "databaseURL": "https://siakadb17-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "siakadb17",
    "storageBucket": "siakadb17.appspot.com",
    "messagingSenderId": "412369454232",
    "appId": "1:412369454232:web:af17f8dac89a0dd9667ced"
}
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

def get_all_collection(collection, orderBy=None, direction=None):
    if orderBy:
        collects_ref = db.collection(collection).order_by(
            orderBy, direction=direction)
    else:
        collects_ref = db.collection(collection)
    collects = collects_ref.stream()
    RETURN = []
    for collect in collects:
        ret = collect.to_dict()
        ret['id'] = collect.id
        RETURN.append(ret)
    return RETURN