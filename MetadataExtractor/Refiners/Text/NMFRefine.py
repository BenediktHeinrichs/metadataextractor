from rdflib.graph import Graph, ConjunctiveGraph
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
from sklearn.decomposition import NMF
import numpy as np
from scipy.optimize import curve_fit
import math
import logging

log = logging.getLogger(__name__)

import visualizationNMF as vis

from ..Interfaces.IRefine import IRefine


class NMFRefine(IRefine):
    def __init__(self, config):
        IRefine.__init__(self, config)
        self.__numberOfComponents = 100

    def refine_metadata(
        self, metadata, fileInfo=None, metadataformat="trig", plottingGraph=False
    ):

        # TODO: Read https://ebiquity.umbc.edu/_file_directory_/papers/771.pdf for better understanding

        if metadata != None:

            log.info("Refining Metadata using NMF.")

            g = ConjunctiveGraph()
            result = g.parse(data=metadata, format=metadataformat)
            G = rdflib_to_networkx_multidigraph(result)

            matrix = nx.adjacency_matrix(G)

            model = NMF(
                n_components=self.__numberOfComponents, init="random", random_state=0
            )

            W = model.fit_transform(matrix)
            H = model.components_

            # Crisp communities
            threshold = 0.01
            for i in range(len(W)):
                for j in range(len(W[i])):
                    if W[i, j] < threshold:
                        W[i, j] = 0

            candidateSet = []

            labels, nfeat, efeat = [], [], []

            nodeNameCollection = []
            for node in G.nodes():
                # if("http://pikes.fbk.eu/#char=" in node):
                # nodeNameCollection.append(charToString[node])
                nodeNameCollection.append(node)

            for i in range(self.__numberOfComponents):
                nodes = []

                Wt = []
                Ht = []
                for j in range(len(W)):
                    if W[j, i] != 0:
                        nodes.append(nodeNameCollection[j])
                        Wt.append(W[j, i])
                        Ht.append(H[i, j])

                subGraph = np.reshape(np.array(Wt), (len(Wt), 1))
                computed = subGraph.T * np.reshape(np.array(Ht), (len(Ht), 1))
                ComputedG = nx.from_numpy_matrix(computed)
                nodeCount = len(ComputedG.nodes())
                edgeCount = len(ComputedG.edges())

                if nodeCount >= 3:
                    if edgeCount >= nodeCount - 1:
                        candidateSet.append(i)
                        nfeat.append(nodeCount)
                        efeat.append(edgeCount)
                labels.append(nodes)

            def func(x, a, b):
                fc = a * (np.array(x).astype(float) ** b)
                return fc

            popt, pcov = curve_fit(func, nfeat, efeat, maxfev=20000)
            plot_nfeat = sorted(nfeat)

            fitline = func(plot_nfeat, *popt)

            # Now give anomaly scores
            outlines = {}
            for count in range(len(candidateSet)):
                subGraph = candidateSet[count]
                ncount = nfeat[count]
                ecount = efeat[count]

                if ecount != 0:
                    efit = func(ncount, *popt)
                    outlines[subGraph] = (
                        max(ecount, efit) / min(ecount, efit)
                    ) * math.log(abs(ecount - efit) + 1)
                else:
                    outlines[subGraph] = 0

            anomaly_scores = sorted(outlines.items(), key=lambda x: x[1])
            anomalies = []
            for anomaly in anomaly_scores[::-1][:10]:
                anomalies.append(anomaly[0])

            outputfilename = "test.txt"
            outputfile = open(outputfilename, "w")

            for i in range(len(anomaly_scores[::-1])):
                subGraphNumber = anomaly_scores[::-1][i][0]

                Wt = []
                Ht = []
                for j in range(len(W)):
                    if W[j, subGraphNumber] != 0:
                        Wt.append(W[j, subGraphNumber])
                        Ht.append(H[subGraphNumber, j])

                subGraph = np.reshape(np.array(Wt), (len(Wt), 1))
                computed = subGraph.T * np.reshape(np.array(Ht), (len(Ht), 1))
                ComputedG = nx.from_numpy_matrix(computed)
                print("Nodes: " + str(len(ComputedG.nodes())))
                print("Edges: " + str(len(ComputedG.edges())))

                print(len(labels[subGraphNumber]))
                print(labels[subGraphNumber])
                outputfile.write("{}\n".format(labels[subGraphNumber]))

            outputfile.close()

            vis.plot_oddball_features(
                nfeat, efeat, plot_nfeat, fitline, labels, anomalies
            )
        return (metadata, metadataformat)
