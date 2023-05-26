import json
import struct
src_path = open("rng-kbqa/outputs/WebQSP.pdev.expr.json")
data = json.load(src_path)
print(len(data))

out_f = open("s_q_pairs_dev.txt",'w')
existing_structure = []
out_f.write("Convert the s-expressions to natural language questions.\n\n")
for d in data:
    # print(d)
    processed_question = d["ProcessedQuestion"]+"?"
    # assert len(d["Parses"])==1
    parse = d["Parses"][0]
    s = parse["SExpr"]
    if s == "null":
        continue
    mid2entity = {}
    TopicEntityMid = parse["TopicEntityMid"]
    TopicEntityName = parse["TopicEntityName"]
    mid2entity[TopicEntityMid] = TopicEntityName
    constraints = parse["Constraints"]
    for con in constraints:
        if con["Argument"].startswith("m."):
            mid2entity[con["Argument"]] = con["EntityName"]
    for mid in mid2entity:
        s = s.replace(mid,mid2entity[mid])
    out_f.write("s-expression:"+s+"\n")
    out_f.write("question:"+processed_question+"\n\n")
    s = s.split()
    structure = []
    for item in s:
        if item in ['(JOIN','(R','(AND','(ARGMAX','(ARGMIN']:
            structure.append(item)
    structure = " ".join(structure)
    if structure not in existing_structure:
        print(structure)
        print("question:",processed_question)
        existing_structure.append(structure)
