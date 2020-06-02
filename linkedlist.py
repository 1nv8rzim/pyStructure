class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest

    def __str__(self):
        return f'Node({self.value},{self.rest})'

    def __repr__(self):
        return str(self)
