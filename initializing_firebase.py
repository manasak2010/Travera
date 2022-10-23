#INITIALIZING FIREBASE
config = {
  "apiKey": "AIzaSyDFwKxLVYhkgJYIN7EsqO5I8_xPJW0DjAI",
  "authDomain": "iiithackathon.firebaseapp.com",
  "projectId": "iiithackathon",
  "storageBucket": "iiithackathon.appspot.com",
  "messagingSenderId": "343429217783",
  "appId": "1:343429217783:web:5a5e8e9bb2ed1ceef142f2",
  "measurementId": "G-Z5JQ8REZEE",
  "databaseURL":"https://iiithackathon.firebase.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
