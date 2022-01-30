from os.path import dirname, abspath, join
import sys

# Find code directory relative to our directory
THIS_DIR = dirname(__file__)
CODE_DIR = abspath(join(THIS_DIR, 'app'))
sys.path.append(CODE_DIR)
print(CODE_DIR)

from gevent.pywsgi import WSGIServer
from cii import app

    
 http_server = WSGIServer(('', 5000), app)
 http_server.serve_forever()
    
