
import json
f = open("dr_prompt_for_grail.txt",'w')
ori_train_data = json.load(open("../GrailQA_v1.0/grailqa_v1.0_train.json"))
for ori_data in ori_train_data[:50]:
    f.write("question:"+ori_data["question"]+'\n')
    answers = [a["entity_name"] if "entity_name" in a else a["answer_argument"] for a in ori_data["answer"]]
    answers = ",".join(answers)
    f.write("answer:"+answers+"\n\n")