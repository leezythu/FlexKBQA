import json
src_data = json.load(open("llm_results_turbo_kqa_from_ent/llm_kqa_5000"))

print(len(src_data))
tgt_data = []
for key in src_data:
    generation = src_data[key]["generations"]
    item = src_data[key]["ori_data_item"]
    item["question"] = generation
    print(item)
    if "fact_h" in generation or " fact " in generation:
        continue
    tgt_data.append(item)

with open("kqapro/kqa_for_train.json",'w') as f:
    f.write(json.dumps(tgt_data))