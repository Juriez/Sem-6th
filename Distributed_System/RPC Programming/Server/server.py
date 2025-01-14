from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")

server.register_function(factorial, "factorial")

server.serve_forever()
