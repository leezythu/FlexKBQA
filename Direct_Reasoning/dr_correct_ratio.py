import json

data = json.load(open("../dr_results_50_shot/dr_res_kqa"))
print(len(data))
correct_num = 0
for key in data:
    d = data[key]
    generations = d["generations"]
    golden_answer = d["ori_data_item"]["answer"]
    if generations == golden_answer:
        correct_num += 1
        
print(correct_num)