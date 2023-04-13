import jsonschema
from jsonschema import validate

class PayloadValidationError(Exception):
    pass

class PayloadValidator:
    schema = {
        "type": "object",
        "properties": {
            "action": {"type": "string"},
            "content": {
                "type": "object",
                "properties": {},
                "additionalProperties": True
            }
        },
        "additionalProperties": False,
        "required": ["action", "content"]
    }

    @classmethod
    def validate_payload(cls, payload: dict) -> dict:
        try:
            validate(instance=payload, schema=cls.schema)
            return payload
        except jsonschema.exceptions.ValidationError as e:
            raise PayloadValidationError(str(e))
