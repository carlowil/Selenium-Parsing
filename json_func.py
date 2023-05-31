import dataclasses
import json


def serialize_json(items, data_name):
    for i in range(len(items)):
        items[i] = dataclasses.asdict(items[i])
    with open(f"{data_name}.json", "w", encoding="utf-8") as write_file:
        json_string = json.dumps(items)
        write_file.write(json_string)
