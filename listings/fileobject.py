from os.path import join

class FileObject:
    '''Wrapper for file objects to make sure the file gets closed 
    on deletion.'''
    
    def __init__(self, filepath='~', filename='sample.txt'):
        # open a file filename in filepath in read and write mode
        self.file = open(join(filepath, filename), 'r+')
   
    def __del__(self):
        self.file.close()
        del self.file
