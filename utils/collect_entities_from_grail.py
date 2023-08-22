import json

data = json.load(open("GrailQA_v1.0/grailqa_v1.0_train.json"))
entities = []
for d in data:
    nodes = d["graph_query"]["nodes"]
    for node in nodes:
        if node["node_type"] == "entity":
            entities.append([node["id"],node["friendly_name"]])
print(len(entities))
with open("grail_entities.json",'w') as f:
    f.write(json.dumps(entities))