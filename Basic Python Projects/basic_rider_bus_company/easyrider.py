import itertools
import json

data_dict = json.loads(input())
bus_info = {}
stops = []

for line in data_dict:
        bus_info.setdefault(line['stop_type'], [])
            bus_info[line['stop_type']].append(line['stop_name'])

for item in set(itertools.chain(*bus_info.values())):
    if list(itertools.chain(*bus_info.values())).count(item) > 1:
        stops.append(item)

print("On demand stops test:")
results = set(bus_info.get("O", [])) & set(
        itertools.chain(
            bus_info.get("S", []),
            bus_info.get("F", []),
            bus_info.get("", []),
            stops,
        )
                                                    )
print("Wrong stop type:", sorted(results)) if results else print("OK")

