# Diffie-Hellman - Calculate shared key
def calcSharedKey(G,N,X,Y):
	# Calculate A and B values
	A = (G ** X) % N
	B = (G ** Y) % N
	key = (B**X) % N 

	# Print the maths the script has done
	print "\n"
	print "A= (",G,"^",X," mod ",N," = ", A
	print "B= (",G,"^",Y," mod ",N," = ", B
	print "Key= (",B,"^",X," mod ",N," = ", key
	print "\n"

	# Print A, B and Key values without maths behind them
	print "A =",(G ** X) % N
	print "B =",(G ** Y) % N
	print "Key = ", (B**X) % N
	print "\n"

G = int(raw_input("Enter G (prime 1): "))
N = int(raw_input("Enter N (prime 2): "))
X = int(raw_input("Enter X (enc): "))
Y = int(raw_input("Enter Y (message): "))

calcSharedKey(G, N, X, Y)