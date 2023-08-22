from SPARQLWrapper import SPARQLWrapper, JSON

SPARQLPATH = "http://localhost:3001/sparql"

def test():
    sparql = SPARQLWrapper(SPARQLPATH)
    s =  """
    PREFIX ns: <http://rdf.freebase.com/ns/>\nSELECT DISTINCT ?x\nWHERE { ns:g.11byb645nh ns:type.object.name ?x .\n}\n
    """
    sparql.setQuery(s)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    print(results)

if __name__ == '__main__':
    test()