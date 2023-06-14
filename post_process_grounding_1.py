from gettext import bindtextdomain
import json,os
from SPARQLWrapper import SPARQLWrapper, JSON
ori_sparql = """ PREFIX ns: <http://rdf.freebase.com/ns/>
SELECT DISTINCT ?x WHERE { 
    FILTER(langMatches(lang(?x), 'en'))
    entity_name ns:type.object.name ?x. 
}
"""
SPARQLPATH = "http://localhost:3001/sparql"
sparql = SPARQLWrapper(SPARQLPATH)

intermediate_dir = "intermediate_results_grail"
def process(i):
    inter_file = os.path.join(intermediate_dir,str(i)+"_valid_expansions.json")
    inter_data = json.load(open(inter_file))
    existing_ents = [] #avoid duplicating 
    existing_rels = []
    final_data = []
    for d in inter_data:
        flag = True
        for key in d:
            if "rel" in key:
                if d[key] in existing_rels:
                    flag = False
                    break
                existing_rels.append(d[key])
                d[key] = {"id":d[key],"name":"ns:"+d[key].split("/")[-1]}
            if "ent" in key:
                if "rdf.freebase.com" in d[key]:
                    d[key] = "ns:"+d[key].split("/")[-1]
                elif key=="?ent0":
                    d[key] = d[key] if "ns:" in d[key] else "ns"+d[key]
                new_sparql = ori_sparql.replace("entity_name",d[key])
                print(new_sparql)
                sparql.setQuery(new_sparql)
                sparql.setReturnFormat(JSON)
                results = sparql.query().convert()
                bindings = results["results"]["bindings"]
                print(bindings)
                for binding in bindings:
                    if binding["x"]["xml:lang"] == 'en':
                        bind = binding["x"]["value"]
                print(bind)
                if bind in existing_ents:
                    flag = False
                    break
                existing_ents.append(bind)
                d[key] = {"id":d[key],"name":bind}
        if flag:
            final_data.append(d)
        # exit(0)
    with open(os.path.join(intermediate_dir,str(i)+"_valid_expansions_w_ent_name.json"),'w') as f:
        f.write(json.dumps(final_data))
        
for i in range(13,14):
    process(i)