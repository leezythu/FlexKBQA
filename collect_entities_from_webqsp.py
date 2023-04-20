import json

def add_entity(entities,mid,name):
    if [mid] not in entities and mid!=None:
        entities.append([mid])

src_path = "WebQSP/data/WebQSP.train.json"
data = json.load(open(src_path))
questions = data["Questions"]
print(len(questions))
entities = []
for q in questions:
    parses = q["Parses"]
    for parse in parses:
        add_entity(entities,parse["TopicEntityMid"],parse["TopicEntityName"])
        for con in parse["Constraints"]:
            if con["ArgumentType"]== "Entity":
                add_entity(entities,con["Argument"],con["EntityName"])
print(len(entities))
with open("webqsp_entities.json",'w') as f:
    f.write(json.dumps(entities))