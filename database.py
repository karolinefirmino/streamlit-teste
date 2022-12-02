from deta import Deta

DETA_KEY = "e0cyncxi_8ryssVihrqjrhQNe2JbCuEy1zgEgrpZZ"

deta = Deta(DETA_KEY)

db = deta.Base("users_db")


def insert_user(username, name, password):
    """Returns the user on a successful user creation, otherwise raises an error"""
# This is how to create/connect a database 
    return db.put({"key": username, "name": name, "password": password})

def fetch_all_users():
    """Returns a dict of all users"""
    res = db.fetch()
    return res.items

print(fetch_all_users())