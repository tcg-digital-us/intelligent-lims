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

### Upload Built Image

```
make upload
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

## Mcube Genie Install

### Kubernetes

Get create a secret to be able to grab private containers from dockerhub:

```
kubectl create secret docker-registry tcgdigitalus-registry-secret --docker-username=tcgdigitalus --docker-password=z628Kkh#qmTE --docker-email=don.koch@tcgdigital.com -n default
```

Deploy the container to Kubernetes on mcube VM's:

```
sudo kubectl apply –f k8s-deploy.yml
```

### Openresty

```
sudo kubectl exec -it $(sudo kubectl get pods --all-namespaces | awk '/^default\s+openresty-/ {print $2}') -- /bin/sh 
```

```
cd /usr/local/openresty/nginx/conf/
```

Create a new nginx config in ``genie/intelligent-lims.yml``. Use ``vi`` to add a location config for the service in openresty deployed with mcube:

```
location /releaseScore {

#	access_by_lua '
#		local chk = require "licenseCheckService"
#		chk.check();
#	';

	proxy_pass http://3.214.69.84:5002/releaseScore;
	proxy_set_header Host $host;
	proxy_set_header X-Real-IP $remote_addr;
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	proxy_next_upstream error timeout invalid_header http_500 http_502
	http_503 http_504;
	proxy_redirect off;
	proxy_buffering off;
	proxy_set_header Host $http_host;
	client_body_in_file_only clean;
	client_body_buffer_size 32K;
	client_max_body_size 300M;
}
```

Update the mcube openresty configuration:

```
./update_config
```

Reload openresty:

```
sudo kubectl exec $(sudo kubectl get pods --all-namespaces | awk '/^default\s+openresty-/ {print $2}') -- /usr/local/openresty/bin/openresty -s reload
```

## Test Deployment

```
sudo curl $(sudo kubectl get service $(sudo kubectl get services -l app=intelligent-lims -o jsonpath='{.items[0].metadata.name}') -o jsonpath='{.spec.clusterIP}:{.spec.ports[0].port}')/releaseScore
```
