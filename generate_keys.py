import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Peter Parker", "Rebecca Miller", "Rodrigo Müller"]
usernames = ["pparker", "rmiller", "rmoboe"]
passwords = ["$2b$12$dzQQfa3XPmHbq034.Ix5UuB2WTM7uhA.EjbnHtw5xtIGlSOnHTkFa", "$2b$12$wOSkUvBFaEsKCK4vVTKRcenyi.Yhn.ftpdEL2YYco.N3wlMUuYIre", "$2b$12$oR91j88e3XVm.ztd2.7Te.yBQumB0TlhxpKJPfOmoc32w169RfNO."]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
