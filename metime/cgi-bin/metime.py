#!/usr/bin/env python3

import os
from datetime import datetime, date, timedelta

today = datetime.today().date() # date(2019, 10, 22)
start = today - timedelta(days=today.weekday())

title = os.environ.get('METIME_TITLE', 'Me-Time')
person1 = os.environ.get('METIME_PERSON1', 'Person 1')
person2 = os.environ.get('METIME_PERSON2', 'Person 2')

HEAD = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>''' + title + '''</title>
  <style type="text/css">

      body {
        margin: auto;
        max-width: 800px;
        font-family: Arial, Helvetica, sans-serif;
      }

    svg {
      float: right;
    }

    th, td {
      border: 1px solid black;
      padding: 15px;
      height: 15px;
      text-align: center;
    }

    table {
      border-collapse: collapse;
    }

    </style>
  </head>
  <body>
  <h1>''' + title + '''
  <svg
     xmlns:dc="http://purl.org/dc/elements/1.1/"
     xmlns:cc="http://creativecommons.org/ns#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:svg="http://www.w3.org/2000/svg"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
     xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
     width="0.7cm"
     height="1.5cm"
     viewBox="0 0 539.99987 986.85719"
     id="svg2"
     version="1.1"
     inkscape:version="0.91 r13725"
     sodipodi:docname="sanduhr.svg">
    <defs
       id="defs4" />
    <sodipodi:namedview
       id="base"
       pagecolor="#ffffff"
       bordercolor="#666666"
       borderopacity="1.0"
       inkscape:pageopacity="0.0"
       inkscape:pageshadow="2"
       inkscape:zoom="0.35"
       inkscape:cx="-1131.7272"
       inkscape:cy="785.14097"
       inkscape:document-units="px"
       inkscape:current-layer="layer1"
       showgrid="false"
       fit-margin-top="0"
       fit-margin-left="0"
       fit-margin-right="0"
       fit-margin-bottom="0"
       inkscape:window-width="1920"
       inkscape:window-height="1023"
       inkscape:window-x="0"
       inkscape:window-y="0"
       inkscape:window-maximized="1" />
    <metadata
       id="metadata7">
      <rdf:RDF>
        <cc:Work
           rdf:about="">
          <dc:format>image/svg+xml</dc:format>
          <dc:type
             rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
          <dc:title></dc:title>
        </cc:Work>
      </rdf:RDF>
    </metadata>
    <g
       inkscape:label="Layer 1"
       inkscape:groupmode="layer"
       id="layer1"
       transform="translate(-95.008367,-67.076512)">
      <g
         id="g4152"
         transform="translate(1805.7143,131.42857)">
        <rect
           ry="29.816853"
           y="-64.352058"
           x="-1710.7059"
           height="62.857147"
           width="539.99988"
           id="rect4134"
           style="opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.58566791;stroke-linecap:round;stroke-miterlimit:4;stroke-dasharray:1.17133582, 2.34267163;stroke-dashoffset:0;stroke-opacity:1" />
        <path
           sodipodi:nodetypes="csc"
           inkscape:connector-curvature="0"
           id="path4139"
           d="m -1667.11,20.63411 c 0,392.52408 203.5897,314.46372 203.5897,408.72809 0,102.04758 -205.1745,5.59527 -205.1745,408.72813"
           style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:28.22912407;stroke-linecap:round;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
        <path
           style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:28.22912407;stroke-linecap:round;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           d="m -1206.1635,20.63411 c 0,392.52408 -203.5897,314.46372 -203.5897,408.72809 0,102.04758 205.1745,5.59527 205.1745,408.72813"
           id="path4141"
           inkscape:connector-curvature="0"
           sodipodi:nodetypes="csc" />
        <rect
           style="opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.58566791;stroke-linecap:round;stroke-miterlimit:4;stroke-dasharray:1.17133582, 2.34267163;stroke-dashoffset:0;stroke-opacity:1"
           id="rect4143"
           width="539.99988"
           height="62.857147"
           x="-1710.7059"
           y="859.64795"
           ry="29.816853" />
        <path
           inkscape:transform-center-x="3.9258023e-05"
           sodipodi:nodetypes="scccs"
           inkscape:connector-curvature="0"
           id="path4145"
           d="m -1439.2459,653.70076 c 125.826,0 152.8336,134.52591 220.5968,194.17191 l -220.5968,0 -220.5969,0 c 81.1294,-41.6429 104.8514,-194.17191 220.5969,-194.17191 z"
           inkscape:transform-center-y="-32.362019"
           style="opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:10.48734951;stroke-linecap:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1" />
        <path
           style="opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:10.48734951;stroke-linecap:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1"
           inkscape:transform-center-y="32.362019"
           d="m -1442.103,360.15838 c 74.7117,-2.68097 138.5478,-48.50239 192.0253,-151.31476 0,0 -116.2993,-51.42857 -192.0253,-51.42857 -75.7261,-1e-5 -180.5969,45.71428 -180.5969,45.71428 29.7009,64.50004 99.6982,159.93203 180.5969,157.02905 z"
           id="path4148"
           inkscape:connector-curvature="0"
           sodipodi:nodetypes="scscs"
           inkscape:transform-center-x="3.9258023e-05" />
        <rect
           ry="10"
           y="281.5051"
           x="-1443.3898"
           height="528.57141"
           width="14.1124"
           id="rect4150"
           style="opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:14.52200031;stroke-linecap:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1" />
      </g>
    </g>
  </svg>
</h1>
'''

FOOT = '''
  </body>
</html>
'''

print(HEAD)

print('''
<table style="width:100%">
<colgroup>
<col style="width:20%">
<col style="width:40%">
<col style="width:40%">
</colgroup>
<tbody>
  <tr>
    <th>Woche</th>
    <th>{}</th>
    <th>{}</th>
  </tr>
'''.format(person1, person2))

dayfmt = '%d.%m'
for i in range(16):
    day_from = start + timedelta(days=7*i)
    day_to = day_from + timedelta(days=6)
    print('''<tr>
        <td>{} - {}</td>
        <td></td>
        <td></td>
      </tr>'''.format(day_from.strftime(dayfmt), day_to.strftime(dayfmt)))

print('''
</tbody>
</table>
''')

print(FOOT)
