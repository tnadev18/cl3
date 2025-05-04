import xmlrpc.client

def main():
	server = xmlrpc.client.ServerProxy('http://localhost:8000')
	n = int(input("Enter input : "))
	result = server.calculate_factorial(n)
	print(f"Factorial of {n} is {result}")

if __name__=='__main__':
	main()