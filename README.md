# scrape-wunderground

Some code which grabs, processes, and maybe even does science on historical
weather data from http://wunderground.com 



### grab the last 10 days of data 

```
stu@redmac ~/scrape-wunderground (master) $ python 00_save_the_webpages.py 10
created: data/2015-03-25.html
created: data/2015-03-24.html
created: data/2015-03-23.html
created: data/2015-03-22.html
created: data/2015-03-21.html
created: data/2015-03-20.html
created: data/2015-03-19.html
created: data/2015-03-18.html
created: data/2015-03-17.html
created: data/2015-03-18.html
```




### grab a couple columns from the html file

```
stu@redmac ~/scrape-wunderground (master) $ python 01_extract_temperature_and_conditions.py data/2015-03-19.html
processing data/2015-03-19.html
21.9 °F Clear
21.0 °F Clear
21.0 °F Clear
19.9 °F Clear
19.9 °F Clear
19.9 °F Clear
19.0 °F Partly Cloudy
19.9 °F Partly Cloudy
21.9 °F Partly Cloudy
23.0 °F Partly Cloudy
25.0 °F Partly Cloudy
28.0 °F Clear
30.0 °F Clear
32.0 °F Partly Cloudy
33.1 °F Partly Cloudy
33.1 °F Partly Cloudy
34.0 °F Partly Cloudy
33.1 °F Partly Cloudy
32.0 °F Partly Cloudy
30.9 °F Partly Cloudy
30.0 °F Clear
28.9 °F Clear
26.1 °F Partly Cloudy
stu@redmac ~/scrape-wunderground (master) $ 
```

