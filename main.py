from fastapi import FastAPI
from routers import register

app = FastAPI()

app.include_router(register.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)