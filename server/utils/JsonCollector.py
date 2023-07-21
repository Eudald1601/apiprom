from prometheus_client import CollectorRegistry, start_http_server, Metric, REGISTRY

import json
import sys
import time

class JsonCollector(CollectorRegistry):
    def __init__(self, diccionari):
        self.response = diccionari

    def collect(self):
        # Fetch the JSON
        print("entro")
        response = self.response
        # Convert requests and duration to a summary in seconds
        metric = Metric('svc_requests_duration_seconds',
            'Requests time taken in seconds', 'summary')
        metric.add_sample('latencia_ping',
            value=response['rtt_min'], labels={})
        print(metric.__str__)
        yield metric

        # Counter for the failures
        metric = Metric('Paquets_fallats',
        'Requests failed', 'summary')
        metric.add_sample('pck_fault',
        value=response['packet_loss_count'], labels={})
        print(metric.__str__)
        yield metric
