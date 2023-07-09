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

data = json.load(open("./llm_kqa"))
new_data = {}
for key in data.keys():
    d = data[key]
    # print(d)
    if "\"arg" in  d["generations"] or " arg" in d["ori_data_item"]["question"]:
        continue
    #初版产生的时候没有给pred:name之后的entity加上引号
    sparql = d["ori_data_item"]["sparql"]
    print(sparql)
    res = execute_sparql(sparql)
    print(res)
    exit(0)
    new_data[key] = d
with open("./llm_kqa_filtered.json",'w') as f:
    f.write(json.dumps(new_data))