#!/usr/bin/env python3

import os
import json
from urllib.request import urlopen

host = os.environ.get('HOST')

HEAD = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Private Cloud</title>
  <style type="text/css">

      body {
        margin: auto;
        max-width: 800px;
        font-family: Arial, Helvetica, sans-serif;
      }
    </style>
  </head>
  <body>
  <h1>Private Cloud</h1>
'''

FOOT = '''
  </body>
</html>
'''

print(HEAD)

print('''
<ul>
''')

with urlopen(f"http://{host}:8080/api/http/routers") as f:
    for router in json.load(f):
        if router["provider"] != "internal" and "reverse-proxy" not in router["name"] and not router["name"].startswith("index@"):
            name = router["name"].split("@")[0]
            route = router["rule"].split("`")[1]
            print(f'<li><a href="//{route}">{name}</a></li>')


print('''
</ul>
''')

print(FOOT)
