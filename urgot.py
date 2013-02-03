# Urgot email client
import poplib
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

    
    def get_user():
        user = ask('Your email address: ')
	if check_mail_addr_pop(user):
	    return user
        else:
	    print 'Invalid email, try again:'
	    return get_user()
    
    
    
    def check_mail_addr_pop(addr):
	alfa_num = compile('([A-Z] * [a-z] * [0-9] *) + @ ([A-Z] * [a-z] * [0-9] *) + . ([A-	    Z] * [a-z] * [0-9] *)')
    	return alfa_num.search(addr)



if __name__=='__main__':
   connection = Connection()
   check_username = Check_username()
   user = check_username.get_user()
   connection.connection_pop3('user', 'password')

