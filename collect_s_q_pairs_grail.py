import json
src_path = open("GrailQA_v1.0/grailqa_v1.0_train.json")
data = json.load(src_path)
print(len(data))

out_f = open("s_q_pairs_grail_train.txt",'w')

existing_structure = []
existing_structure_cnt = {}
sparql_tems = []
out_f.write("Convert the s-expressions to natural language questions.\n\n")
#统计
for d in data:
    # print(d)
    processed_question = d["question"]+"?"
    sexpr = d["s_expression"]
    mid2entity = {}
    nodes = d["graph_query"]["nodes"]
    for node in nodes:
        if node["node_type"] == "entity":
            mid2entity[node["id"]] = node["friendly_name"]
    for mid in mid2entity:
        sexpr = sexpr.replace(mid,mid2entity[mid])
    s = sexpr.split()
    structure = []
    for item in s:
        if item in ['(JOIN','(R','(AND','(ARGMAX','(ARGMIN','(COUNT',"(le","(lt","(gt","(ge"]:
        # if item in ['(JOIN','(R','(AND','(ARGMAX','(ARGMIN','(COUNT']:
        # if item in ['(JOIN','(R','(AND','(COUNT']:
            structure.append(item)
    structure = " ".join(structure)
    if structure not in existing_structure:
        existing_structure_cnt[structure] = 0
        # print(structure)
        # print("question:",processed_question)
        existing_structure.append(structure)
    existing_structure_cnt[structure] += 1
print(existing_structure_cnt)

filtered_structure = []
for key in existing_structure_cnt:
    if existing_structure_cnt[key] > 97:
        filtered_structure.append(key)

# print("filtered_structure",filtered_structure)
print(len(filtered_structure))
#筛选
existing_structure = []
for d in data:
    # print(d)
    processed_question = d["question"]+"?"
    sexpr = d["s_expression"]
    mid2entity = {}
    nodes = d["graph_query"]["nodes"]
    for node in nodes:
        if node["node_type"] == "entity":
            mid2entity[node["id"]] = node["friendly_name"]
    for mid in mid2entity:
        sexpr = sexpr.replace(mid,mid2entity[mid])
    s = sexpr.split()
    structure = []
    for item in s:
        if item in ['(JOIN','(R','(AND','(ARGMAX','(ARGMIN','(COUNT',"(le","(lt","(gt","(ge"]:
        # if item in ['(JOIN','(R','(AND','(ARGMAX','(ARGMIN','(COUNT']:
        # if item in ['(JOIN','(R','(AND','(COUNT']:
            structure.append(item)
    structure = " ".join(structure)
    if structure not in existing_structure and structure in filtered_structure:
        out_f.write("s-expression:"+sexpr+"\n")
        out_f.write("question:"+processed_question+"\n\n")
        existing_structure.append(structure)
        sparql_tems.append(d)

with open("sparql_for_prompts_sparql.json",'w') as f:
    f.write(json.dumps(sparql_tems))
