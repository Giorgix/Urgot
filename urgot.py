# Urgot email client
import sys, shelve, getpass, string, os, email
import smtplib, poplib
import re
from email import parser

class Connection(object):
	
    def connection_pop3(self, user, password):
        print 'Connecting...'
	host = 'pop.gmail.com'
        pop_conn = poplib.POP3_SSL(host)
        pop_conn.user(user)
	try:
	    pop_conn.pass_(password)

	except Exception as e:
	    raise e

	finally:
	    pop_conn.quit()

        print pop_conn.getwelcome()
        return pop_conn

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


class MailActions(object):

    def list_mail(self, connection):
        msgs_list = [connection.retr(i) for i in range(1,len(connection.list()[1])+1)  ]
	msgs_list =['\n'.join(m[1]) for m in msgs_list]
	msgs_list = [parser.Parser().parsestr(m) for m in msgs_list]
	return msgs_list

    def print_mail_list(self, messages):
        print 'Inbox: %s' % len(messages)
	i=0
	while i<len(messages): 
	    print '['+str(i+1)+'] ',messages[i]['subject']
	    i=i+1
	


if __name__=='__main__':
   connection = Connection()
   login = Login()
   mail_actions = MailActions()
   user = login.get_user()
   password = login.get_password()
   pop3_conn = connection.connection_pop3(user, password)
   messages = mail_actions.list_mail(pop3_conn)
   mail_actions.print_mail_list(messages)
