from rdflib.graph import Graph, ConjunctiveGraph

import logging

log = logging.getLogger(__name__)

from rdflib import Namespace, URIRef
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import matplotlib.pyplot as plt

from MetadataExtractor.Util import metadataFormatter

from ..Interfaces.IRefine import IRefine

import PikesRefineTest


class PikesRefine(IRefine):
    def refine_metadata(
        self, metadata, fileInfo, metadataformat="trig", plottingGraph=False, skip=True
    ):
        if not skip and metadata and not metadata.isspace():

            if "The request payload size exceeds the max post size limitation" in metadata:
                log.info("Too big for Pikes.")
                return "", metadataformat

            log.info("Refining Pikes Metadata.")

            fact = Namespace(
                "{}ontologies/factgraph/".format(
                    metadataFormatter.getBaseUrl(self._IRefine__config)
                )
            )

            fileIdentifier = metadataFormatter.formatIdentifier(fileInfo["identifier"])

            # ConjunctiveGraph so that multiple contexts can be explored
            # Pikes returns mulitple contexts (e.g. every fact is a graph)
            g = ConjunctiveGraph()
            # Resolve problems with ks:quantity description
            metadata = metadata.replace("..", ".")
            g.parse(data=metadata, format=metadataformat)
            toRemove = []
            for (subject, predicate, obj) in g:
                stringPredicate = str(predicate)
                stringObject = str(obj)
                if (
                    "http://dkm.fbk.eu/ontologies/knowledgestore#mod" != stringPredicate
                    and "http://premon.fbk.eu/resource/" not in stringPredicate
                    and "http://framebase.org/ns/" not in stringPredicate
                    and "http://semanticweb.cs.vu.nl/2009/11/sem/hasActor"
                    != stringPredicate
                    and "http://www.w3.org/2000/01/rdf-schema#seeAlso"
                    != stringPredicate
                    and "http://www.newsreader-project.eu/ontologies/"
                    not in stringObject
                    and "http://dbpedia.org/class/yago/" not in stringObject
                ):
                    toRemove.append((subject, predicate, obj))
            for entry in toRemove:
                g.remove(entry)

            if (
                "Values" in self._IRefine__config
                and "Text" in self._IRefine__config["Values"]
                and "PikesMergeDefinitions" in self._IRefine__config["Values"]["Text"]
                and self._IRefine__config["Values"]["Text"]["PikesMergeDefinitions"]
            ):
                # Remove Pikes giving every word in a new sentence a new id
                toRemove = []
                toAdd = []
                for (subject, predicate, obj) in g:
                    stringSubject = str(subject)
                    stringObject = str(obj)
                    delete = False
                    if (
                        "http://pikes.fbk.eu/#" in stringSubject
                        and "_" in stringSubject
                    ):
                        delete = True
                        stringSubject = stringSubject[: stringSubject.rindex("_")]
                    if "http://pikes.fbk.eu/#" in stringObject and "_" in stringObject:
                        delete = True
                        stringObject = stringObject[: stringObject.rindex("_")]
                    if delete:
                        toRemove.append((subject, predicate, obj))
                        toAdd.append(
                            (URIRef(stringSubject), predicate, URIRef(stringObject))
                        )

                for entry in toRemove:
                    g.remove(entry)
                for entry in toAdd:
                    g.add(entry)

            # Add a fact graph and remove the indiviual fact graphs
            factG = ConjunctiveGraph()
            factIdentifier = fact[fileIdentifier]
            factgraph = factG.get_context(factIdentifier + "/@type=metadata&extracted=true")
            for context in list(g.contexts()):
                if "fact:" in context.identifier and len(context.all_nodes()) > 0:
                    for (subject, predicate, obj) in context:
                        factgraph.add((subject, predicate, obj))

            if plottingGraph:
                self.__plotGraph(factG)

            # Conversion to nquads for speed purposes
            metadataformat = "nquads"
            return (
                factG.serialize(format=metadataformat, base=fact[fileIdentifier], encoding='utf8')
                .decode("utf-8")
                .replace("\xa0", ""),
                metadataformat,
            )
        else:
            return metadata, metadataformat

    def __plotGraph(self, result):

        G = rdflib_to_networkx_multidigraph(result)

        # Plot Networkx instance of RDF Graph
        pos = nx.spring_layout(G, scale=2)
        edge_labels = nx.get_edge_attributes(G, "r")
        nx.draw_networkx_edge_labels(G, pos, labels=edge_labels)
        nx.draw(G, with_labels=True)
        plt.show()


if __name__ == "__main__":

    pikesRefine = PikesRefine({})

    for test in PikesRefineTest.returnData():
        print(
            pikesRefine.refine_metadata(
                test,
                {"identifier": "PikesTest", "file": "NoFile.txt"},
                plottingGraph=True,
            )
        )
