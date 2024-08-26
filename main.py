from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3]

@app.get("/contacts")
def get_contacts():
    return {"name":"Leonel"}



    