import json,os
data = json.load(open("sparql_for_prompts_grail.json"))

intermediate_dir = "intermediate_results_grail"
out_dir = "results_grail/sparql"

def process(data,i):
    # d = data[i]["Parses"][0]["masked_query"] #for webqsp
    masked_query = data[i]["masked_query"]#for grail
    ori_sexpr = data[i]["s_expression"]
    print(masked_query)
    inter_file = os.path.join(intermediate_dir,str(i)+"_valid_expansions_w_ent_name.json")
    out_file = open(os.path.join(out_dir,str(i)+"_valid_expansions.json"),'w')
    inter_data = json.load(open(inter_file))
    out_data = []
    for d in inter_data:
        # new_query = masked_query
        mid2name = {}
        query = masked_query
        for key in d:
            full_key = key
            if not key.startswith("?"):
                full_key = "?"+key
            # new_query = new_query.replace(full_key,d[key]["name"])
            if "ent" in key:
                query = query.replace(full_key,d[key]["id"].split("ns")[1])
                mid2name[d[key]["id"]] = d[key]["name"]
            else:
                query = query.replace(full_key,d[key]["name"].split("ns")[1])
        # print(new_query)
        out_data.append({"sparql":query,"TopicEntityMid":d["?ent0"]["id"],"mid2name":mid2name,"ori_sexpr":ori_sexpr,"vars":d})
    out_file.write(json.dumps(out_data))

for i in range(0,6):
    process(data,i)