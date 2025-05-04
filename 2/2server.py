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
