import json
input_path = "webqsp_881_samples.json"
out_path = "webqsp_881_samples_to_llm.json"

data = json.load(open(input_path))
new_data = []
print(len(data))
for d in data:
    new_d = {}
    new_d["QuestionId"] = d["QuestionId"] 
    new_d["TopicEntityMid"] = d["Parses"][0]["TopicEntityMid"]
    if new_d["TopicEntityMid"] == None:
        continue
    mid2name = {}
    mid2name[new_d["TopicEntityMid"]] = d["Parses"][0]["TopicEntityName"]
    for con in d["Parses"][0]["Constraints"]:
        if con["Argument"].startswith("m."):
            mid2name[con["Argument"]] = con["EntityName"]
    new_d["mid2name"] = mid2name
    new_d["SExpr"] = d["Parses"][0]["SExpr"]
    new_d["SExpr_w_name"] = new_d["SExpr"]
    for mid in mid2name:
        new_d["SExpr_w_name"] = new_d["SExpr_w_name"].replace(mid,mid2name[mid])
    new_data.append(new_d)

with open(out_path,'w') as f:
    f.write(json.dumps(new_data))