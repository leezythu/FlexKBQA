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
            if not "ns" in bind[key]["value"].split("/") or "freebase" in rel or "common" in rel or "type" in rel or "rdf" in rel :
                flag = False
        if flag:
            valid_results.append(bind)
    return valid_results

def ground(data,i):
    d = data[i]["Parses"][0]
    # s = d["Sparql_Tem_First_Stage"]
#     s = """
# PREFIX ns: <http://rdf.freebase.com/ns/>
# SELECT DISTINCT ?rel0
# WHERE {
# FILTER (?x != ns:m.0glnq6z)
# FILTER (!isLiteral(?x) OR lang(?x) = '' OR langMatches(lang(?x), 'en'))
# ns:m.0glnq6z ?rel0 ?x .
# }
    # """
    # print(s)
    # exit(0)
    # sparql.setQuery(s)
    # sparql.setReturnFormat(JSON)
    # results = sparql.query().convert()
    # print(results)
    # exit(0)
    # valid_entities = filter_valid_entities(results)
    # with open(str(i)+"_first_stage_results.json",'w') as f:
    #     f.write(json.dumps(valid_entities))

    valid_entities = json.load(open("grail_entities.json"))
    entities = random.sample(valid_entities,100)
    valid_expansions = []
    for e in entities:
        second_query = d["Sparql_Tem_Second_Stage"]
        # for key in e:
        second_query = second_query.replace("?ent0","ns:"+e[0])
        print(second_query)
        sparql.setQuery(second_query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        # print(results)
        valid_rels = filter_valid_rels(results)
        print(valid_rels)
        exit(0)
        if len(valid_rels) == 0:
            continue
        valid_expansion = valid_rels[0]
        valid_expansion["ent0"] = {"mid":e[0],"friendly name":e[1]}
        # print(valid_expansion)
        valid_expansions.append(valid_expansion)
    with open(str(i)+"_valid_expansions.json",'w') as f:
        f.write(json.dumps(valid_expansions))
    exit(0)


# def ground(data,i):
#     d = data[i]["Parses"][0]
#     # s = d["Sparql_Tem_Second_Stage"]
#     s = """
# PREFIX ns: <http://rdf.freebase.com/ns/>
# SELECT DISTINCT ?rel0
# WHERE {
#     FILTER (?x != ?ent0)
#     FILTER (!isLiteral(?x) OR lang(?x) = '' OR langMatches(lang(?x), 'en'))
#     ?ent0 ?rel0 ?x .\n}\n
#     """
#     print(s)
#     sparql.setQuery(s)
#     sparql.setReturnFormat(JSON)
#     results = sparql.query().convert()
#     print(results)
#     valid_rels = filter_valid_rels(results)
#     print(valid_rels)
#     exit(0)
#     with open(str(i)+"_first_stage_results.json",'w') as f:
#         f.write(json.dumps(valid_entities))
#     entities = random.sample(valid_entities,1000)
#     for e in entities:
#         second_query = d["Sparql_Tem_Second_Stage"]
#         for key in e:
#             second_query = second_query.replace("?"+key,"ns:"+e[key]["value"].split('/')[-1])
#         print(second_query)
#         exit(0)
#         sparql.setQuery(second_query)
#         sparql.setReturnFormat(JSON)
#         results = sparql.query().convert()
#         print(results)
#         valid_rels = filter_valid_rels(results)
#         print(valid_rels)
#         # exit(0)
#         # with open(str(i)+"_second_stage_results.json",'w') as f:
#         #     f.write(json.dumps())
#     exit(0)

if __name__ == '__main__':
    data = json.load(open("sparql_for_prompts.json"))
    for i in range(1,len(data)):
        ground(data,i)
    # for d in data:
    # d = data[0]
    # ground(d)
        # exit(0)