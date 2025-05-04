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
