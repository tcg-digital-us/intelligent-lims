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