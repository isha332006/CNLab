import http.server
import socketserver
import hashlib
import os

PORT=8080

class CachingHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path=self.translate_path(self.path)
        if not os.path.isfile(path):
            self.send_error(404, "File not found")
            return None

        # Read file contents to compute ETag
        with open(path,'rb') as f:
            content=f.read()
        etag=hashlib.md5(content).hexdigest()
        modification_time=os.path.getmtime(path)
        last_modified=self.date_time_string(modification_time)

        # Check client cache headers
        if_none_match=self.headers.get('If-None-Match')
        if_modified_since=self.headers.get('If-Modified-Since')

        if ((if_none_match==etag) or (if_modified_since==last_modified)):
            self.send_response(304)
            self.send_header("ETag",etag)
            self.send_header("Last-Modified",last_modified)
            self.end_headers()
            return None

        self.send_response(200)
        self.send_header("ETag",etag)
        self.send_header("Last-Modified",last_modified)
        self.send_header("Content-type",self.guess_type(path))
        self.send_header("Content-Length",str(len(content)))
        self.end_headers()
        return open(path,'rb')

    def do_GET(self):
        f=self.send_head()
        if f:
            self.copyfile(f,self.wfile)
            f.close()

if __name__=="__main__":
    with socketserver.TCPServer(("",PORT),CachingHandler) as httpd:
        print(f"Serving HTTP caching server on port {PORT}")
        httpd.serve_forever()
