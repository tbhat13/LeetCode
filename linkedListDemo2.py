class linkedList:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode


class linkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        node = linkedList(value)
        if self.head is None:
            self.head = node
            return 
        
        currentNode = self.head    
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode