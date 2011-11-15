# complete_project.wsgi is configured to live in projects/complete_project/deploy.
# If you move this file you need to reconfigure the paths below.
import sys
from os.path import abspath, dirname, join
from os import environ

# redirect sys.stdout to sys.stderr for bad libraries like geopy that uses
# print statements for optional import exceptions.
sys.stdout = sys.stderr

import site
site.addsitedir('/var/www/localwiki_temp/env/lib/python2.6/site-packages/')
sys.path.insert(0, abspath(join(dirname(__file__), "..","..")))

from django.core.handlers.wsgi import WSGIHandler
from django.conf import settings

environ["DJANGO_SETTINGS_MODULE"] = "localwiki_splash.settings"

sys.path.insert(0, settings.PROJECT_PATH)

application = WSGIHandler()

