import pymongo

def createMany(client, documents):
    db = client["PythonDB"]
    col = db["dummyCollection"]
    results = col.insert_many(documents)
    print(results.inserted_ids)

def readDocs(client, condition):
    db = client["PythonDB"]
    col = db["dummyCollection"]
    results = col.find(condition)
    # db.collectio.find({})

    for row in results:
        print(row)


def updateDocs(client, condition, operation):
    db = client["PythonDB"]
    col = db["dummyCollection"]
    results = col.update_many(condition, operation)
    print(results.modified_count)

def deleteDoc(client, condition):
    db = client["PythonDB"]
    col = db["dummyCollection"]
    results = col.delete_many(condition)

    print(results.deleted_count)


if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb+srv://ahmadO1024:test_123@cluster0.vgldm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # documents = [{"doc1": 1, "doc1-2":2},{"doc2": 1, "doc2-2":2}]
    # createMany(client,documents)
    # readDocs(client,{"doc1-2": {"$eq": 2}})
    # updateDocs(client,{"doc1-2": {"$eq": 3}}, {"$set": {"doc1-2":"Apple"}})
    deleteDoc(client,{"doc1-2": {"$eq": "Apple"}})

