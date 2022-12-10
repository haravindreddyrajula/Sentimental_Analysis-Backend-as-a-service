import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Analysis(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    text: str = Field(...)
    probability: str = Field(...)
    prediction: str = Field(...)
    created_on: datetime = Field(...)
    updated_on: datetime = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "...",
                " created_on": 2022
            }
        }


class AnalysisUpdate(BaseModel):
    text: Optional[str]
    probability: Optional[str]
    prediction: Optional[str]
    updated_on: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "text": "Don Quixote",
                "probability": "Miguel de Cervantes",
                "prediction": "Don Quixote is a Spanish novel by Miguel de Cervantes...",
                "updated_on": 2020
            }
        }
