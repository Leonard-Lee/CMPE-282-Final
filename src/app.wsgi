import os, sys
EXTRA_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))
if EXTRA_DIR not in sys.path:
    sys.path.append(EXTRA_DIR)

sys.path.insert (0,'/var/www/html/mobilesensor/src/')

from app import app as application