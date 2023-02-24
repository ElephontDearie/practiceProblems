from linked_node import LinkedNode


class LinkedList:
    head = LinkedNode

    def __init__(self, int_map: dict):
        map_size = len(int_map)

        if (map_size == 0):
            raise IndexError("Must have a list with a size greater than 0")
        
        self.head = LinkedNode(int_map[0])
        current = self.head

        for index in range(0, map_size, 2):
            if (index < map_size - 2):
                next_pointer = LinkedNode(int_map[index + 2])
                current.pointer = LinkedNode(int_map[index + 1], next_pointer)
            elif (index < map_size - 1):
                current.pointer = LinkedNode(int_map[index + 1])

            current = next_pointer
            

    def reverse(self) -> 'LinkedList':
        previous_node = self.head
        current_node = previous_node.pointer
        previous_node.pointer = None

        while current_node:
            next_node = current_node.pointer
            current_node.pointer = previous_node
            
            if not next_node: 
                self.head = current_node
                break
            previous_node = current_node
            current_node = next_node
        

    def next(self):
        self.head = self.head.pointer
        return self.head





