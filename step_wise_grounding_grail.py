from dataclasses import replace
from html import entities
from SPARQLWrapper import SPARQLWrapper, JSON
import json
import random

SPARQLPATH = "http://localhost:3001/sparql"
sparql = SPARQLWrapper(SPARQLPATH)

def filter_valid_entities(results):
    valid_results = []
    bindings = results["results"]["bindings"]
    for bind in bindings:
        flag = True
        for key in bind:
            if not bind[key]["value"].split("/")[-1].startswith("m."):
                flag = False
        if flag:
            valid_results.append(bind)
    return valid_results

def filter_valid_rels(results):
    valid_results = []
    bindings = results["results"]["bindings"]
    for bind in bindings:
        flag = True
        for key in bind:
            rel = bind[key]["value"].split("/")[-1]
            if not "ns" in bind[key]["value"].split("/") or "freebase" in rel or "common" in rel or "type" in rel or "rdf" in rel or "base" in rel or "_id" in rel or ".uri" in rel:
                flag = False
        if flag:
            valid_results.append(bind)
    return valid_results

def filter_valid_rets(results):
    # if results["head"]["vars"][0].startswith("rel"):
    return filter_valid_rels(results)
    # else :
    #     return filter_valid_entities(results)

def ground(data,i):
    d = data[i]
    valid_entities = json.load(open("grail_entities.json"))
    # entities = random.sample(valid_entities,10000)
    entities = valid_entities
    valid_expansions = []
    for e in entities:
        step_wise_querys = d["step_wise_queries"]
        replace_info = {}
        replace_info["?ent0"] = ":"+e[0]
        for query in step_wise_querys:
            for key in replace_info:
                if not key.startswith("?ent0"):
                    query = query.replace("?"+key,":"+replace_info[key].split("/")[-1])
                else:
                    query = query.replace(key,replace_info[key])
            # print(query)
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
        # print(results)
            valid_rets = filter_valid_rets(results)
            # print(valid_rets)
            if len(valid_rets)==0:
                replace_info = {}
                break
            # valid_ret = valid_rets[0]
            valid_ret = random.choice(valid_rets)
            for key in valid_ret:
                replace_info[key] = valid_ret[key]["value"]
        if replace_info!={}:
            valid_expansions.append(replace_info)
    with open("intermediate_results_grail/"+str(i)+"_valid_expansions.json",'w') as f:
        f.write(json.dumps(valid_expansions))
    # exit(0)

if __name__ == '__main__':
    data = json.load(open("sparql_for_prompts_grail.json"))
    for i in range(len(data)):
        ground(data,i)
        break