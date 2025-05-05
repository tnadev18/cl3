from xmlrpc.server import SimpleXMLRPCServer

# Define the arithmetic operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero"

# Create an RPC server
with SimpleXMLRPCServer(("localhost", 8000)) as server:
    print("Server listening on port 8000...")

    # Register the functions
    for func in [add, subtract, multiply, divide]:
        server.register_function(func, func.__name__)

    # Run the server indefinitely
    server.serve_forever()
    
    #########################################################################################
    import xmlrpc.client

# Create an RPC proxy
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Main program loop
while True:
    choice = input("""
    Choose an operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit
    Enter your choice: """)
    
    if choice == '5':
        break
    
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter a valid option.")
        continue
    
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    # Execute the chosen operation
    result = getattr(proxy, ['add', 'subtract', 'multiply', 'divide'][int(choice) - 1])(x, y)
    print("Result:", result)

