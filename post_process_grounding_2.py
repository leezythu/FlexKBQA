import json,os
data = json.load(open("sparql_for_prompts.json"))
intermediate_dir = "intermediate_results"
out_dir = "results"
def process(data,i):
    d = data[i]["Parses"][0]
    masked_query = d["masked_query"]
    print(masked_query)
    inter_file = os.path.join(intermediate_dir,str(i)+"_valid_expansions_w_ent_name.json")
    out_file = open(os.path.join(out_dir,str(i)+"_valid_expansions.json"),'w')
    inter_data = json.load(open(inter_file))
    out_data = []
    for d in inter_data:
        new_query = masked_query
        for key in d:
            new_query = new_query.replace(key,d[key])
        print(new_query)
        out_data.append(new_query)
    out_file.write(json.dumps(out_data))
for i in range(0,5):
    process(data,i)