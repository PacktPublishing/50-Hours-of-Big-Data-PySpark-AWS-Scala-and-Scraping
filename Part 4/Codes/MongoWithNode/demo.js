const {MongoClient} = require('mongodb');
async function main(){

    const uri = "mongodb+srv://ahmadO1024:test_123@cluster0.vgldm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
    const client = new MongoClient(uri);
    
    try{
        await client.connect();
        console.log("Try")
        // await listDatabases(client);
        // await insertDocument(client,{"one doc": 1, "one doc 2": 2 });
        // await insertDocuments(client,[{"multi doc": 1, "multi doc 2": 2 },{"multi doc": 3, "multi doc 2": 4 }]);
        // await readDocuments(client);
        // await updateDocuments(client, {"one doc" : {"$eq":1}})
        // await deleteDocuments(client, {"multi doc" : {"$gte":3}})

    }
    catch(e){
        console.error(e);
        console.log("error")

    }
    finally{
        await client.close();
        console.log("finally")

    }
}

async function listDatabases(client){
    databasesList = await client.db().admin().listDatabases();
    console.log("Databases: ");
    databasesList.databases.forEach(db => {
        console.log(` - ${db.name}`);    
    });
}

async function insertDocument(client, document){
    results = await client.db("NodeJsDB").collection("dummyCollection").insertOne(document);
    console.log("Insert One");
    console.log(results);
}
async function insertDocuments(client, documents){
    results = await client.db("NodeJsDB").collection("dummyCollection").insertMany(documents);
    console.log("Insert Many");
    console.log(results);
    console.log(results.insertedIds.for);

}

async function readDocuments(client){
    cursor = await client.db("NodeJsDB").collection("dummyCollection").find();
    // db.collectionName.find({})
    results = await cursor.toArray();
    console.log(results);
    
}


async function updateDocuments(client, conditions){
    results = await client.db("NodeJsDB").collection("dummyCollection").updateMany(conditions,{$inc: {"one doc": 5}});
    console.log(results);
}

async function deleteDocuments(client, conditions){
    results = await client.db("NodeJsDB").collection("dummyCollection").deleteMany(conditions);
    console.log(results);
}



main().catch(console.error);