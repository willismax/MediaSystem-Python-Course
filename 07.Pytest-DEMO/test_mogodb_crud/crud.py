from pymongo.mongo_client import MongoClient

database_name = "test"
collection_name = "user"


def insert_user(conn: MongoClient, data: dict) -> dict:
    # 插入資料並取得 id
    insert_id = conn[database_name][collection_name].insert_one(data).inserted_id

    # 藉由 id 搜尋並回傳
    result = conn[database_name][collection_name].find_one({"_id": insert_id})
    return result