import mysql.connector
import numpy as sp

hostname = "localhost"
dbName = "test"
userName = "pma"

conn = mysql.connector.connect(user=userName, host=hostname, database=dbName)
cur=conn.cursor()

sql = 'select * from dwm_test;'
sqlx = 'select x from dwm_test;'
sqly = 'select y from dwm_test;'
sqlz = 'select z from dwm_test;'
sqlR = 'select R from dwm_test;'


cur.execute(sqlx)
recordsx = cur.fetchall()
## for record in recordsx:
  ## print(record[0])

cur.execute(sqlR)
recordsR = cur.fetchall()
## for record in recordsR:
##   print(record[0])

print(recordsR[0][0])
print(recordsR[1][0])




cur.close
conn.close


#x1 = input('x1:')
#x1 = int(x1)
#y1 = input('y1:')
#y1 = int(y1)
#z1 = input('z1:')
#z1 = int(z1)
#x2 = input('x2:')
#x2 = int(x2)
#y2 = input('y2:')
#y2 = int(y2)
#z2 = input('z2:')
#z2 = int(z2)
#x3 = input('x3:')
#x3 = int(x3)
#y3 = input('y3:')
#y3 = int(y3)
#z3 = input('z3:')
#z3 = int(z3)
x1 = 0
y1 = 6000
z1 = 2250

x2 = 6400
y2 = 0
z2 = 2250

x3 = 0
y3 = 0
z3 = 2250

r1 = input('r1:')
r1 = float(r1)
r2 = input('r2:')
r2 = float(r2)
r3 = input('r3:')
r3 = float(r3)


x21 = x2 - x1
y21 = y2 - y1
z21 = z2 - z1

x31 = x3 - x1
y31 = y3 - y1
z31 = z3 - z1

##A1 = r1^2 - x1^2 - y1^2 - z1^2
A1 = r1*r1 - x1*x1 - y1*y1 - z1*z1

A2 = r2*r2 - x2*x2 - y2*y2 - z2*z2
A3 = r3*r3 - x3*x3 - y3*y3 - z3*z3

A21 = -(A2 - A1)/2
A31 = -(A3 - A1)/2

D = x21 * y31 - y21 * x31
D = float(D)
B0 = (A21*y31 - A31 * y21)/D
B0 = float(B0)
B1 = (y21*z31 - y31 * z21)/D
B1 = float(B1)
C0 = (A31*x21 - A21 * x31)/D
C0 = float(C0)
C1 = (x31*z21 - x21 * z31)/D
C1 = float(C1)

e = B1*B1 + C1*C1 + 1
e = float(e)


f = (B1*(B0 - x1)) + (C1*(C0 - y1)) - z1
f = float(f)
g = (B0 - x1)*(B0 - x1) + (C0 - y1)*(C0 - y1) + z1*z1 - r1*r1
g = float(g)

a = f*f - e*g
a = float(a)

a = a ** (1/2)
##z = (-f - pow(a, 0.5))/e
z = (-f - a)/e

z = float(z)

x = B0 + B1 * z

y = C0 + C1 * z



print(x,y,z)