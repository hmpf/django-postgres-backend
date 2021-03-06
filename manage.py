#!/usr/bin/env python
import os, sys


if __name__ == "__main__":
    sys.path.append('./src')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.test_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
