import unittest
from urgot import Connection,MailActions
from poplib import error_proto

class ConnectionPop3Test(unittest.TestCase):
    
    def setUp(self):
        self.connection = Connection()
    
    #def test_connection_pop3_invalid_host(self):
	#self.assertEqual(self.connection.connection_pop3('kakas.e', 'mendrugo@kk.es', 'DaVinci5260'), '[Errno -2] Name or service not known')

    
    def test_connection_pop3_invalid_username(self):
		
	self.assertEqual(self.connection.connection_pop3('pop.gmail.com', 'mendrugo@kk.es', 'prueba1ab2'), '-ERR [AUTH] Username and password not accepted.')
    
    def test_connection_pop3_invalid_password(self):
	
	self.assertEqual(self.connection.connection_pop3('pop.gmail.com', 'pruebas@madtec.es', 'password'), '-ERR [AUTH] Username and password not accepted.')

    def test_connection_pop3_valid_data(self):

        self.assertTrue(self.connection.connection_pop3('pop.gmail.com', 'pruebas@madtec.es', 'prueba1ab2'))

class MailActionsTest(unittest.TestCase):

    def setUp(self):
	self.connection = Connection()    
	self.mail_actions = MailActions()

    def test_empty_mail_list(self):

	self.assertTrue(self.mail_actions.list_mail(self.connection.connection_pop3('pop.gmail.com', 'pruebas@madtec.es', 'prueba1ab2')))
