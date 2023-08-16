# import json
# dr_data = json.load(open("../dr_results_50_shot/dr_res_kqa_test"))
# ori_data = json.load(open("/home/lzy/data/kgqa/KQAPro_Baselines/dataset/test.json"))
# questions = [d["question"] for d in ori_data]
# predict_data = open("/home/lzy/data/kgqa/KQAPro_Baselines/logs_sparql_predict_reproduce_st_iter2/predict.txt").readlines()
# assert len(predict_data) == len(questions)
# print(questions[0])
# question2answer = {}
# for key in dr_data:
#     question = dr_data[key]["ori_data_item"]["question"]
#     answer = dr_data[key]["generations"]
#     question2answer[question] = answer
# for q in question2answer:
#     ind = questions.index(q)
#     predict_data[ind] = question2answer[q]+"\n"
# with open("predict_kqa_test+dr.txt",'w') as f:
#     for ans in predict_data:
#         f.write(ans)

#if none, replace it
import json
dr_data = json.load(open("../dr_results_50_shot/dr_res_kqa_test"))
ori_data = json.load(open("/home/lzy/data/kgqa/KQAPro_Baselines/dataset/test.json"))
questions = [d["question"] for d in ori_data]
predict_data = open("/home/lzy/data/kgqa/KQAPro_Baselines/logs_sparql_predict_reproduce_st_iter2/predict.txt").readlines()
assert len(predict_data) == len(questions)
print(questions[0])
question2answer = {}
for key in dr_data:
    question = dr_data[key]["ori_data_item"]["question"]
    answer = dr_data[key]["generations"]
    question2answer[question] = answer
for q in question2answer:
    ind = questions.index(q)
    predict_data[ind] = question2answer[q]+"\n"
with open("predict_kqa_test+dr.txt",'w') as f:
    for ans in predict_data:
        f.write(ans)