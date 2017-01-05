#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "{{ project_name }}.settings.local")

    SQL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'db.sqlite3')
    SQL_URL = "".join(["sqlite:///", SQL_DIR])
    os.environ.setdefault("DATABASE_URL", SQL_URL)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
