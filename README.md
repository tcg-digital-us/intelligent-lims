# intelligent lims microservice

do we want more than one LIMS? 
    NO

do we want to allow clients to send a batch of jobs and data or should calls be
relegated to one action per data?

if you send three actions, and two of them are okay, but one fails, how do you handle that?
if you send three actions and one takes really long, how do you handle that?
    should you make it that only one action can be called for a single call?
    or should it be that there is a timer and the quick ones are sent back immediately, and 
        slow ones are sent back later?

This microservice should only have a single root endpoint, and the 
action parameter sent in the POST request should determine how it should
act. The reasoning behind this is that the intelligent-lims microservice is 
already passing the POST to this url, we would rather, in this microservice,
gracefully catch and respond to the case that a specific action is unavailable
or unimplemented. The opposite, tacking the action onto the url in intelligent-lims
and making the equivalent routes available here to be called would make it so that
if a call was made to that url you wouldn't be able to distinguish if the root
url of the call was bad or if it was the route that doesn't exist, you would
just get a 404 or equivalent. In this case, we are separating the burden so that
intelligent-lims can error out if the url is missing or doesnt work, and then
lv-handler can filter out if the action does or doesnt exist, with a custom message.

Add new functionality by adding the equivalent action text key and function call
value in the actions dictionary.

There should only be one datastore in this app, because this app specifically only
needs a datastorage object for logging transaction results. This could be stored
in any type of way, so this should be abstract. Because there is only one, this
can be a singleton class.

Here is a payload example:

{
	"action": "getScore",
	"content": {
		"data": [
			[
				20948,
				28,
				1838,
				4082
			],
			[
				422,
				2434,
				21,
				144
			],
			[
				249,
				2928,
				82,
				18171
			]
		],
		"id": {
			"key_id1": "f483f98j",
			"key_id2": "f4fj903j83u",
			"key_id3": "f9j28u2"
		},
		"sdcid": "Batch"
	},
	"result": {
		"context": {},
		"justification": "Generated a random float",
		"releaseScore": 0.43502250991878766,
		"action_id": "9a33ac88-2f97-4872-a6cc-2dbf9c28e2d5"
	},
}


$(Invoke-WebRequest -Method Post -ContentType "application/json" -Body '{"action": "lookupTransaction", "content": {"transaction_id": "fb774673-e113-45bc-b351-ac98618bffc0"}}' -Uri http://localhost:5003/intelligent-lims -UseBasicParsing).Content

$(Invoke-WebRequest -Method Post -ContentType "application/json" -Body '{"action":"getScore","content":{"sdcid":"Batch","id":{"keyid1":"492028","keyid2":"38298427"},"data":[[20948,28,1838,4082],[422,2434,21,144],[249,2928,82,18171]]}}' -Uri http://localhost:5003/intelligent-lims -UseBasicParsing).Content

# intelligent-lims microservice

The purpose of this microservice is to handle the 'lims' attribute accordingly,
forwarding the package to the lv-handler for further evalutation.

<center>

![graph](./res/graph.svg)

</center>

## LIMS

To modify/add mappings for LIMS, enter the container and modify:

```
# LIMS to URL mapping
lims_to_url = {
    "labvantage": "https://some-kubernetes-cluster-service/lv-handler",
}
```

## Payload
```
{
	"lims": "labvantage",
	...
}

```
$(Invoke-WebRequest -Method Post -ContentType "application/json" -Body '{"lims": "labvantage", "action": "lookupTransaction", "shouldReport": true, "content": {"transaction_id": "9a33ac88-2f97-4872-a6cc-2dbf9c28e2d5"}}' -Uri http://localhost:5001/intelligent-lims -UseBasicParsing).Content
```

```
$(Invoke-WebRequest -Method Post -ContentType "application/json" -Body '{"lims": "labvantage", "action": "getScore", "shouldReport": true, "content": {"sdcid": "Batch", "labels": ["sdclabel184", "sdclabel284", "sdclabel281"], "data": [[44, 28, 1838, 4082], [10, 221, 213, 22], [249, 2928, 82, 18171]]}}' -Uri http://localhost:5004/intelligent-lims -UseBasicParsing).Content
```

```
$(Invoke-WebRequest -Method Post -ContentType "application/json" -Body '{"lims": "labvantage", "action": "lookupTransaction", "shouldReport": true, "content": {"transaction_id": "ab90a2af-b948-4725-9422-fca237f2f30d"}}' -Uri http://localhost:5001/intelligent-lims -UseBasicParsing).Content
```

```
$response = Invoke-WebRequest -Method Post -ContentType "application/json" -Body '{"lims": "labvantage", "action": "getScore", "shouldReport": true, "content": {"sdcid": "Batch", "labels": ["sdclabel11384", "sdclabel23084", "sdclabel29481"], "data": [[20948, 28, 1838, 4082], [422, 2434, 21, 144], [249, 2928, 82, 18171]]}}' -Uri http://3.214.69.84:5004/intelligent-lims -UseBasicParsing
$response.Content
```

```
$response = Invoke-WebRequest -Method Post -ContentType "application/json" -Body '{"lims": "labvantage", "action": "lookupTransaction", "shouldReport": true, "content": {"transaction_id": "59fada2f-958a-4313-8337-e0222e5eedab"}}' -Uri http://3.214.69.84:5004/intelligent-lims -UseBasicParsing
$response.Content
```

curl -X POST -H "Content-Type: application/json" -d '{"lims": "labvantage", "action": "lookupTransaction", "shouldReport": true, "content": {"transaction_id": "59fada2f-958a-4313-8337-e0222e5eedab"}}' http://3.214.69.84:5004/intelligent-lims

Rules:

- Always use Python for our true backend services (like the genie
  microservices). Reasoning: It is easy to get lost in the sauce, because of
  this java should only be used for front end, and python should be used for
  backend.

- Always use toml configuration files. json should be used specifically within
  the code itself, but all external configuration should be done via toml
  Reasoning: json is messy, toml is easier to modify, and json is more
  specifically for web transactions.

- We use python because of its easy support of virtual environments and its
  ubiquity

- all variables in snake_case, all classes in PascalCase, and all functions in
  camelCase. Constants in ALL_CAPS.

- abstract classes in python will end with ABC, for abstract base class, e.g.
  AutomobileABC.

- all functions should have full definitions, that is, their definition
  attributes should include the relevant types, and returns should be typed
  as well.

- All functions that elicit an exception should document as such with a
  docquote, e.g. """Raises: ExceptionThatCouldHappen"""
```

