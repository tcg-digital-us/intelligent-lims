# Intelligent LIMS Microservice

The intelligent-lims Microservice is designed for ADMA Biologics and built with the Python 'easy deploy template'. It is a part of the test project for applying new microservices to TCG Digital's mcube software using mcube's internal Genie framework provided by the mcube development team.

## Overview

The intelligent-lims microservice provides an API designed for LabVantage LIMS that allows advanced analytics and other operations to be run on data sent from LabVantage. Currently, only the LabVantage LIMS is supported for use with mcube due to the partnership between LabVantage and TCG Digital.

This service acts as a reverse proxy, validating the action string recieved in the payload against available actions to be run, parsing and transforming the payload data before sending that data to separate running services that provide more specific operations.

Intelligent-lims serves as a logging service as well, allowing developers to record and retrieve previous payloads and their associated results. An abstractable data storage class is provided for creating handlers with different data storage types, so that any data storage facility can be applied to this project (e.g. sql, elasticsearch, redis, etc.)

## Available Actions

- ``getScore``: Get score is a test microservice that does nothing but retun a random float, a justification, and an empty context.
- ``lookupTransaction``: If an action returns a transaction_id (indicating that results were saved), that transaction_id can be used with this action to get that saved record.

## API Usage

The API provides a POST endpoint at `/intelligent-lims`.

### Payload Schema

The required payload schema consists of an object with two properties: "action" and "content". The "action" is a string that represents the action to be performed, and the "content" is an object containing additional properties required for the action.

Example of a proper payload calling the 'getScore' endpoint:

```json
{
  "action": "getScore",
  "content": {
    "sdcid": "Batch",
    "id": {
      "keyid1": "492028",
      "keyid2": "38298427"
    },
    "data": [
      [20948, 28, 1838, 4082],
      [422, 2434, 21, 144],
      [249, 2928, 82, 18171]
    ]
  }
}
```

Example of a proper payload calling the 'lookupTransaction' endpoint:

```json
{
  "action": "lookupTransaction",
  "content": {
    "transaction_id": "8ue89hg98g19hdj0"
  }
}
```

## Adding a New Action

To add a new action, follow these steps:

1. Create a new module in the `source/actions/handlers` folder.
2. Make sure the class in the module extends the `ActionHandlerABC` class and overwrites the static method `exec`.
3. Create a class in the `src/microservices` directory that can be called by the new action handler for handling different payload and result formats.
4. Import the new handler class in `src/actions/ActionsHandler.py` and update the `action_handlers` dictionary with a new key-value pair. The key should be the action string expected in the payload, and the value should be the handler class.

## Deployment

Due to licensing and mcube requirements, this microservice must be deployed under Kubernetes. A Kubernetes deployment file is included in the project. Ensure the associated YAML files are updated with the correct image name and ports before deploying with Docker Compose or Kubernetes.

## Configuration

Modify the `config.toml` file to update the base URLs representing the hosted locations for each of the microservice classes making requests to the associated microservices. This TOML file can be changed while the Intelligent LIMS service is running, making it easy to modify the locations of the running microservices.
