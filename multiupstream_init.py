from prometheus_client import start_http_server, Summary
import random
import time
import requests
import json

from prometheus_client import Info,Gauge

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

URLS=[
      'http://url1.upstream.com/metrics',
      'http://url2.upstream.com/metrics'
      ]

from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY

class CustomCollector(object):
    def collect(self):
        results = {}
        metrics = []
        for u in URLS:
          r = requests.get(u)
          res = r.json()
          results[u] = res
          for m in res:
            if m not in metrics:
              metrics.append(m)
        for i in metrics:
          s_mname=i
          mname=i.replace('.','_')
          g = GaugeMetricFamily(mname, 'text', labels=['serv'])
          for x in results:
            try:
              g.add_metric([x], results[x][s_mname])
            except Exception as e:
              print(e)
          yield g

REGISTRY.register(CustomCollector())


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    Collector = CustomCollector()
    Collector.collect()
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8008)
    # Generate some requests.
    while True:
        process_request(10)
