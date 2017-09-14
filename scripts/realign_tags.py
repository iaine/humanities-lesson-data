'''
   Script to improve the concatenated terms in TCP data fordatabase lesson
   author: Iain Emsley
'''
import csv
import sys

write_file = sys.argv[1]
read_file = sys.argv[2]

with open(write_file, 'wb') as f:
    writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    with open(read_file, 'rU') as fh:
        data = csv.reader(fh, delimiter=',', quotechar='|')
        print(data)
        for row in data:
            _id = row[0]
            if ';' in row[1]:
                terms = row[1].split(';')
                for term in terms:
                    if term.startswith('"'):
                        term = term[1:]
                    #print(_id + " : " +  str(term).strip())
                    writer.writerow([_id,str(term).strip()])

            elif row[1]:
            #    print(_id + " : " + row[1])
                writer.writerow([_id, str(row[1]).strip()])
