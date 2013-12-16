class Feet(object):
    '''Descriptor for foot-based access of a meter value.'''

    def __get__(self, instance, owner):
        return instance.meters * 3.2808
    def __set__(self, instance, value):
        instance.meters = float(value) / 3.2808

class Distance(object):
    '''Class to represent distance holding two descriptors for feet and
    meters.'''

    def __init__(self, meters):
        self.meters = meters
    feet = Feet()

