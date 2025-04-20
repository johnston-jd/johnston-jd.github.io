from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, USER, PASS):
        # Initializing the MongoClient.
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'JandO1427'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32278
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@localhost:32278/?authMechanism=DEFAULT&authSource=AAC' % ('aacuser', 'JandO1427'))
        self.database = self.client['AAC']
        self.collection = self.database['animals']
        
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
                self.database.animals.insert_one(data)  # data should be dictionary 
                return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
            
            
# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data)
        else:
            raise Exception('Nothing to read, because parameter is empty')
            return False
        
#Create method to implement the U in CRUD.
    def update(self, search, update_data):
        if search is not None:
            result = self.database.animals.update_one(search, update_data)
            if result.updated_count > 0:
                return True
            else:
                raise Exception('Nothing to update, because parameter is empty')
                return False
            
#Create method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_one(data)
            if result.deleted_count > 0:
                return True
            else:
                raise Exception('Nothing to delete, because data parameter is empty')
                return False