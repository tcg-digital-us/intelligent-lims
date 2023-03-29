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

### Run Locally

First a python3 virtual environment will be created and the ``build/requirements.txt`` prerequisites will be installed. After that the app should run normally. Upon exiting the local run with a sigterm or equivalent, the virtual environment should be automatically deactivated as well.

```
make run-dev
```

### Clean

```
make clean
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

The only element that is currently required in the call is ``sdcid`` (see chart above for appropriate scdid values). All other data will be provided to the api handlers as well.

- Powershell
  ```
  Invoke-WebRequest -Uri "http://3.214.69.84:5002/releaseScore" -Method POST -ContentType "application/json" -Body '{"sdcid": <sdc_id>, ... }'
  ```

- Bash
  ```
  curl -X POST -H "Content-Type: application/json" -d '{"sdcid": <sdc_id>, ... }' "http://3.214.69.84:5002/releaseScore"
  ```


