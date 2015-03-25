import lxml
import lxml.html
import sys

def process_file(file):

    print 'processing %s' % file
    root = lxml.html.fromstring(open(file).read())
    foobar = root.xpath('//td[(((count(preceding-sibling::*) + 1) = 13) and parent::*)] | //*[(@id = "obsTable")]//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]')
    i = iter(foobar)
    res = []
    for temp,condition in zip(i,i):
        res.append( [temp.text_content().strip().encode('utf-8'),condition.text_content().strip()])

    return res

if __name__ == '__main__':
    for f in sys.argv[1:]:
        data = process_file(f)
        for row in data:
            print row[0],row[1] 


