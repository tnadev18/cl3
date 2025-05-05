from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
	if n==0 or n==1:
		return 1
	else:
		return n*factorial(n-1)

server=SimpleXMLRPCServer(('localhost',8000))
server.register_function(factorial,'calculate_factorial')
print("Server is ready")
server.serve_forever()

###################################################################################
import xmlrpc.client

def main():
	server = xmlrpc.client.ServerProxy('http://localhost:8000')
	n = int(input("Enter input : "))
	result = server.calculate_factorial(n)
	print(f"Factorial of {n} is {result}")

if __name__=='__main__':
	main()