import scipy.sparse as sp
import numpy as np
import pickle

class Dataset(object):
    '''
    classdocs
    '''

    def __init__(self, path):
        '''
        Constructor
        '''
        self.trainMatrix = self.read_data(path, 'trainMatrix.pkl')
        self.testRatings = self.read_data(path , 'testRatings.pkl')
        self.testNegatives = self.read_data(path , 'testNegative.pkl')
        assert len(self.testRatings) == len(self.testNegatives)

           
    def read_data(self, path, file_name):
        with open(path + file_name, 'rb') as f:
            self.a = pickle.load(f)
            
        return self.a

        #assert len(self.testRatings) == len(self.testNegatives)
        
        #self.num_users, self.num_items = self.trainMatrix.shape