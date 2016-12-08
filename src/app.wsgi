import sys, os
sys.path.insert (0,'/var/www/terminal_blog')
os.chdir("/var/www/terminal_blog")

from app import app as application