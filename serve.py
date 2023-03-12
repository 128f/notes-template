from http import server

# originally
# python -m http.server 9000 --directory output

class Handler(server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        kwargs["directory"] = "output"
        super(Handler, self).__init__(*args, **kwargs)

    def guess_type(self, path):
        guess = super(Handler, self).guess_type(path)
        if guess == 'application/octet-stream':
            return "text/html"
        return guess

if __name__ == '__main__':
    server.test(HandlerClass=Handler)
