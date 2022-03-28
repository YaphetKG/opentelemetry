# Introduction 
Jaeger based Open telemetry prototype. 

#### Prototype Architecture



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

