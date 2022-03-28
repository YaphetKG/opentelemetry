# jaeger_tracing.py

import httpx

# ------ SETUP OPEN-TELEMETRY FOR HTTPX
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from jaeger_setup import setup_jaeger
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
setup_jaeger("simple-client")
HTTPXClientInstrumentor().instrument()
# ------ END OPEN-TELEMETRY


def make_call():
    url = "http://localhost:5000/foobar"

    with httpx.Client() as client:
        response = client.get(url)


if __name__ == '__main__':
    make_call()