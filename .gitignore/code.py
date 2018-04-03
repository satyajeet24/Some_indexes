#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
#print n
fn=data.getvalue('Fname')
g=data.getvalue('a')
e=data.getvalue('email')
p=data.getvalue('password')
con=MySQLdb.connect("127.0.0.1","root","","iiit",3306)
query="insert into register(name,fname,gender,email,password) values ('"+n+"','"+fn+"','"+g+"','"e"','"+p+"')"
print(query)
