from BaseHTTPServer import *
from urlparse import urlparse
from os import path
from urllib2 import *
import math

googleApiKey = None

class Params:
    def __init__(self, width, height, bbox):
        self.width = width
        self.height = height
        self.bbox = bbox
        self.center = ((bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2)

        size = float(bbox[2] - bbox[0]) * 256 / width # cause google use 256 tile size
        self.zoom = -math.log(float(size) / 360, 2)

def getParams(path):
    query = urlparse.urlparse(path).query
    queryDict = dict([x.split('=') for x in query.split('&')])

    width = queryDict['WIDTH']
    height = queryDict['HEIGHT']
    bbox = queryDict['BBOX']
    return Params(int(width), int(height), map(float, bbox.split(',')))

def getGoogleTile(x, y, zoom, size):
    addr = 'http://maps.googleapis.com/maps/api/staticmap?center={0},{1}&maptype=satellite&zoom={2}&size={3}x{3}&sensor=false' \
            .format(y, x, zoom, size);

    if googleApiKey:
        keyString = '&key={0}'.format(googleApiKey)
        addr += keyString

    u = urlopen(addr)
    content = u.read()
    u.close()
    return content

class GoogleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/favicon.ico':
            return

        self.send_response(200)
        self.send_header("Content-type", "image/jpeg")
        self.end_headers()

        params = getParams(self.path)
        content = getGoogleTile(params.center[0], params.center[1], int(round(params.zoom)), params.width)

        self.wfile.write(content)
        self.wfile.close()


server = HTTPServer(('localhost', 8080), GoogleHTTPRequestHandler)
server.serve_forever()
