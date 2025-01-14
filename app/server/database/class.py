
from bson.objectid import ObjectId

# Retrieve all classes present in the database
async def retrieve_classes():
    classes = []
    async for class in class_collection.find():
        classes.append(class_helper(class))
    return classes

# Retrieve a class wih a matchingID
async def retrieve_class(id: str) -> dict:
    class = await class_collection.find_one({"_id": ObjectId(id)})
    if class:
        return class_helper(class)
    
# Delete a class from the database
async def delete_class(id: str):
    class = await class_collection.find_one({"_id": ObjectId(id)})
    if class:
        await class_collection.delete_one({"_id": ObjectId(id)})
        return True
    
#Add a new class
async def add_class(class_data:dict)->dict:
    class=await class_collection.insert_one(class_data)
    new_class=await class_collection.find_one({"_id": class.inserted_id})
    return class_helper(class)

#Updation of class with matching ID
async def update_class(id:str,data:dict):
    #Return false if empty requestbody is sent
    if len(data)<1:
        return False
    class=await class_collection.find_one({"_id": ObjectId(id)})
    if class:
        update_class= await class_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if update_class:
            return True
        return False
