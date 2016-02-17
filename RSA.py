# Calculate RSA decryption key
import random

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def is_prime(a):
    return all(a % i for i in xrange(2, a))

def RSA(P, Q, E, M): 
	N = P * Q
	phi = (P-1)*(Q-1)

	sickArray = set()

	print phi, "\n"

	# for i in range(1,phi+1):
	# 	if phi % i != 0:
	# 		for x in xrange(2,i+1):
	# 			if i+1 % x == 0:
	# 				break
	# 			sickArray.add(i)

	# E = int(random.sample(sickArray, 1)[0])
	# E = 7 
	D = 0
	if is_prime(phi):
		D = E**(-1)%phi
	else:
		D = modinv(E, phi)


	print "public key [", N,",", E,"]"
	print "private key[", N,",", D,"]"
	print "E =", E
	print "N =", N
	print "D =", D
	print "Message =", M

	C = M**E%N

	print "encrypted message =", C

	Decrypted = C**D % N
	print "decrypted message =", Decrypted

P = int(raw_input("Enter P (prime 1): "))
Q = int(raw_input("Enter Q (prime 2): "))
E = int(raw_input("Enter E (enc): "))
M = int(raw_input("Enter M (message): "))

RSA(P, Q, E, M)



