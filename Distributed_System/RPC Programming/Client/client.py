import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")

while True:
    try:
      
        number = int(input("Enter a number to compute its factorial (or -1 to exit): "))
        
        if number == -1:
            print("Exiting the client.")
            break
        
        if number < 0:
            print("Factorial is not defined for negative numbers. Try again.")
            continue
        
        print(f"Requesting factorial of {number}...")
        result = server.factorial(number)

        print(f"The factorial of {number} is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except Exception as e:
        print(f"An error occurred: {e}")
