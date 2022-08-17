import json

def create_tadabase_insert_payload(fullpath: str, data: dict) -> dict:
    # Note that if you're using setuptools, you should probably use its package resources API instead.
    with open(fullpath) as fp:
        fields = json.load(fp)
    payload = {}
    for k, v in data.items():
        payload[fields[k]] = v
    return payload
