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



if __name__=='__main__':
   connection = Connection()
   connection.connection_pop3('user', 'password')

