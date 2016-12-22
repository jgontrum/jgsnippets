import json
import pprint as ppprint


def jprint(text: str):
    print(json.dumps(text, indent=2))


def pprint(obj):
    ppprint.pprint(obj)