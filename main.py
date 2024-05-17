import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from apps.config import settings

from apps.apis.v1.data.routes import router as data_router
from apps.apis.v1.csv.routes import router as csv_router


def get_application() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
    )

    if not os.path.exists(settings.MEDIA_PATH):
        os.makedirs(settings.MEDIA_PATH)

    media_directory = Path(settings.MEDIA_PATH)
    app.mount("/media", StaticFiles(directory=media_directory), name="media")

    origins = [
        "*",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = get_application()
app.include_router(data_router, prefix="/api/v1")
app.include_router(csv_router, prefix="/api/v1")


@app.get("/")
async def home():
    return {"status": f"{settings.APP_ENV} is running!"}
