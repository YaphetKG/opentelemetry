import fastapi
import uvicorn
import httpx
app = fastapi.FastAPI()

@app.get("/foobar")
async def foobar():
    async with httpx.AsyncClient() as client:
        response = await client.get('http://localhost:5001/another_endpoint')
        resp = response.json()
    return resp


# ------ SETUP OPEN-TELEMETRY FOR FASTAPI AND HTTPX

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from jaeger_setup import setup_jaeger
setup_jaeger("http-server-1")
FastAPIInstrumentor.instrument_app(app)
HTTPXClientInstrumentor().instrument()
# ------ END OPEN-TELEMETRY

if __name__ == '__main__':
    uvicorn.run(app, port=5000)