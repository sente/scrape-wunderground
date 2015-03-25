import sys
import requests
import os
import grequests
import dateutil.parser
import datetime

from utils import create_urls


def chop(seq,size):
    """Chop a sequence into chunks of the given size."""
    chunk = lambda i: seq[i:i+size]
    return map(chunk,xrange(0,len(seq),size))


def get_chunk(chunk):
    reqs = (grequests.get(u['url']) for u in chunk)
    foo = grequests.map(reqs)
    for r in foo:
        year,month,day = r.request.url.split('/')[6:9]
        fname = 'data/%s-%s-%s.html' % (year,month,day)
        open(fname, 'w').write(r.content)
        print fname


dates, urls = create_urls(40)


foobar = [{'date':x[0], 'url':x[1]} for x in zip(dates,urls)]


for chunk in chunks:
    get_chunk(chunk)

