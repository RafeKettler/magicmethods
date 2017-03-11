class Closer:
    '''A context manager to automatically close an object with a
    close() method in a with statement.'''

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj # bound to target

    def __exit__(self, exception_type, exception_val, trace):
        try:
           self.obj.close()
        except AttributeError: # obj isn't closable
           print 'Not closable.'
           return True # exception handled successfully

if __name__ == '__main__':
    with Closer(3) as test:
       test.close()
    with Closer(open('test.txt', 'a')) as test:
        test.close()
    with Closer(2/1) as test:
        test.close()
