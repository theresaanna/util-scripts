""" Takes a CSV with no headers
    Originally written for turning a CSV of complaint data tallies into a
    JSON object with nested product data to feed into a d3 treemap visualization.

    The CSV should have five columns without headers:
    1: Complaint group
    2: Complaint sub-group
    3: All time complaint count
    4: Last year complaint count
    5: This month complaint count
"""

import csv
import json

output = {'name': 'cr', 'children': []}
current_name = None
with open('cr.csv', 'rU') as crfile:
  data = csv.reader(crfile)
  for row in data:
    if not current_name:
      current_name = row[0]
      children = []

    if not row[0] == current_name:
      cluster = [{'name': current_name, 'children': children}]
      output['children'].extend(cluster)
      current_name = row[0]
      children = []

    children.append({'name': row[1], 'alltime': row[2], 'lastyear': row[3], 'avgmonth': row[4]})

cluster = [{'name': current_name, 'children': children}]
output['children'].extend(cluster)

with open('cr.json', 'w') as json_file:
  json.dump(output, json_file)
  print output

crfile.close()
json_file.close()
