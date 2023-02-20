

"""Gunicorn *development* config file"""

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "mailer.wsgi:application"
# The granularity of Error log outputs
loglevel = "warning"
# The number of worker processes for handling requests
workers = 3
# The socket to bind
bind = "0.0.0.0:8000"
# Restart workers when code changes (development only!)
reload = False
# Write access and error info to /var/log
accesslog = errorlog = "configs/gunicorn/dev.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "configs/gunicorn/dev.pid"
# Daemonize the Gunicorn process (detach & enter background)
# daemon = True