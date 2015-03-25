import datetime
import dateutil.parser



url = "http://www.wunderground.com/history/airport/KBOS/$DATE/DailyHistory.html?req_city=Somerville&req_state=MA&req_statename=Massachusetts&reqdb.zip=02144&reqdb.magic=1&reqdb.wmo=99999"

def create_urls(days):

    now = datetime.datetime.now()
    dates = [now - datetime.timedelta(days=n) for n in range(days)]
    formatted_dates = [d.strftime('%Y/%m/%d') for d in dates]
    urls = [url.replace('$DATE',formatted_date) for formatted_date in formatted_dates]

    return [dates,urls]
