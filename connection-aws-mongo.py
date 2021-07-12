# this is considereing you have all the credencials explicit in the code 
# and that your db is publicly available, with is shouldn't

MONGO_DATABASE_NAME = 'db-name'

MONGO_LOCAL_HOST = "http://some-mongo-host"

class MongoDBConnection:
    _conn = None
    def __init__(self):
        mongo_credentials = {}
        if is_pytest():
            from pymongo_inmemory import MongoClient as MongoClientIM
            self.client = MongoClientIM()

        else:
            self.client = MongoClient(host=MONGO_LOCAL_HOST, password=MONGO_LOCAL_PASSWORD, username=MONGO_LOCAL_USERNAME)

        self.db = self.client[MONGO_DATABASE_NAME]

    @classmethod
    def conn(cls):
        # this is a singleton so onlyonece the connnections is called
        if cls._conn is None:
            cls._conn = cls()
        return cls._conn
