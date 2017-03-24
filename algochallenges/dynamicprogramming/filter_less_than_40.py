import csv

with open('/Users/Indix/Downloads/terms/terms_count/myntra1.txt', 'rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')

    target1 = open(("/Users/Indix/Downloads/to_seed_search_terms_myntra.txt"), 'w')
    for row in tsvin:
        length = len(row[1].split(","))
        if (length < 40):
            print row[0] , length
            target1.write(row[0] + "\n")
    target1.close()