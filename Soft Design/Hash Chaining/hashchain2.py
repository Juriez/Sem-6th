import hashlib

class ConsistentHashChain:
    def __init__(self):
        self.servers = []  
        self.keys = {}    

    def _hash(self, value):
        """Hash a value using SHA-256 and return a consistent hash."""
        return int(hashlib.sha256(value.encode()).hexdigest(), 16) % (2**32)

    def add_server(self, server_id, position=None):
        """Add a server at a specific position on the hash ring and redistribute keys."""
        print(f"Adding server: {server_id}")
        if position is None:
            self.servers.append(server_id)
        else:
            self.servers.insert(position, server_id)
        self.servers.sort(key=lambda server: self._hash(server))  # Ensure servers are sorted by their hash values

        self.redistribute_keys()

    def remove_server(self, server_id):
        """Remove a server from the hash ring and redistribute keys."""
        print(f"Removing server: {server_id}")
        if server_id in self.servers:
            self.servers.remove(server_id)
            self.redistribute_keys()
        else:
            print("Server not found!")

    def assign_key(self, key):
        """Assign a key to the appropriate server based on consistent hashing."""
        key_hash = self._hash(key)
        for server in self.servers:
            if key_hash <= self._hash(server):
                return server

        # If no server has a higher hash, wrap around to the first server
        return self.servers[0]

    def add_key(self, key):
        """Add a new key to the hash chain."""
        assigned_server = self.assign_key(key)
        self.keys[key] = assigned_server
        print(f"Key {key} added and assigned to server {assigned_server}")

    def redistribute_keys(self):
        """Redistribute keys based on the current state of the hash ring."""
        new_key_mapping = {}

        for key in self.keys:
            assigned_server = self.assign_key(key)
            new_key_mapping[key] = assigned_server

        self.keys = new_key_mapping

    def get_server_for_key(self, key):
        """Get the server responsible for a given key."""
        return self.keys.get(key, None)

    def display_state(self):
        """Display the current state of the hash chain."""
        print("\nCurrent Hash Chain State:")
        print(f"Servers: {self.servers}")
        print("Key Assignments:")
        for key, server in self.keys.items():
            print(f"  Key: {key} -> Server: {server}")

if __name__ == "__main__":
    hash_chain = ConsistentHashChain()

    predefined_servers = ["s1", "s2", "s3"]
    predefined_keys = ["key1", "key2", "key3"]

    for server in predefined_servers:
        hash_chain.add_server(server)

    for key in predefined_keys:
        hash_chain.add_key(key)

    hash_chain.display_state()

    while True:
        print("\nOptions:")
        print("1. Add Server")
        print("2. Remove Server")
        print("3. Add Key")
        print("4. Display State")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            server_id = input("Enter server ID: ")
            position = input("Enter position to add server (leave blank for automatic): ")
            if position.strip() == "":
                hash_chain.add_server(server_id)
            else:
                hash_chain.add_server(server_id, int(position))

        elif choice == "2":
            server_id = input("Enter server ID to remove: ")
            hash_chain.remove_server(server_id)

        elif choice == "3":
            key = input("Enter key to add: ")
            hash_chain.add_key(key)

        elif choice == "4":
            hash_chain.display_state()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
