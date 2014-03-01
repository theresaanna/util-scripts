""" Takes a CSV file and spits out
    a new one with double quotes around each col.
"""

import csv

with open('thing.csv', 'rU') as csvfile, open('quotes.csv', 'wb') as newfile:
  data = csv.reader(csvfile)
  write = csv.writer(newfile, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
  for row in data:
    newrow = []
    for col in row:
      newrow.append('"%s"' % col)
    write.writerow(newrow)

csvfile.close()
newfile.close()
