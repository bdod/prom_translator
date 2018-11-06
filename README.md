# prom_translator
Translate metrics to prometheus format

This utility helping to change the format of metrics  from json to prometheus compatible. 

You can add own hook to Collect function, to change metrics format or add labels.

Usage :
```
 python init.py '<upstream_url>'
```
If you want use it for many upstreams you can add it to URL dict in multiupstream_init.py and run as 
```
python multiupstream_init.py
```


run with docker
```
docker build . -t ptranslate
docker run -d -e 'UPSTREAM=<upstream url>' -p 8000:8000 ptranslate
```



