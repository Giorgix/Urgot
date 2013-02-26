# Urgot email client
import sys, shelve, getpass, string, os, email
import smtplib, poplib
import re
from email import parser

#import gaierror for bad host exception(socket)
from socket import gaierror 

class Connection(object):
	
    def connection_pop3(self, host, user, password):
        
        
	try:
	    #Create a POP3_SSL object
	    pop_conn = poplib.POP3_SSL(host)

	    #Try to connect with an user and password 
	    pop_conn.user(user)
	    pop_conn.pass_(password)

	#Catch the exception for a bad host
        except gaierror as e:
	    return e.message

        #Catch the exception for bad user adn password
	except poplib.error_proto as e:
	    return e.message

        
	finally:
	   pass	
           # pop_conn.quit()
        
	#Return a POP_SSL object in order to access to it properties
        return pop_conn

    def close_connection_pop3(self, connection):

        connection.quit()
'''
class Login(object):

    def ask(self, question):
        print "\r%s" %question,
	return sys.stdin.readline().strip()
    

    def get_user(self):

        user = self.ask('Your email address: ')

	if self.check_mail_addr_pop(user):
	    return user

        else:
	    print 'Invalid email, try again:'
	    return self.get_user()

    def get_password(self):
        
	password = getpass.getpass('enter you password for %s: '%user)
	return password
    
    
    
    def check_mail_addr_pop(self, addr):
	
	alfa_num = re.compile('([A-Z]*[a-z]*[0-9]*)+@([A-Z]*[a-z]*[0-9]*)+.([A-Z]*[a-z]*[0-9]*)')
	return alfa_num.search(addr)
'''

class MailActions(object):
    
    #Read the messages of the connection object
    def list_mail(self, connection):
        msgs_list = [connection.retr(i) for i in range(1,len(connection.list()[1])+1)  ]
	msgs_list =['\n'.join(m[1]) for m in msgs_list]
	msgs_list = [parser.Parser().parsestr(m) for m in msgs_list]
	return msgs_list
    
    #Print the total number of mails, the  mail number and the subject
    def print_mail_list(self, messages):
	
       	print 'Inbox: %s' % len(messages)
	i=0
	while i<len(messages): 
	    print '['+str(i+1)+'] ',messages[i]['subject']
	    i=i+1
    
    #Print the subject, from, date and the body content
    def read_mail(self, messages):
	
	index=int(ask("please specify the mail number: "))
	if 0<index<=len(messages):
            print '#'*64
	    print 'SUBJECT:',messages[index-1]['Subject']
	    print 'FROM:',messages[index-1]['From']
	    print 'DATE:',messages[index-1]['Date']
	    print '-'*24+'message below'+'-'*26+'\n'
	    print self.extract_body_message(messages[index-1])
	    print '#'*64

    #Read the body content of the message
    def extract_body_message(self, message):
	
	for part in message.walk():
	    if part.get_content_type()=='text/plain':
	        return part.get_payload()


def ask(question):
    print "\r%s" %question,
    return sys.stdin.readline().strip()


if __name__=='__main__':
   connection = Connection()
   mail_actions = MailActions()
   conn_pop3 = connection.connection_pop3('pop.gmail.com', 'pruebas@madtec.es', 'prueba1ab2')
   messages = mail_actions.list_mail(conn_pop3)
   #print messages
   mail_actions.print_mail_list(messages)
   #print mail_actions.extract_body_message(messages[0])
   mail_actions.read_mail(messages)
