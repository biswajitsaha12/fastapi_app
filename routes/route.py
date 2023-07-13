from fastapi import APIRouter
from models.users import User
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

#Root
@router.get("/")
async def root():
    return {"Welcome to FastAPI app!"}

#GET request
@router.get("/users")
async def get_users():
    users = list_serial(collection_name.find())
    return users

#POST request
@router.post("/")
async def create_user(user: User):
    collection_name.insert_one(dict(user))

#PUT request
@router.put("/{id}")
async def update_user(id:str, user:User):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})

#Delete request
@router.delete("/{id}")
async def delete_user(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})







