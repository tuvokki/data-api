import unittest
from pymongo import MongoClient

class TestMongoInsertFunctions(unittest.TestCase):

  def setUp(self):
    # Get a reference to the MongoDB
    self.client = MongoClient('mongodb://localhost:27017/')
    self.db = self.client['test']
    # self.collection = self.db['quotes']

  def testConn(self):
    for quote in self.db.quotes.find():
      # print quote
    # for quote in quotes:
    #   # print values
      for kk, vv in quote.iteritems():
        print kk, ': ', vv

suite = unittest.TestLoader().loadTestsFromTestCase(TestMongoInsertFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
