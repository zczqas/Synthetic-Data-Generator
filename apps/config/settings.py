import os


from starlette.config import Config
from starlette.datastructures import (
    Secret,
    CommaSeparatedStrings,
)

env = os.environ.get("APP_ENV", "DEV")

if env == "PROD":
    config = Config(".env.prod")
elif env == "DEV":
    config = Config(".env")
else:
    config = Config(".env")

VERSION: str = config("VERSION", default="1.0.0")
DEBUG: bool = config("DEBUG", cast=bool, default=False)
APP_ENV: str = config("APP_ENV", default="Quiktok DEV")
PROJECT_NAME: str = config("PROJECT_NAME", default="QUIKTOK")
DESCRIPTION: str = config("DESCRIPTION", default="QUIKTOK")
APP_SECRET_KEY: str = config(
    "APP_SECRET_KEY",
    default="UBzPj7Qj29K4z4aeCqZ40xi8dVdTbbch",
    cast=Secret,
)


ADMIN_USERNAME: str = config("ADMIN_USERNAME", default="admin@admin.com")
ADMIN_PASSWORD: str = config("ADMIN_PASSWORD", default="admin@123")
ALLOWED_HOSTS: list[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)


DATABASE_HOST: str = config("DATABASE_HOST", default="localhost")
DATABASE_PORT: str = config("DATABASE_PORT")
DATABASE_NAME: str = config("DATABASE_NAME", default="")
DATABASE_USER: str = config("DATABASE_USER")
DATABASE_PASSWORD: str = config("DATABASE_PASSWORD")
SQLALCHEMY_DATABASE_URL: str = config(
    "SQLALCHEMY_DATABASE_URL", default="sqlite:///./test.db"
)
ASYNC_SQLALCHEMY_DATABASE_URL: str = config(
    "ASYNC_SQLALCHEMY_DATABASE_URL", default="sqlite:///./test.db"
)

SECRET_KEY: Secret = config("SECRET_KEY", default="secret")
ALGORITHM: str = config("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", default=300)
ACCESS_TOKEN_IN_MINUTES: int = config("ACCESS_TOKEN_IN_MINUTES", default=60)
REFRESH_TOKEN_TIME_IN_MINUTES: int = config(
    "REFRESH_TOKEN_TIME_IN_MINUTES", cast=int, default=3600
)
TOKEN_URL: str = config("TOKEN_URL", default="token")

EMAIL_USE_TLS: str = config("EMAIL_USE_TLS", default="")
EMAIL_HOST: str = config("EMAIL_HOST", default="")
EMAIL_PORT: int = int(config("EMAIL_PORT", default=587))
EMAIL_HOST_USER: str = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD: str = config("EMAIL_HOST_PASSWORD", default="")

MEDIA_PATH: str = config("MEDIA", default="media")
SERVER_URL: str = config("SERVER_URL", default="http://localhost:8000")

OTP_LENGTH: int = config("OTP_LENGTH", cast=int, default=4)
API_KEY: str = config("ANTHROPIC_API_KEY", default="")
