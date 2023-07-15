from fastapi import FastAPI

from src.lib.managedb import ManageDb

app = FastAPI()
md = ManageDb()

@app.get("/")
def root():
    return{"hola"}

@app.get("/api/contacts")
def get_all_contacts():
    return md.read_contacts()

#@app.post("/")
#def post():
#    return ("post")

@app.get("/api/contacts/{id_contact}")
def get_single_contact(id_contact):
    contacts = md.read_contacts()

    for contact in contacts:
        if contact["id"] == id_contact:
         return contact