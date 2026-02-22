from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, tasks

app = FastAPI(title="TaskFlow Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://localhost:3000",
        "https://taskflow-portfolio.vercel.app",
        "https://www.taskflow-portfolio.vercel.app",
        "https://taskflow-portfolio-git-main-khadr-projects.vercel.app",
        "https://taskflow-portfolio-fw6d7m7qk-khadr-projects.vercel.app",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "TaskFlow Backend is running"}