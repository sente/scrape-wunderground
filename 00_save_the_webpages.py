import sys
import os
import requests
import datetime
import dateutil.parser

url = "http://www.wunderground.com/history/airport/KBOS/$DATE/DailyHistory.html?req_city=Somerville&req_state=MA&req_statename=Massachusetts&reqdb.zip=02144&reqdb.magic=1&reqdb.wmo=99999"

def create_urls(days):

    now = datetime.datetime.now()
    dates = [now - datetime.timedelta(days=n) for n in range(days)]
    formatted_dates = [d.strftime('%Y/%m/%d') for d in dates]
    urls = [url.replace('$DATE',formatted_date) for formatted_date in formatted_dates]
    
    return [dates,urls]

def download_urls(dates,urls):

    if not os.path.isdir('data'):
        os.mkdir('data')

    for the_date, url in zip(dates,urls):

        yyyy_mm_dd = the_date.strftime("%F")
        fname = 'data/%s.html'  % yyyy_mm_dd

        if os.path.exists(fname):
            print 'skipping: %s' % fname
            continue

        with open(fname, 'w') as ofile:
            resp = requests.get(url)
            if resp.status_code == 200:
                ofile.write(resp.content)
                print 'created: %s' % fname
            else:
                print "error: %s" % url


if __name__ == '__main__':

    num = sys.argv[1]
    dates,urls = create_urls(int(num))
    download_urls(dates,urls)

