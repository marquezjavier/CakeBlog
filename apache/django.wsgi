import os
import sys


path = sys.path.append('/srv/www')
if path not in sys.path:
    sys.path.insert(0, '/srv/www/cakeashes')

os.environ['DJANGO_SETTINGS_MODULE'] = 'cakeashes.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

