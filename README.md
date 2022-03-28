# Introduction 
Jaeger based Open telemetry prototype. 

#### Prototype Architecture

<img width="422" alt="image" src="https://user-images.githubusercontent.com/45075777/160414989-55668178-a03e-4c3b-a051-6d2c81eaa3c2.png">



## Installation

Install Python dependencies

```shell
pip install -r requirements
```

## Setup Jaeger backend

Run Jaeger container

```shell
./run-jaeger.sh
```

## Start tracing


#### Run Web servers

```shell
python simple-server.py
python simple-server-2.py
```

#### Run client 

```shell
python simple.py
```

## Previews

On web browser navigate to `http://localhost:16686` for Jaeger UI.

### Search trace 
<img width="957" alt="image" src="https://user-images.githubusercontent.com/45075777/160415518-80ba3e7e-ca74-48c5-b449-0908c04d6ae6.png">

### View Spans in a trace 
<img width="957" alt="image" src="https://user-images.githubusercontent.com/45075777/160415856-a46cce72-24ad-4e52-a6bb-01c6fe3e57d6.png">

### View Architecture Overview (based on collected traces)
<img width="957" alt="image" src="https://user-images.githubusercontent.com/45075777/160416053-22deb874-e488-4ad3-8ec9-19854a4bead4.png">

