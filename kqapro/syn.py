import json
from SPARQLWrapper import SPARQLWrapper, JSON
import random

SPARQLPATH = "http://localhost:8890/sparql"
def execute_sparql(s):
    sparql = SPARQLWrapper(SPARQLPATH)
    sparql.setQuery(s)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def gen_uttrance(tem,res,vars):
    for key in vars:
        if key in res:
            tem = tem.replace(key,res[key]["value"].replace("_"," "))
    # print("tem:",tem)
    # exit(0)
    # assert not "?" in tem
    return tem
    # sample = []
    # for item in tem.split():
    #     if item.startswith("<") and item.endswith(">"):
    #         continue
    #     sample.append(item)
    # return " ".join(sample)

tems = json.load(open("sparql_templates.json"))
print(len(tems))
syn_res = {}
for i in range(188,len(tems)):
    print(i)
    tem = tems[i]
    uttrances = []
    print(tem)
    res = execute_sparql(tem["tem_executed"])
    # results = random.sample(res["results"]["bindings"],1000)
    results = res["results"]["bindings"]
    # print("result:",results)
    for result in results:
        uttrance = {}
        uttrance["question"] = gen_uttrance(tem["tem"],result,tem["vars"])
        uttrance["binding"] = result
        uttrances.append(uttrance)
    with open("syn_res/{}.json".format(i),'w') as f:
        f.write(json.dumps(uttrances))
    # break
