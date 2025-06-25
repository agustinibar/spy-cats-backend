from pydantic import BaseModel, validator
import requests

class SpyCatBase(BaseModel):
    name: str
    years_of_experience: int
    breed: str
    salary: float

    @validator("breed")
    def validate_breed(cls, value):
        res = requests.get("https://api.thecatapi.com/v1/breeds")
        breeds = [breed["name"].lower() for breed in res.json()]
        if value.lower() not in breeds:
            raise ValueError("Invalid cat breed")
        return value

class SpyCatCreate(SpyCatBase):
    pass

class SpyCatOut(SpyCatBase):
    id: int

    class Config:
        from_attributes = True

class SpyCatUpdate(BaseModel):
    salary: float
