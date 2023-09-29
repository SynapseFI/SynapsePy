import json

def json_serialize(obj):
    if obj is None:
        pass  # No obj, don’t serialize.
    elif isinstance(obj, str):
        try:
            _ = json.loads(obj)  # All good, a valid JSON string.
        except json.decoder.JSONDecodeError as e:
            raise ValueError("obj is not a valid JSON string") from e
    else:
        try:
            obj = json.dumps(obj)  # All good, a JSON serializable object.
        except TypeError as e:
            raise ValueError("obj is not JSON serializable") from e
