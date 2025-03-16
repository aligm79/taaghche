from django.core.cache import caches

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
        
class CacheCenter:
    def __init__(self):
        self.head = None 

    def append(self, node):
        if not self.head: 
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
    
    def append_after_node(self, target, node):
        current = self.head
        while current and current.name != target:
            current = current.next

        if current:
            node.next = current.next
            current.next = node

    def search(self, id):
        current = self.head
        while current:
            book = caches[current.name].get(id)
            if book:  
                return book , current.name
            current = current.next  
        return None, None  
    
    def cache(self, item, id, ending_layer):
        current = self.head
        while current and current.name != ending_layer:
            caches[current.name].set(id, item)
            current = current.next

    def delete_from_cache(self, id):
        current = self.head
        while current:
            caches[current.name].delete(id)
            current = current.next


cached_layers = CacheCenter()
cached_layers.append(Node("memory"))
cached_layers.append(Node("default"))

