import json
from re import S
from SPARQLWrapper import SPARQLWrapper, JSON
SPARQLPATH = "http://localhost:3001/sparql"
sparql = SPARQLWrapper(SPARQLPATH)

def find_mids(exprs):
    mids = []
    for expr in exprs:
        if expr.startswith("m.") or expr.startswith("g."):
            mids.append(expr.strip(")"))
    return mids

def get_name(mid):
    s =  "PREFIX ns: <http://rdf.freebase.com/ns/>\nSELECT DISTINCT ?x\nWHERE { ns:"+mid+" ns:type.object.name ?x .\nFILTER(LANGMATCHES(LANG(?x),\"en\"))}\n"
    sparql.setQuery(s)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    name = results["results"]["bindings"][0]["x"]["value"]
    return name

data = json.load(open("final_grailqa_train_data.json"))
for d in data:
    sexpr = d["s_expression"]
    mids = find_mids(sexpr.split())
    try:
        assert len(mids) > 0 
    except:
        print(sexpr)
        exit(0)
    mid2name = {}
    for mid in mids:
        name = get_name(mid)
        print(name)
        mid2name[mid] = name
    d["mid2name"] = mid2name
    for mid in mids:
        sexpr = sexpr.replace(mid,mid2name[mid])
    d["s_expression"] = sexpr

with open("final_grailqa_train_data_w_ent_name.json",'w') as f:
    f.write(json.dumps(data))

