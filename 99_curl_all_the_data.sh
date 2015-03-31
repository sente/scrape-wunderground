

seq 1 1000 | while read day; do

    DATE=$(date -d "- $day days" +%Y/%m/%d);
    FILE=$(date -d "- $day days" +%Y-%m-%d.dat);

    URL="http://www.wunderground.com/history/airport/KBOS/${DATE}/DailyHistory.html?reqdb.zip=02144&format=1";

    curl -s -o "data-curl/$FILE" "$URL"

done



