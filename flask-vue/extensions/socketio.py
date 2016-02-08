from flask_socketio import SocketIO
from flask_script import Server

import sys


socketio = SocketIO()


class AsyncServer(Server):
    def __call__(self, app, host, port, use_debugger, use_reloader,
                 threaded, processes, passthrough_errors):
        # we don't need to run the server in request context
        # so just run it directly

        if use_debugger is None:
            use_debugger = app.debug
            if use_debugger is None:
                use_debugger = True
                if sys.stderr.isatty():
                    print("Debugging is on. DANGER: Do not allow random users to connect to this server.", file=sys.stderr)
        if use_reloader is None:
            use_reloader = app.debug

        # use_debugger, threaded, processes and passthrough_errors are not supported
        socketio.run(app,
            host=host,
            port=port,
            debug=use_debugger,
            use_reloader=use_reloader,
            **self.server_options)
