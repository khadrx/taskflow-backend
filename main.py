from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, tasks

app = FastAPI(title="TaskFlow Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://taskflow-portfolio.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "TaskFlow Backend is running"}