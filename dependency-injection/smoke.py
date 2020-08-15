# interface for clients
# clients know to call serve()
class Service():
    def __init__(self):
        pass
    def serve(self,client):
        print(f"Service {client.info()}")

# interface for services
# services need some information from clients
class Client():
    def __init__(self,name,service):
        self.service = service
        self.name = name
    def info(self):
        return self.name
    def do(self):
        pass

# classes that implement both service and client
class Tobacco(Service):
    pass

class Wizard(Client):
    def do(self):
        self.service.serve(self)

# assembler
def Injector():
    t = Tobacco()
    w0 = Wizard("w0",t)
    w1 = Wizard("w1",t)
    w0.do()
    w1.do()

Injector()

