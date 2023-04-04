import json
import random

def load_json(fname):
    with open(fname) as f:
        return json.load(f)

def dump_json(obj, fname, indent=None):
    with open(fname, 'w') as f:
        return json.dump(obj, f, indent=indent)

# 指定原文件路径
validex_0 = load_json("0_valid_expansions.json")
validex_1 = load_json("1_valid_expansions.json")
validex_2 = load_json("2_valid_expansions.json")
validex_3 = load_json("3_valid_expansions.json")
validex_4 = load_json("4_valid_expansions.json")

result_list = []
count = 0
content_count = -1
for content in [validex_0, validex_1, validex_2, validex_3, validex_4]:
    content_count += 1
    count = 0
    for k,v in content.items():
        sample = {}
        sample["QuestionId"] = str(content_count) + "_" + str(count)
        sample["RawQuestion"] = v["generations"][0][0]
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
dump_json(result_list,"result.json")
