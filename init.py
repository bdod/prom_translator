from prometheus_client import start_http_server, Summary
import random
import time
import requests
import sys

from prometheus_client import Info, Gauge

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

URL=sys.argv[1]

from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY

class CustomCollector(object):
    def collect(self):
        r = requests.get(URL)
        res = r.json()
        for i in res:
          s_mname=i
          mname=i.replace('.','_')
          g = GaugeMetricFamily(mname, 'text', labels=['serv'])
          g.add_metric([i], res[s_mname])
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
    start_http_server(8000)
    # Generate some requests.
    while True:
        #process_request(random.random())
        process_request(10)
