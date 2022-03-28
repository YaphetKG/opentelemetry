from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME as telemetery_service_name_key, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

def setup_jaeger(service_name):
   assert service_name and isinstance(service_name, str)

   trace.set_tracer_provider(
      TracerProvider(
          resource=Resource.create({telemetery_service_name_key: service_name})
      )
   )

   jaeger_exporter = JaegerExporter(
      agent_host_name="localhost",
      agent_port=6831,
   )
   trace.get_tracer_provider().add_span_processor(
      BatchSpanProcessor(jaeger_exporter)
   )

   tracer = trace.get_tracer(__name__)

