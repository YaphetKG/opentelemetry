import fastapi
import uvicorn
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from jaeger_setup import setup_jaeger




app = fastapi.FastAPI()

@app.get("/another_endpoint")
async def foobar():
    return {"message": "hello world"}

# ------ SETUP OPEN-TELEMETRY FOR FASTAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from jaeger_setup import setup_jaeger
setup_jaeger("http-server-2")
FastAPIInstrumentor.instrument_app(app)
# ------ END OPEN-TELEMETRY

if __name__ == '__main__':
    uvicorn.run(app, port=5001)