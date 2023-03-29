# Test REST service for the Intelligent LIMS hackathon

The mcube REST service that will return a random number between 0-1.

## About

This rest service acquires the releaseScore for the following SDC's via POST request:

|SDC|sdc\_id|
|---|--------|
|Batch|"Batch"|
|Batch Stage|"BatchStage"|
|Sample|"Sample"|
|Monitor Group|"MonitorGroup"|

The sdc\_id is a required parameter in the POST request. Any other relevant data can be included in the post request and it will be available in the relevant handlers.

## Prerequisites

This solution requires:

- python v3
- make
- docker

## Develop

### Local Run

```
make run-dev
```

### Build

```
make build
```

## Deploy

### Run

```
make up
```

### Stop

```
make down
```

## Test

Powershell
```
Invoke-WebRequest -Uri "http://3.214.69.84:5002/releaseScore" -Method POST -ContentType "application/json" -Body '{"sdcid": <sdc_id>, ... }'
```

Bash
```
curl -X POST -H "Content-Type: application/json" -d '{"sdcid": <sdc_id>, ... }' "http://3.214.69.84:5002/releaseScore"
```


