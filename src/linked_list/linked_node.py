class LinkedNode:
    value: int
    pointer: 'LinkedNode'

    def __init__(self, value, pointer = None):
        self.value = int(value)
        if type(pointer) == LinkedNode or pointer == None: 
            self.pointer = pointer

        else: raise TypeError("Must provide LinkedNode or None as pointer")