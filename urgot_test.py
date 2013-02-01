import unittest
from urgot import Connection

class connection_pop3Test(unittest.TestCase):
    
    def setUp(self):
        self.connection = Connection()
    def test_connection_pop3(self):

	self.assertTrue(self.connection.connection_pop3('user', 'password'))
	

if __name__ == '__main__':
    unittest.main()
