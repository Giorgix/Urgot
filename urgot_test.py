import unittest
from urgot import Connection

class connection_pop3Test(unittest.TestCase):
    
    def setUp(self):
        self.connection = Connection()
    def test_connection_pop3(self):

	self.assertTrue(self.connection.connection_pop3('jorge.delgado@madtec.es', 'DaVinci5260'))
	self.assertRaises(Exception, self.connection.connection_pop3, 'jorge.delgado@madtec.es', 'abc1234')
	

if __name__ == '__main__':
    unittest.main()
