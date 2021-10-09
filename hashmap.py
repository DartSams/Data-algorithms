"""
Think of a hash map as a cabinet having drawers with labels for the things stored in them.
For example, storing user information- consider email as the key, and we can map values
corresponding to that user such as the first name, last name etc to a bucket. 
"""

class HashTable:
    def __init__(self,size):
        self.size=size
        self.hashtable=self.create_bucket()
        # print(self.hashtable)

    def create_bucket(self):
        return [[] for i in range(self.size)]

    def hash_key(self,key):
        hashed_key=hash(key) % self.size
        return hashed_key

    def set_value_to_key(self,key,value):
        hashed_key=self.hash_key(key)
        slot=self.hashtable[hashed_key]
        key_exist=False
        # print(hashed_key)
        for i,key_value in enumerate(slot):
            # print(i,key_value)
            k,v=key_value
            if key == k:
                key_exist=True
                break
        
        if key_exist:
            slot=((key,value))
        else:
            slot.append((key,value))

    def get_value(self,key):
        hashed_key=self.hash_key(key)
        slot=self.hashtable[hashed_key]
        for i,key_value in enumerate(slot):
            k,v = key_value
            if key == k:
                return hashed_key,k,v
            else:
                raise KeyError("Key does not exist")

        
h=HashTable(256)
h.set_value_to_key("item2","dirt")
h.set_value_to_key("item3","sand")
h.set_value_to_key("item4","air")

print(h.get_value("item2"))
print(h.get_value("item3"))
print(h.get_value("item4"))

print(h.hashtable)