from pymongo import MongoClient

class AnimalShelterCRUD(object):
   

    def __init__(self, username, password, host, port, database, colelction):
        # Init MongDB connection
        USER = username
        PASS = password
        HOST = host
        PORT = port
        DB = database
        COL = colelction

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
      
        try:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def read(self, query):
        
        try:
            cursor = self.collection.find(query)
            return list(cursor)  # Convert cursor to list of documents
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
            
    def update(self, query, new_data):
   
        try:
            result = self.collection.update_many(query, {'$set': new_data})
            return result.modified_count
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
    
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
          
