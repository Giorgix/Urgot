# Urgot email client
import sys, shelve, getpass, string, os, email
import smtplib, poplib
import re
class Connection(object):
	
    def connection_pop3(self, user, password):
        print 'Connecting...'
	host = 'pop.gmail.com'
        pop_conn=poplib.POP3_SSL(host)
        pop_conn.user(user)
        pop_conn.pass_(password)
        print pop_conn.getwelcome()
        return pop_conn

class Check_username(object):

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



if __name__=='__main__':
   connection = Connection()
   check_username = Check_username()
   user = check_username.get_user()
   password = check_username.get_password()
   connection.connection_pop3(user, password)

