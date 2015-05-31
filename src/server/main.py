#/usr/bin/env python

import sys

if __name__ == '__main__':
    listen_port = sys.argv[3]
    reloader_port = sys.argv[2]
    traverser = Traverser(sys.argv[1])
    indexer = Indexer(traverser)
    # start a server
    reloader = Reloader()
    reloader.listen(reloader_port)
    server = Server(listen_port)
    server.start()
    reloader.start()
