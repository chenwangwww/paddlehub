import rdflib

root_uri = 'http://www.example.org/'
g = rdflib.Graph()
has_border_with = rdflib.URIRef(root_uri + 'has_border_with')
located_in = rdflib.URIRef(root_uri + 'located_in')

germany = rdflib.URIRef(root_uri + 'country1')
france = rdflib.URIRef(root_uri + 'country2')
china = rdflib.URIRef(root_uri + 'country3')
mongolia = rdflib.URIRef(root_uri + 'country4')

europa = rdflib.URIRef(root_uri + 'part1')
asia = rdflib.URIRef(root_uri + 'part2')

g.add((germany, has_border_with, france))
g.add((china, has_border_with, mongolia))
g.add((germany, located_in, europa))
g.add((france, located_in, europa))
g.add((china, located_in, asia))
g.add((mongolia, located_in, asia))

# q = "select ?country where { ?country <" + root_uri + "located_in> " + root_uri + "part1> }"
q = "select ?country where { ?country <http://www.example.org/located_in> <http://www.example.org/part1> }"
x = g.query(q)
# print(list(x))
g.serialize("graph.rdf")
g1 = rdflib.Graph()
g1.parse("graph.rdf", format="xml")
x1 = g1.query(q)
print(list(x1))