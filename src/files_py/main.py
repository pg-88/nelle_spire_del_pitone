import uvicorn
from fastapi import FastAPI

app = FastAPI()
HELLO = {
    "first": "hello ",
    "second": "world!"
}

@app.get("/")
def say_hello():
    '''just a quick hello to the world!'''
    return({HELLO["first"] + HELLO["second"]})

@app.get("/insert_name/{name_str}")
def insert_name(name_str):
    HELLO[name_str] = name_str
    return HELLO

    



if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
