#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.py."""
import os
import sys
import subprocess
import time


def main():
    """Run administrative tasks.py."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'goldfinger.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def start_browser():
    try:
        print('Recived: ' + os.environ['driver_url'])
    except KeyError:
        subprocess.Popen('pipenv shell python ' + os.getcwd() + '/webdriver/webdriver_initializer.py')
        time.sleep(10)
        from webdriver import webdriver_config
        os.environ['driver_url'] = webdriver_config.driver_url
        os.environ['driver_session_id'] = webdriver_config.driver_session_id


if __name__ == '__main__':
    start_browser()
    main()
