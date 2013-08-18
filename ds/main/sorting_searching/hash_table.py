
class HashMap(object):
    def __init__(self):
        self.size = 17
        self.slots = [None] * self.size
        self.data  = [None] * self.size

    def __repr__(self):
        return ',\n'.join(['{0}: {1}'.format(k, v) for k, v in zip(self.slots, self.data)])


    def put(self, key, item):
        '''
        - compute hash of key to get slot
        - while slot is occupied, get slot using rehash value
        - resize() has not been implemented yet
        '''
        if key is None: raise Exception('key cannot be --> {0}'.format(key))

        slot = self.hash_function(key)

        while self.slots[slot] is not None and self.slots[slot] != key:
            slot = self.rehash(slot)

        # we get to this step in three cases:
        # 1. The initial slot had None (the loop didn't run even once)
        # 2. We found a slot with None value
        # 3. We found a slot with the key value (overwrite the prev value)
        self.slots[slot] = key
        self.data[slot]  = item


    def get(self, key, default_val=None):
        '''
        - compute hash of the key to get slot
        - if slot has the key, return the data of that slot
        - while key is not found, get next slot using rehash function
        - return key if found, else default_val
        '''
        if key is None: raise Exception('key cannot be --> {0}'.format(key))

        slot = self.hash_function(key)
        if self.slots[slot] == key:
            # found the key in the proper hashed slot. yay!
            return self.data[slot]

        else:
            # there must have been a collision with this key,
            # probing for key using the rehashing scheme
            initial_slot = slot
            slot = self.rehash(slot)

            while self.slots[slot] != key and slot != initial_slot:
                slot = self.rehash(slot)

            if slot == initial_slot:
                return default_val
            else:
                return self.data[slot]


    def hash_function(self, key):
        return key % self.size


    def rehash(self, old_hash_value):
        '''
        which strategy are we using?
        '''
        return self._linear_probing(old_hash_value)


    def length(self):
        return len([x for x in self.slots if x])


    def delete(self, key):
        pass


    def _linear_probing(self, old_hash_value):
        return (old_hash_value + 1) % self.size


    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
