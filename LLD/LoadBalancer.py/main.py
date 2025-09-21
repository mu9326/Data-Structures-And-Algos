from abc import ABC, abstractmethod
from typing import List


# Server class
class Server:
    def __init__(self, server_id: str):
        self.server_id = server_id
        self.is_healthy = True
        # Placeholder for current connections
        self.current_connections = 0

    def __str__(self):
        return f"Server({self.server_id})"

    def set_healthy(self, healthy: bool):
        self.is_healthy = healthy


# Request class (placeholder)
class Request:
    pass


# LoadBalancingStrategy interface
class LoadBalancingStrategy(ABC):
    @abstractmethod
    def get_server(self, servers: List[Server], request: Request) -> Server:
        pass


# RoundRobinStrategy
class RoundRobinStrategy(LoadBalancingStrategy):
    def __init__(self):
        self.current_index = 0

    def get_server(self, servers: List[Server], request: Request) -> Server:
        total_servers = len(servers)
        if total_servers == 0:
            raise Exception("No servers available")
        server = servers[self.current_index]
        self.current_index = (self.current_index + 1) % total_servers
        return server


# LeastConnectionsStrategy
class LeastConnectionsStrategy(LoadBalancingStrategy):
    def get_server(self, servers: List[Server], request: Request) -> Server:
        min_connections = float("inf")
        selected_server = None

        for server in servers:
            if server.is_healthy:
                if server.current_connections < min_connections:
                    min_connections = server.current_connections
                    selected_server = server

        if selected_server is None:
            raise Exception("No healthy servers available")
        return selected_server


# LoadBalancer class (Singleton)
class LoadBalancer:
    _instance = None

    def __init__(self):
        self.servers: List[Server] = []
        self.strategy: LoadBalancingStrategy = None

    @staticmethod
    def get_instance():
        if LoadBalancer._instance is None:
            LoadBalancer._instance = LoadBalancer()
        return LoadBalancer._instance

    def add_server(self, server: Server):
        self.servers.append(server)

    def remove_server(self, server: Server):
        self.servers.remove(server)

    def set_load_balancing_strategy(self, strategy: LoadBalancingStrategy):
        self.strategy = strategy

    def get_server(self, request: Request) -> Server:
        if not self.strategy:
            raise Exception("Load balancing strategy not set")
        return self.strategy.get_server(self.servers, request)


# Main logic
if __name__ == "__main__":
    # Create servers
    server1 = Server("server1")
    server2 = Server("server2")

    # Create load balancer
    load_balancer = LoadBalancer.get_instance()
    load_balancer.add_server(server1)
    load_balancer.add_server(server2)

    # Set load balancing strategy
    round_robin_strategy = RoundRobinStrategy()
    load_balancer.set_load_balancing_strategy(round_robin_strategy)

    # Create requests
    request1 = Request()
    request2 = Request()

    # Get server for requests
    selected_server1 = load_balancer.get_server(request1)
    print("Selected server for request1:", selected_server1)

    selected_server2 = load_balancer.get_server(request2)
    print("Selected server for request2:", selected_server2)
