import ConfigParser
from indexer import Indexer
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.read('server.conf')
    indexer = Indexer(config.get('ServerConf', 'ROOT_DIRECOTRY'))
    indexer.start(config.get('ServerConf', 'IGNORE'))

    # Create server
    server = SimpleXMLRPCServer(("localhost", int(config.get('ServerConf', 'LISTEN_PORT'))),
                                requestHandler=RequestHandler)
    server.register_introspection_functions()
    server.register_instance(indexer)

    # Run the server's main loop
    server.serve_forever()