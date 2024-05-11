from pymongo import MongoClientdef create_distributed_database(hosts):
    # Create a distributed database using Apache Cassandra or MongoDB

    client = MongoClient(f'mongodb://{hosts[0]}:27017')
    db = client['distributed_database']
    db.command('replSetInitiate', {'_id': 'distributed_database', 'members': [{'_id': 0, 'host': hosts[0], 'priority': 7}, {'_id': 1, 'host': hosts[1], 'priority': 3}]})

    return db

def insert_data(db, collection_name, data):
    # Insert data into a distributed database

    collection = db[collection_name]
    collection.insert_one(data)

def query_data(db, collection_name, query):
    # Query data from a distributed database

    collection = db[collection_name]
    result = collection.find(query)

    return result
