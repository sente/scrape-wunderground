import sys 
import pytz
import pprint
import lxml.html
import dateutil.parser


def process_file(file):

    root = lxml.html.fromstring(open(file).read())

    text = root.xpath('//h2[@class="history-date"]')[0].text_content()
    the_date = dateutil.parser.parse(text)

    foobar = root.xpath('//td[(((count(preceding-sibling::*) + 1) = 13) and parent::*)] | //*[(@id = "obsTable")]//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)] | //*[(@id = "obsTable")]//td[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]')

    i = iter(foobar)

    res = []

    for time, temp, cond in zip(i,i,i):

        localtz = pytz.timezone('US/Eastern')
        the_time = time.text_content().strip().encode('utf-8','ignore')

        timestamp = dateutil.parser.parse('%s %s' % ( the_date, the_time))
        timestamp = localtz.localize(timestamp)

        res.append([timestamp,
                    temp.text_content().strip().encode('utf-8'),
                    cond.text_content().strip().encode('utf-8')])

    return res


for f in sys.argv[1:]:
    print f
    data = process_file(f)
    for row in data:
        print '\t'.join(map(str,row))
