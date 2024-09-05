import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service.router.service import RouterService

router = RouterService.get_router()
app = FastAPI(title="InvestLab")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]

app.include_router(
    router
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    port = 8000
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        access_log=True,
        root_path="/"
    )