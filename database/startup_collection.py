from database.mongodb import startup_collection

def save_startup(data):

    result = startup_collection.insert_one(
        data
    )

    return str(result.inserted_id)


def get_startup(id):

    return startup_collection.find_one(
        {"_id": id}
    )