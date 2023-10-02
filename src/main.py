import uvicorn
from settings import Settings
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app=app, host=Settings.HOST, port=Settings.PORT)
