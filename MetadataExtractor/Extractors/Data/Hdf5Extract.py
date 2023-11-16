from .IDataExtract import IDataExtract
import h5py
from h5py import Dataset
from MetadataExtractor.Util import metadataCreation, metadataFormatter
import logging
import numpy

log = logging.getLogger(__name__)


class Hdf5Extract(IDataExtract):
    def extract(self, fileInfo):
        log.info('Extracting text and metadata from hdf5 "' + fileInfo["file"] + '".')
        self.clearDataSetsAndCatalogs()
        text = ""
        metadata = ""
        # TODO: Implement cross link between datasets
        # TODO: Implement automatic metadata schema (ap) detection based on the string predicate and select the most fitting
        with h5py.File(fileInfo["file"], "r") as f:
            self.setDataSetsAndCatalogs(f, fileInfo)
            metadata = self.__catalogMetadata
            dataSets = self.__dataSets
            for dataSet in dataSets:
                metadata += self.getMetadataFromDataSet(fileInfo, dataSet)
        return text, metadata

    def clearDataSetsAndCatalogs(self):
        self.__dataSets = []
        self.__catalogMetadata = ""

    def getMetadataFromDataSet(self, fileInfo, dataSet: "Dataset"):
        # TODO: metadata subject for a dataset has to be different

        shape = dataSet.shape
        dtype = dataSet.dtype
        size = dataSet.size
        # Can be none
        compression = dataSet.compression
        # Can be none
        compression_opts = dataSet.compression_opts
        attributes = dataSet.attrs
        name = dataSet.name
        identifier = name
        graphIdentifier = fileInfo["identifier"] + identifier

        data = dataSet[()]
        average = None
        max = None
        min = None
        try:
            if size > 0 and numpy.issubdtype(data.dtype, numpy.number):
                average = numpy.average(data)
                max = numpy.max(data)
                min = numpy.min(data)
        except ValueError:
            pass

        # map to http://www.qudt.org/doc/2020/07/DOC_SCHEMA-QUDT-v2.1.html
        # http://qudt.org/2.0/schema/qudt/
        # http://www.linkedmodel.org/schema/dtype
        # resolve rdf terms from: https://prefix.zazuko.com/
        ontology = "mex"
        values = [
            {
                "predicate": "rdf:type",
                "object": "http://qudt.org/schema/qudt/Vector",
            },
            {
                "predicate": "rdf:type",
                "object": "http://www.w3.org/ns/dcat#Dataset",
            },
            {"predicate": "dcterms:identifier", "object": identifier},
            {"predicate": "qudt:hasDimension", "object": shape},
            {"predicate": "qudt:dataType", "object": dtype},
            {"predicate": "qudt:length", "object": size},
        ]
        if average is not None:
            values.append(
                {"predicate": "dbo:average", "object": average},
            )
        if max is not None:
            values.append(
                {"predicate": "dbo:max", "object": max},
            )
        if min is not None:
            values.append(
                {"predicate": "dbo:min", "object": min},
            )
        if compression is not None:
            values.append(
                {"predicate": "{}:compression".format(ontology), "object": compression}
            )
        if compression_opts is not None:
            values.append(
                {
                    "predicate": "{}:compression_opts".format(ontology),
                    "object": compression_opts,
                }
            )
        for attribute in attributes.keys():
            objectValue = attributes[attribute]
            if isinstance(objectValue, (numpy.bytes_, bytes)):
                objectValue = objectValue.decode()
            values.append(
                {
                    "predicate": ontology
                    + "attr:"
                    + metadataFormatter.replaceForbiddenValues(attribute),
                    "object": objectValue,
                }
            )

        graphOptions = {
            "additionalPrefixes": [
                "@prefix qudt: <http://qudt.org/schema/qudt/>",
                "@prefix dbo: <http://dbpedia.org/ontology/>",
                "@prefix dcat: <http://www.w3.org/ns/dcat#>",
                "@prefix dcterms: <http://purl.org/dc/terms/>",
            ],
            "identifier": graphIdentifier,
            "ontology": ontology,
            "referencePredicate": "dcterms:hasPart",
            "values": values,
        }

        return metadataCreation.addEntryToFileGraph(
            fileInfo, self._IExtract__config, graphOptions
        )

    def setDataSetsAndCatalogs(self, obj, fileInfo):
        objType = type(obj)
        if objType in [h5py._hl.group.Group, h5py._hl.files.File]:
            self.setCatalogMetadata(obj, fileInfo)
            for key in obj.keys():
                self.setDataSetsAndCatalogs(obj[key], fileInfo)
        elif objType == h5py._hl.dataset.Dataset:
            self.__dataSets.append(obj)

    def setCatalogMetadata(self, obj, fileInfo):
        name = obj.name
        dctidentifier = name
        identifier = fileInfo["identifier"] + dctidentifier
        values = []
        for key in obj.keys():
            keyName = obj[key].name
            keyIdentifier = fileInfo["identifier"] + keyName
            predicate = "http://www.w3.org/ns/dcat#"
            objType = type(obj[key])
            if objType in [h5py._hl.group.Group, h5py._hl.files.File]:
                predicate = predicate + "catalog"
            elif objType == h5py._hl.dataset.Dataset:
                predicate = predicate + "dataset"
            else:
                continue

            values.append(
                {
                    "predicate": predicate,
                    "object": "{}{}".format(
                        metadataFormatter.getFileUrl(self._IExtract__config),
                        metadataFormatter.formatIdentifier(keyIdentifier),
                    ),
                }
            )

        values.append(
            {"predicate": "rdf:type", "object": "http://www.w3.org/ns/dcat#Catalog"}
        )

        attributes = obj.attrs
        for attribute in attributes.keys():
            objectValue = attributes[attribute]
            if isinstance(objectValue, (numpy.bytes_, bytes)):
                objectValue = objectValue.decode()
            values.append(
                {
                    "predicate": "mexattr:"
                    + metadataFormatter.replaceForbiddenValues(attribute),
                    "object": objectValue,
                }
            )

        values.append({"predicate": "dcterms:identifier", "object": dctidentifier})

        self.__catalogMetadata += metadataCreation.addEntryToFileGraph(
            fileInfo,
            self._IExtract__config,
            {
                "additionalPrefixes": [
                    "@prefix dcat: <http://www.w3.org/ns/dcat#>",
                    "@prefix dcterms: <http://purl.org/dc/terms/>",
                ],
                "identifier": identifier,
                "ontology": "mex",
                "values": values,
            },
        )

    def registerMimeTypes(self):
        self.mimeTypes["concrete"] = ["application/x-hdf"]


def setDataSets(listp, obj):
    objType = type(obj)
    if objType in [h5py._hl.group.Group, h5py._hl.files.File]:
        for key in obj.keys():
            setDataSets(listp, obj[key])
    elif objType == h5py._hl.dataset.Dataset:
        listp.append(obj)
