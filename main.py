import configparser
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from Routes.routes import router as analysis_router

config = dotenv_values(".env")
app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Welcome!"}

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGO_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("success")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(analysis_router, tags=["analysis"], prefix="/twitter")


def config_reader():
    cfg = configparser.RawConfigParser()
    cfg.read('./ConfigFiles/all_config.cfg')
    bearer_token = cfg.get('TWITTER', 'bearer_token')
    print(bearer_token)
    return bearer_token


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    bearer_token = config_reader()
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r
