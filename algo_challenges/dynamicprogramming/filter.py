url_with_dp_patten = "http[s]?://www.amazon.in/dp/[a-zA-Z0-9-]{19}"
url_with_slredirect = "http[s]?://www.amazon.in/gp/slredirect/picassoRedirect.html/"
url_with_sl_redirect = "http://www.amazon.in/gp/slredirect/redirect.html/ref="
import re
import csv

# with open('/Users/Indix/Downloads/tmp/file1.txt', 'rb') as tsvin:
#     tsvin = csv.reader(tsvin, delimiter='\t')
#
#     for row in tsvin:
#         print row
#

def filter():
    file = open("/Users/Indix/Downloads/file.txt")
    target1 = open(("/Users/Indix/Downloads/wrong_urls1/dp_pattern.txt"), 'w')
    target2 = open(("/Users/Indix/Downloads/wrong_urls1/picasso_redirect_patter.txt"), 'w')
    target3 = open(("/Users/Indix/Downloads/wrong_urls1/slredirect.txt"), 'w')
    target4 = open(("/Users/Indix/Downloads/wrong_urls1/other.txt"), 'w')
    with open('/Users/Indix/Downloads/tmp/file1.txt', 'rb') as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')

        for row in tsvin:

            i = row[0]

            pattern1 = re.compile(url_with_dp_patten)
            pattern2 = re.compile(url_with_sl_redirect)
            pattern3 = re.compile(url_with_slredirect)
            if pattern1.match(i):
                target1.write(row[0] + "," + row[1]+"\n")
            elif pattern2.match(i):
                target2.write(row[0] + "," + row[1]+"\n")
            elif pattern3.match(i):
                target3.write(row[0] + "," + row[1]+"\n")
            else:
                target4.write(row[0] + "," + row[1]+"\n")
    target1.close()
    target2.close()
    target3.close()
    target4.close()

filter()
