class search_node:
    def __init__(self, G, Parent):
        self.location = 0, 0
        self.state = []
        self.h = int()
        self.g = G
        self.f = int()
        self.status = ''
        self.parent = Parent
        self.children = []