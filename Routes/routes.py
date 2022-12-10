from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from MongoModels.analysis import Analysis, AnalysisUpdate
from KafkaService.kafka_client import connect_kafka_producer
from stream.twitter_streams import get_stream

router = APIRouter()


# from flask import Flask
# app = Flask(__name__)

@router.get("/", response_description="List all Analysis", response_model=List[Analysis])
def list_analysis(request: Request):
    analysis = list(request.app.database["analysis"].find(limit=100))
    return analysis


@router.post("/", response_description="Create a new analysis", status_code=status.HTTP_201_CREATED,
             response_model=Analysis)
def create_analysis(request: Request, analysis: Analysis = Body(...)):
    kafka_producer = connect_kafka_producer()
    get_stream(kafka_producer)
    analysis = jsonable_encoder(analysis)
    new_analysis = request.app.database["analysis"].insert_one(analysis)
    created_analysis = request.app.database["analysis"].find_one(
        {"_id": new_analysis.inserted_id}
    )

    return created_analysis

# @app.route('/')
# def hello_world():
#     kafka_producer = connect_kafka_producer()
#     get_stream(kafka_producer)
#     return 'Hello World'


# if __name__ == '__main__':
#     app.run()
