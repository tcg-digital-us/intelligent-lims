# intelligent-lims microservice

The purpose of this microservice is to handle the 'lims' attribute accordingly,
forwarding the package to the lv-handler for further evalutation.

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
$(Invoke-WebRequest -Method Post -ContentType "application/json" -Body '{"lims": "labvantage", "action": "getScore", "shouldReport": true, "content": {"sdcid": "Batch", "labels": ["sdclabel184", "sdclabel284", "sdclabel281"], "data": [[44, 28, 1838, 4082], [10, 221, 213, 22], [249, 2928, 82, 18171]]}}' -Uri http://localhost:5001/intelligent-lims -UseBasicParsing).Content
```