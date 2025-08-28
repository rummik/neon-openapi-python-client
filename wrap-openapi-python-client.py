#!/usr/bin/env python
import aenum
import http

aenum.extend_enum(http.HTTPStatus, 'O_K', 222, 'Neon extra OK response')


import sys
from openapi_python_client.cli import app
if __name__ == '__main__':
    if sys.argv[0].endswith('.exe'):
        sys.argv[0] = sys.argv[0][:-4]

    # Generating a patched version of the Neon CRM schema:
    #   sed -r \
    #       -e "s/^( +)([0-9]+):/\1'\2':/;" \
    #       -e "s/^( +)['\"]\*\/\*['\"]:\$/\1'application\/json':/;" \
    #       ~/Downloads/v2.10.yaml > /tmp/v2.10-patched.yaml

    # argv0 = sys.argv[0]
    #
    # sys.argv = [
    #     argv0,
    #     'generate',
    #     '--overwrite',
    #     '--config',
    #     'client-config.yaml',
    #     '--path',
    #     # '--url',
    #     '/tmp/v2.10-patched.yaml',
    # ]

    sys.exit(app())
