from bson.objectid import ObjectId
# Retrieve all class present in the database
async def retrieve_classes():
    classes = []
    async for lot in class_collection.find():
        classes.append(class_helper(lot))
    return classes
# Retrieve a class with a matching ID
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