import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    HOST = os.environ.get("HOST", "localhost")
    PORT = int(os.environ.get("PORT", 8000))
    DATABASE = os.environ.get("DATABASE", None)
    DEV = os.environ.get("DEV", False)
