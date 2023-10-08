import uvicorn
import settings
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app=app, host=settings.HOST, port=settings.PORT)
