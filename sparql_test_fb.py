from SPARQLWrapper import SPARQLWrapper, JSON

SPARQLPATH = "http://localhost:3001/sparql"

def test():
    sparql = SPARQLWrapper(SPARQLPATH)
    # s =  """
    # PREFIX ns: <http://rdf.freebase.com/ns/>\nSELECT DISTINCT ?x\nWHERE {\nFILTER (?x != ns:m.0gdm1 )\nFILTER (!isLiteral(?x) OR lang(?x) = '' OR langMatches(lang(?x), 'en'))\nns:m.0gdm1 ns:fictional_universe.school_in_fiction.students_graduates ?x .\n?x ns:fictional_universe.fictional_character.gender ns:m.05zppz .\n}\n
    # """
    s =  """
    PREFIX ns: <http://rdf.freebase.com/ns/>\nSELECT DISTINCT ?x\nWHERE { ns:m.07dn1 ns:type.object.name ?x .\n}\n
    """
  #   s = """
  # PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX : <http://rdf.freebase.com/ns/> \nSELECT (?x0 AS ?value) WHERE {\nSELECT DISTINCT ?x0  WHERE { \n?x0 :type.object.type :people.profession . \nVALUES ?x1 { :m.03gfw_m } \n?x0 :broadcast.genre.content ?x1 . \nFILTER ( ?x0 != ?x1  )\n}\n}
  #   """
    sparql.setQuery(s)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    print(results)

if __name__ == '__main__':
    test()