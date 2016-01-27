from fabric.api import *
from fabric.utils import puts

#Set your drupal workspace here. This should be your root of the directory
DRUPAL_WORKSPACE = ''

def restart_apache():
    """Restart apache, make sure you give the user to run sudo, for linux"""
    sudo('/etc/init.d/httpd graceful')


def clear_caches(workspace):
    """Clear cache for the entire drupal instance"""
    run('./drush cc all')


@runs_once
def js_reagg(workspace):
    """Task to reaggregate js """
    run('./drush vset preprocess_js 0')
    run('./drush vset preprocess_js 1')


@runs_once
def css_reagg():
    """Task to reaggregate css only"""
    run('./drush vset preprocess_css 0')
    run('./drush vset preprocess_css 1')


@runs_once
def css_js_reagg():
    """Task to reaggregate css & js """
    js_reagg()
    css_reagg()
