class Entity:
    '''Class to represent an entity. Callable to update 
    the entity's position.'''

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''Change the position of the entity.'''
        self.x, self.y = x, y

    # snip...
