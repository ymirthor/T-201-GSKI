class ItemExistsException(Exception): pass
class NotFoundException(Exception): pass

class MutableMapping:
    """ 
    This is an ABC class for hashmap classes.
    Children classes must include following functions:
        __setitem__
        __getitem__
        __delitem__
    and initialize with class variable named:
        length
    """
    
    def insert(self, key, data):
        try:
            self[key]
            raise ItemExistsException()
        except NotFoundException:
            self[key] = data

    def update(self, key, data):
        self[key]
        self[key] = data

    def find(self, key):
        return self[key]

    def contains(self, k):
        try:
            self[k]
            return True
        except NotFoundException:
            return False
    
    def remove(self, key):
        del self[key]

    def __len__(self):
        return self.length