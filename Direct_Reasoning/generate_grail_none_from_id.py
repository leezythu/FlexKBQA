import json
ids = json.load(open("not_cover_id_test_zero_shot.json"))
ori_data = json.load(open("../GrailQA_v1.0/grailqa_v1.0_test_public.json"))
print(len(ids))
filtered_data = []
for d in ori_data:
    if d["qid"] in ids:
        filtered_data.append(d)
with open("grail_test_with_no_answer_zero_shot.json",'w') as f:
    f.write(json.dumps(filtered_data))