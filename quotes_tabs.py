""" Takes a CSV file and spits out a new CSV with
    double quotes around each column, delimited
    by tabs.
"""

import csv

with open('thing.csv', 'rU') as csvfile, open('quoteswithtabs.csv', 'wb') as newfile:
  data = csv.reader(csvfile)
  write = csv.writer(newfile, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
  for row in data:
    newrow = []
    for col in row:
      newrow.append('"%s"' % col)
    write.writerow(newrow)

csvfile.close()
newfile.close()
