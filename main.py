from fastapi import FastAPI
from typing import Optional, Union
from pydantic import BaseModel
# uvicorn main:app --reload
app = FastAPI(title="sw360")

# http://127.0.0.1:8000/


class MillionThing(BaseModel):
    name: str
    age: int
    desc: Optional[str] = None


class MillionThingIn(MillionThing):
    secret: str


@app.post('/mt/', response_model=MillionThing, response_model_exclude_unset=True)
async def get_item(millionthing: MillionThingIn):
    return millionthing


# @app.post('/mt/')
# async def get_item(millionthing: MillionThing):
#     return millionthing


@app.post('/mt/{prior}')
async def get_item(prior: int, millionthing: MillionThing):
    return {"prior": prior, **millionthing.dict()}


@app.get('/')
async def hw():
    return {"hello": "world"}

# http://127.0.0.1:8000/item/1000


@app.get('/item/{item_id}')
async def get_itemId(item_id):
    return {"item_id": item_id}


# http://127.0.0.1:8000/item/?num=100&text=Ten


@app.get('/item/')
async def get_item(num: int, text: Optional[str]):
    return {"num": num, "text": text}
