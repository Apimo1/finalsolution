primeLsts=[]
for n in range(2, max+1):
	isprime=True
	for y in range(2, max+1):
		if n%y == 0 :
			isprime= false
			break
	if isprime:
		primeList.append(n)

def prime_number(n):
	max= int(input( "Enter upto number of choice"))
for n in range (2, n+1):
	isprime=True
	for i in range(2,n):

		if i % y == 0:
			isprime=false
if isprime:
	print(n)