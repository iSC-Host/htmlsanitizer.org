activate_this = '/var/www/bleach/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/bleach')

from app import app as application