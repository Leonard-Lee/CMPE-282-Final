import sys, os
sys.path.insert (0,'/var/www/html/mobilesensor')
os.chdir("/var/www/html/mobilesensor")

from app import app as application