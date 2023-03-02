from .linked_list import LinkedList


class FileManager:

    def load_to_linked_list(self, file_path):
        numbers = self.load_file_as_string(file_path)

        int_list = [int(x) for x in numbers.split("\n")]
        int_dict = dict(enumerate(int_list))
        return LinkedList(int_dict)
        
    
    def load_file_as_string(self, file_path):
        with open(file_path) as f:
            contents = f.read()
            f.close()
            return contents

    
    def save_reversed_to_file(self, linked_list: LinkedList, file_path: str):
        linked_list.reverse()

        with open(file_path, 'w') as f:
            current = linked_list.head
            while(current):
                f.write(f'{current.value}\n')
                current = linked_list.next()
            f.close()