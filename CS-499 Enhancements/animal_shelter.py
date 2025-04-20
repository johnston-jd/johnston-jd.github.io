#To be updated with new database information
from bson.objectid import ObjectId
import mysql.connector as mariadb

#Enhancement 2 - Creating HashMap
#Enhancement 3 - Database
class animalshelter(object):
# To be updated with new database
    def __init__(self, user, password, capacity):
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        # Initializing mariadb
        # Connection Variables
        #
        self.connection = mariadb.connect (user = 'root', password = 'L3w!sZ03Sally', host = '127.0.0.1',
                                              port = '49670', database = 'animalshelter')

        # Initialize Connection
        self.cursor = self.connection.cursor()
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True

        return False
    #inserts key, value into hashmap
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size += 1
    #returns value of mapped key
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError('Key not found')
    #removes key and value
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError('Key not found')
    #keys
    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]
    #values
    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]
    #items
    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity

        return hash_result


if __name__ == '__main__':
    import uuid
    import matplotlib.pyplot as plt

    #Will update with new database
    hash_map = animalshelter(user = 'root', password = 'L3w!sZ03Sally', capacity = 10000)

    for _ in range(10000):
        hash_map.put(uuid.uuid4(), 'some value')

    X = []
    Y = []

    for i, bucket in enumerate(hash_map.buckets):
        X.append(i)
        Y.append(i)
    #returns bar chart
    plt.bar(X,Y)
    plt.show()
else:
    pass
