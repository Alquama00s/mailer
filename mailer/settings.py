import os

if 'SERVER_MODE' in os.environ and os.environ['SERVER_MODE'] == "prod":
    print ("PROD SERVER")
    from .settings_prod import *
else:
    print ("DEV SERVER")
    from .settings_dev import *
   