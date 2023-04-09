import json
import random

def load_json(fname):
    with open(fname) as f:
        return json.load(f)

def dump_json(obj, fname, indent=None):
    with open(fname, 'w') as f:
        return json.dump(obj, f, indent=indent)

# 指定原文件路径
validex_0 = load_json("llm_results/0_valid_expansions.json")
validex_1 = load_json("llm_results/1_valid_expansions.json")
validex_2 = load_json("llm_results/2_valid_expansions.json")
validex_3 = load_json("llm_results/3_valid_expansions.json")
validex_4 = load_json("llm_results/4_valid_expansions.json")
validex_5 = load_json("llm_results_turbo/5_valid_expansions.json")
validex_6 = load_json("llm_results_turbo/6_valid_expansions.json")
validex_7 = load_json("llm_results_turbo/7_valid_expansions.json")
validex_8 = load_json("llm_results_turbo/8_valid_expansions.json")
validex_9 = load_json("llm_results_turbo/9_valid_expansions.json")
validex_10 = load_json("llm_results_turbo/10_valid_expansions.json")
validex_11 = load_json("llm_results_turbo/11_valid_expansions.json")
validex_16 = load_json("llm_results_turbo/16_valid_expansions.json")
validex_22 = load_json("llm_results_turbo/22_valid_expansions.json")

result_list = []
count = 0
content_count = -1
for content in [validex_0, validex_1, validex_2, validex_3, validex_4, validex_5, validex_6, \
                validex_7, validex_8, validex_9, validex_10,validex_11,validex_16,validex_22]:
    content_count += 1
    count = 0
    for k,v in content.items():
        sample = {}
        sample["QuestionId"] = str(content_count) + "_" + str(count)
        if type(v["generations"][0]) == list:
            sample["RawQuestion"] = v["generations"][0][0]
        elif type(v["generations"]) == str:
            sample["RawQuestion"] = v["generations"]
        else:
            raise KeyError
        parse_list = []
        one_parse = {}
        one_parse["TopicEntityMid"] = v["ori_data_item"]["TopicEntityMid"]
        one_parse["TopicEntityName"] = v["ori_data_item"]["mid2name"]["ns:{}".format(one_parse["TopicEntityMid"])]
        one_parse["SExpr"] = v["ori_data_item"]["SExpr"]
        parse_list.append(one_parse)
        sample["Parses"] = parse_list

        result_list.append(sample)
        count += 1

# 对result_list进行shuffle
random.shuffle(result_list)

# 指定输出文件路径
dump_json(result_list,"llm_results_to_rng_kbqa/result.json")
