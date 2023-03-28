# Test REST service for the Intelligent LIMS hackathon

The mcube REST service will return a random number between 0-1.

## Running this example

1. In one shell

    ```sh
    cd ~/batch
    source ./env/bin/activate
    python ./batch_release.py
    ```

1. In another shell

    ```sh
    cd ~/batch
    ./test.sh
    ```

## Intallation

To setup the environment for this example:

```sh
cd batch
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

## Redeploy docker

```sh
docker-compose down
docker buildx build -t tcgdigitalus/batch-release:latest --file Dockerfile .
docker-compose up -d
```

