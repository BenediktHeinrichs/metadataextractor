def returnData():
    test1 = """@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix ks: <http://dkm.fbk.eu/ontologies/knowledgestore#> .

        {
            <http://pikes.fbk.eu/#char=38,51> a ks:NameMention .
            
            <http://pikes.fbk.eu/#char=53,55;60,65> ks:componentSubString <http://pikes.fbk.eu/#char=60,65> .
        }
        @prefix nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#> .
        @prefix xs: <http://www.w3.org/2001/XMLSchema#> .

        {
            <http://pikes.fbk.eu/#char=101,110> nif:beginIndex "101"^^xs:int .
        }
        @prefix dbpedia: <http://dbpedia.org/resource/> .

        {
            <http://dbpedia.org/resource/Washington,_D.C.> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=0,15> .
            
            <http://pikes.fbk.eu/#char=53,55;60,65> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=23,30> ks:lemma "capital" .
            
            <http://pikes.fbk.eu/#char=19,51;53,55> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#char=118,122> nif:endIndex "122"^^xs:int .
            
            <http://pikes.fbk.eu/#char=23,30;38,51> ks:componentSubString <http://pikes.fbk.eu/#char=23,30> .
            
            <http://pikes.fbk.eu/#char=23,30> nif:anchorOf "capital" .
            
            <http://pikes.fbk.eu/#char=60,65;72,89> ks:componentSubString <http://pikes.fbk.eu/#char=60,65> .
            
            <http://pikes.fbk.eu/#char=23,30> nif:beginIndex "23"^^xs:int .
            
            <http://pikes.fbk.eu/#char=23,30;38,51> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#char=53,55;60,65> ks:mentionOf <http://pikes.fbk.eu/> .
            
            dbpedia:George_Washington <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=72,89> .
            
            <http://pikes.fbk.eu/#char=53,55;60,65> nif:anchorOf "It [...] named" .
            
            <http://pikes.fbk.eu/#char=101,110> ks:lemma "president" .
            
            <http://pikes.fbk.eu/#char=60,65;72,89> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=19,51;53,55> nif:beginIndex "19"^^xs:int .
            
            <http://pikes.fbk.eu/#char=72,89;91,122> ks:componentSubString <http://pikes.fbk.eu/#char=91,122> .
            
            <http://pikes.fbk.eu/#char=118,122> nif:beginIndex "118"^^xs:int .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=23,30> .
            
            <http://pikes.fbk.eu/#char=101,110;118,122> a ks:CompoundString .
            
            <http://pikes.fbk.eu/#char=23,30> a ks:PredicateMention ;
                ks:sst <http://www.newsreader-project.eu/sst/noun.group> .
            
            <http://pikes.fbk.eu/#char=60,65> nif:beginIndex "60"^^xs:int .
            
            <http://pikes.fbk.eu/#char=53,55> nif:beginIndex "53"^^xs:int .
            
            <http://pikes.fbk.eu/#char=72,89> a ks:Mention .
        }
        @prefix dcterms: <http://purl.org/dc/terms/> .

        {
            <http://pikes.fbk.eu/> dcterms:language <http://lexvo.org/id/iso639-3/eng> .
            
            <http://pikes.fbk.eu/#char=101,110> a ks:EntityMention .
            
            <http://pikes.fbk.eu/#char=0,15> nif:endIndex "15"^^xs:int .
            
            <http://pikes.fbk.eu/#char=72,89;91,122> a ks:CompoundString .
            
            <http://pikes.fbk.eu/.naf> ks:annotationOf <http://pikes.fbk.eu/> .
            
            dbpedia:United_States <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=118,122> .
            
            <http://pikes.fbk.eu/#char=72,89;91,122> ks:componentSubString <http://pikes.fbk.eu/#char=72,89> .
            
            <http://pikes.fbk.eu/#char=60,65;72,89> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/.naf> a ks:NAF .
            
            <http://pikes.fbk.eu/#char=0,15;19,51> a ks:CompoundString .
            
            <http://pikes.fbk.eu/#char=95,100> nif:beginIndex "95"^^xs:int .
            
            <http://pikes.fbk.eu/#char=72,89> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=53,55;60,65> .
            
            <http://pikes.fbk.eu/#char=23,30;38,51> nif:endIndex "51"^^xs:int .
            
            <http://pikes.fbk.eu/#char=19,51;53,55> nif:anchorOf "the capital of the United States [...] It" .
            
            <http://pikes.fbk.eu/#char=118,122> a ks:EntityMention .
            
            <http://pikes.fbk.eu/#char=0,15;53,55> nif:endIndex "55"^^xs:int .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=19,51;53,55> .
            
            <http://pikes.fbk.eu/#char=0,15;53,55> a ks:CompoundString .
            
            <http://pikes.fbk.eu/#char=0,15> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=0,15;19,51> ks:componentSubString <http://pikes.fbk.eu/#char=0,15> .
            
            <http://pikes.fbk.eu/#char=60,65> a ks:PredicateMention .
            
            <http://pikes.fbk.eu/#char=91,122> nif:anchorOf "the first president of the U.S." .
            
            <http://pikes.fbk.eu/#char=0,15;19,51> ks:componentSubString <http://pikes.fbk.eu/#char=19,51> .
            
            <http://pikes.fbk.eu/#char=19,51> nif:anchorOf "the capital of the United States" .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=95,100> .
            
            <http://pikes.fbk.eu/#char=101,110> nif:anchorOf "president" .
            
            <http://pikes.fbk.eu/#char=101,110;118,122> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=0,15;53,55> nif:anchorOf "Washington D.C. [...] It" .
            
            <http://pikes.fbk.eu/#char=91,122> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=60,65> nif:anchorOf "named" .
            
            <http://pikes.fbk.eu/#char=19,51;53,55> ks:componentSubString <http://pikes.fbk.eu/#char=53,55> .
            
            <http://pikes.fbk.eu/#char=0,15;53,55> ks:componentSubString <http://pikes.fbk.eu/#char=0,15> .
            
            <http://pikes.fbk.eu/#char=23,30> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=60,65> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=72,89;91,122> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=0,15> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#char=101,110> a ks:ParticipationMention ;
                nif:endIndex "110"^^xs:int .
            
            <http://pikes.fbk.eu/#char=72,89;91,122> nif:anchorOf "George Washington [...] the first president of the U.S." .
            
            <http://pikes.fbk.eu/#char=101,110;118,122> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#char=0,15;19,51> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=101,110;118,122> nif:endIndex "122"^^xs:int .
            
            <http://pikes.fbk.eu/#char=91,122> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#capital_2> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=23,30> .
            
            <http://pikes.fbk.eu/#char=91,122> nif:endIndex "122"^^xs:int .
            
            <http://pikes.fbk.eu/#char=53,55> nif:endIndex "55"^^xs:int .
            
            <http://pikes.fbk.eu/#char=19,51> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=38,51> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=23,30> nif:endIndex "30"^^xs:int ;
                ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#char=95,100> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=118,122> nif:anchorOf "U.S." .
            
            <http://pikes.fbk.eu/#char=101,110> ks:sst <http://www.newsreader-project.eu/sst/noun.person> .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=53,55> .
            
            <http://pikes.fbk.eu/#char=0,15;53,55> a ks:Mention .
            
            <http://pikes.fbk.eu/> ks:textHash "PIaLM4Eb2wZDK9FAbDxgBa" .
            
            dbpedia:George_Washington <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=101,110> .
            
            <http://pikes.fbk.eu/> dcterms:creator "" .
            
            <http://pikes.fbk.eu/#char=60,65> ks:sst <http://www.newsreader-project.eu/sst/verb.communication> .
            
            <http://pikes.fbk.eu/#char=0,15;19,51> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://dbpedia.org/resource/Washington,_D.C.> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=23,30> .
            
            <http://pikes.fbk.eu/#char=19,51> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#char=38,51> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#char=95,100> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#char=118,122> a ks:NameMention .
            
            <http://pikes.fbk.eu/#char=53,55> nif:anchorOf "It" .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=0,15;53,55> .
            
            <http://pikes.fbk.eu/#char=53,55;60,65> ks:componentSubString <http://pikes.fbk.eu/#char=53,55> .
            
            <http://pikes.fbk.eu/#char=101,110;118,122> nif:beginIndex "101"^^xs:int .
            
            <http://pikes.fbk.eu/#char=0,15;53,55> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#name> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=60,65> .
            
            <http://pikes.fbk.eu/#char=72,89> a ks:EntityMention .
            
            <http://pikes.fbk.eu/#char=38,51> nif:beginIndex "38"^^xs:int .
            
            <http://pikes.fbk.eu/#char=53,55;60,65> nif:endIndex "65"^^xs:int .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=118,122> .
            
            <http://pikes.fbk.eu/#char=60,65> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#char=72,89;91,122> ks:mentionOf <http://pikes.fbk.eu/> ;
                nif:endIndex "122"^^xs:int .
            
            <http://pikes.fbk.eu/#char=0,15;19,51> nif:beginIndex "0"^^xs:int .
            
            <http://pikes.fbk.eu/#char=19,51> nif:beginIndex "19"^^xs:int .
            
            <http://pikes.fbk.eu/#char=0,15> nif:beginIndex "0"^^xs:int .
            
            <http://pikes.fbk.eu/.naf> ks:layer ks:layer_text .
            
            <http://pikes.fbk.eu/#char=53,55> a ks:Mention .
            
            <http://pikes.fbk.eu/#president_2> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=101,110> .
            
            <http://pikes.fbk.eu/#char=23,30;38,51> a ks:ParticipationMention .
            
            <http://pikes.fbk.eu/#char=53,55;60,65> a ks:ParticipationMention .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=101,110> .
            
            <http://pikes.fbk.eu/.naf> ks:version "v3" .
            
            <http://pikes.fbk.eu/#char=0,15;19,51> nif:endIndex "51"^^xs:int .
            
            <http://pikes.fbk.eu/#char=38,51> nif:anchorOf "United States" .
            
            <http://pikes.fbk.eu/#char=0,15;53,55> nif:beginIndex "0"^^xs:int .
            
            <http://pikes.fbk.eu/#char=38,51> nif:endIndex "51"^^xs:int .
            
            <http://pikes.fbk.eu/#char=19,51> nif:endIndex "51"^^xs:int .
            
            <http://pikes.fbk.eu/#char=53,55;60,65> nif:beginIndex "53"^^xs:int .
            
            <http://pikes.fbk.eu/#char=101,110> a ks:PredicateMention .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=91,122> .
            
            <http://pikes.fbk.eu/#char=72,89> a ks:NameMention .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=23,30;38,51> .
            
            <http://pikes.fbk.eu/#char=0,15> a ks:EntityMention .
            
            <http://pikes.fbk.eu/#char=91,122> nif:beginIndex "91"^^xs:int .
            
            <http://pikes.fbk.eu/#char=53,55> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=60,65;72,89> .
            
            <http://pikes.fbk.eu/#char=95,100> nif:endIndex "100"^^xs:int .
            
            <http://pikes.fbk.eu/#char=60,65;72,89> a ks:ParticipationMention .
            
            <http://pikes.fbk.eu/.naf> ks:layer ks:layer_naf-filter .
            
            <http://pikes.fbk.eu/#char=19,51;53,55> a ks:CompoundString .
            
            <http://pikes.fbk.eu/> a ks:Text .
            
            <http://pikes.fbk.eu/#char=23,30> a ks:EntityMention ;
                ks:synset <http://www.newsreader-project.eu/syn/08357129-n> .
            
            <http://pikes.fbk.eu/#char=23,30;38,51> ks:componentSubString <http://pikes.fbk.eu/#char=38,51> .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=0,15;19,51> .
            
            <http://pikes.fbk.eu/#char=60,65;72,89> nif:endIndex "89"^^xs:int .
            
            <http://pikes.fbk.eu/#char=23,30;38,51> a ks:CompoundString .
            
            <http://pikes.fbk.eu/#char=95,100> a ks:AttributeMention .
            
            <http://dbpedia.org/resource/Washington,_D.C.> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=53,55> .
            
            <http://pikes.fbk.eu/#char=72,89> nif:endIndex "89"^^xs:int .
            
            <http://pikes.fbk.eu/#char=0,15;53,55> ks:componentSubString <http://pikes.fbk.eu/#char=53,55> .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=38,51> .
            
            <http://pikes.fbk.eu/#char=38,51> a ks:EntityMention .
            
            <http://pikes.fbk.eu/#char=60,65> ks:lemma "name" .
            
            <http://pikes.fbk.eu/#char=72,89> nif:anchorOf "George Washington" ;
                nif:beginIndex "72"^^xs:int .
            
            <http://pikes.fbk.eu/.naf> dcterms:creator ks:NAF%20filter.null .
            
            <http://pikes.fbk.eu/> a ks:Resource .
            
            <http://pikes.fbk.eu/#char=23,30;38,51> nif:beginIndex "23"^^xs:int .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=101,110;118,122> .
            
            <http://pikes.fbk.eu/#char=19,51;53,55> nif:endIndex "55"^^xs:int .
            
            <http://pikes.fbk.eu/#char=101,110> a ks:Mention .
            
            ks:NAF%20filter.null dcterms:title "NAF filter" .
            
            <http://pikes.fbk.eu/#char=60,65;72,89> nif:beginIndex "60"^^xs:int .
            
            <http://pikes.fbk.eu/#char=23,30;38,51> nif:anchorOf "capital [...] United States" .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=72,89> .
            
            <http://pikes.fbk.eu/.naf> dcterms:identifier "" .
            
            <http://pikes.fbk.eu/#char=60,65> nif:endIndex "65"^^xs:int ;
                ks:synset <http://www.newsreader-project.eu/syn/01024190-v> .
            
            <http://pikes.fbk.eu/.naf> dcterms:creator ks:Stanford%20CoreNLP.null .
            
            <http://pikes.fbk.eu/#char=101,110;118,122> nif:anchorOf "president [...] U.S." .
            
            <http://pikes.fbk.eu/.naf> dcterms:created "2020-01-22T15:34:16.410+0100" .
            
            <http://pikes.fbk.eu/#char=101,110;118,122> a ks:ParticipationMention .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=0,15> .
            
            <http://pikes.fbk.eu/#char=19,51;53,55> a ks:Mention .
            
            dbpedia:United_States <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=38,51> .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=19,51> .
            
            <http://pikes.fbk.eu/#char=0,15> a ks:NameMention .
            
            <http://pikes.fbk.eu/#char=0,15;19,51> nif:anchorOf "Washington D.C. [...] the capital of the United States" .
            
            <http://pikes.fbk.eu/#char=53,55;60,65> a ks:CompoundString .
            
            <http://pikes.fbk.eu/#char=23,30> a ks:ParticipationMention .
            
            <http://pikes.fbk.eu/#char=101,110;118,122> ks:componentSubString <http://pikes.fbk.eu/#char=118,122> .
            
            <http://pikes.fbk.eu/#char=101,110> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#char=118,122> a ks:Mention .
            
            <http://pikes.fbk.eu/#char=19,51;53,55> ks:componentSubString <http://pikes.fbk.eu/#char=19,51> .
            
            ks:Stanford%20CoreNLP.null dcterms:title "Stanford CoreNLP" .
            
            <http://pikes.fbk.eu/#char=95,100> nif:anchorOf "first" .
            
            <http://pikes.fbk.eu/.naf> a ks:Resource .
            
            <http://pikes.fbk.eu/#char=23,30;38,51> a ks:Mention .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=60,65> .
            
            <http://pikes.fbk.eu/#char=101,110;118,122> ks:componentSubString <http://pikes.fbk.eu/#char=101,110> .
            
            <http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=72,89;91,122> .
            
            <http://pikes.fbk.eu/#char=0,15> nif:anchorOf "Washington D.C." .
            
            <http://pikes.fbk.eu/#char=53,55> a ks:EntityMention .
            
            <http://pikes.fbk.eu/#char=118,122> ks:mentionOf <http://pikes.fbk.eu/> .
            
            <http://pikes.fbk.eu/#char=101,110> ks:synset <http://www.newsreader-project.eu/syn/10467395-n> .
            
            <http://pikes.fbk.eu/#char=60,65;72,89> a ks:CompoundString .
            
            <http://pikes.fbk.eu/#char=72,89;91,122> nif:beginIndex "72"^^xs:int .
            
            <http://pikes.fbk.eu/> dcterms:title "" ;
                dcterms:created "2020-01-22T15:34:11+01:00" ;
                ks:annotatedWith <http://pikes.fbk.eu/.naf> .
            
            <http://pikes.fbk.eu/#char=60,65;72,89> ks:componentSubString <http://pikes.fbk.eu/#char=72,89> ;
                nif:anchorOf "named [...] George Washington" .
        }
        @prefix sem: <http://semanticweb.cs.vu.nl/2009/11/sem/> .

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a sem:Event .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }
        @prefix sumo: <http://www.ontologyportal.org/SUMO.owl#> .

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a sumo:Entity .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:HdxRwoOYBLfEeU2VfAvNYc> {
            <http://pikes.fbk.eu/#name> sem:hasActor <http://dbpedia.org/resource/Washington,_D.C.> .
        }

        {
            <fact:HdxRwoOYBLfEeU2VfAvNYc> ks:expressedBy <http://pikes.fbk.eu/#char=53,55;60,65> .
        }
        @prefix pm: <http://premon.fbk.eu/resource/> .

        <fact:HdxRwoOYBLfEeU2VfAvNYc> {
            <http://pikes.fbk.eu/#name> <http://premon.fbk.eu/resource/vb32-name-29.3@theme> <http://dbpedia.org/resource/Washington,_D.C.> .
        }

        {
            <fact:HdxRwoOYBLfEeU2VfAvNYc> ks:expressedBy <http://pikes.fbk.eu/#char=53,55;60,65> .
        }

        <fact:NrhpdAIPYiRBedKPt2yDBM> {
            dbpedia:United_States a <http://www.newsreader-project.eu/ontologies/LOCATION> .
        }

        {
            <fact:NrhpdAIPYiRBedKPt2yDBM> ks:expressedBy <http://pikes.fbk.eu/#char=118,122> , <http://pikes.fbk.eu/#char=38,51> .
        }

        <fact:FkZqkK8T_fEILEz9bWPPoE> {
            <http://pikes.fbk.eu/#name> sem:hasTime dbpedia:George_Washington .
        }

        {
            <fact:FkZqkK8T_fEILEz9bWPPoE> ks:expressedBy <http://pikes.fbk.eu/#char=60,65;72,89> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a ks:Predicate .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }
        @prefix dbyago: <http://dbpedia.org/class/yago/> .

        <fact:EpJko-B_jg8E8TBwUo_Ajb> {
            dbpedia:George_Washington a dbyago:HeadOfState110164747 .
        }

        {
            <fact:EpJko-B_jg8E8TBwUo_Ajb> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a sumo:BiologicalProcess .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:EpJko-B_jg8E8TBwUo_Ajb> {
            <http://pikes.fbk.eu/#president_2> a ks:Entity .
        }

        {
            <fact:EpJko-B_jg8E8TBwUo_Ajb> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> .
        }
        @prefix eso: <http://www.newsreader-project.eu/domain-ontology#> .

        <fact:HdxRwoOYBLfEeU2VfAvNYc> {
            <http://pikes.fbk.eu/#name> <http://www.newsreader-project.eu/domain-ontology#Replacing@replacing-entity_2> <http://dbpedia.org/resource/Washington,_D.C.> .
        }

        {
            <fact:HdxRwoOYBLfEeU2VfAvNYc> ks:expressedBy <http://pikes.fbk.eu/#char=53,55;60,65> .
        }

        <fact:D8j498ACDxvMm6Rcg1n2Wx> {
            <http://dbpedia.org/resource/Washington,_D.C.> a ks:Entity .
        }

        {
            <fact:D8j498ACDxvMm6Rcg1n2Wx> ks:expressedBy <http://pikes.fbk.eu/#char=0,15> , <http://pikes.fbk.eu/#char=23,30> , <http://pikes.fbk.eu/#char=53,55> .
        }

        <fact:CnV_hOHiy3XCIWVVg7G0JG> {
            dbpedia:George_Washington a <http://www.newsreader-project.eu/ontologies/PERSON> .
        }

        {
            <fact:CnV_hOHiy3XCIWVVg7G0JG> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> , <http://pikes.fbk.eu/#char=72,89> .
        }

        <fact:EpJko-B_jg8E8TBwUo_Ajb> {
            <http://pikes.fbk.eu/#president_2> a ks:Predicate .
        }

        {
            <fact:EpJko-B_jg8E8TBwUo_Ajb> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> .
        }

        <fact:EpJko-B_jg8E8TBwUo_Ajb> {
            <http://pikes.fbk.eu/#president_2> sem:hasActor dbpedia:George_Washington .
        }

        {
            <fact:EpJko-B_jg8E8TBwUo_Ajb> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> .
        }
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

        <fact:PV56DYeno0PIgZ_VkrniPQ> {
            dbpedia:George_Washington rdfs:label "George Washington" .
        }

        {
            <fact:PV56DYeno0PIgZ_VkrniPQ> ks:expressedBy <http://pikes.fbk.eu/#char=72,89> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a pm:pb17-name.01 .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:GjR3kgUbE4MN-D3v6nRTx3> {
            <http://dbpedia.org/resource/Washington,_D.C.> a dbyago:FederalGovernment108052549 .
        }

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:KTS8gueHU_GNCGpImPFiMD> {
            <http://pikes.fbk.eu/#capital_2> <http://premon.fbk.eu/resource/fn15-relational_political_locales@container_possessor> dbpedia:United_States .
        }

        {
            <fact:KTS8gueHU_GNCGpImPFiMD> ks:expressedBy <http://pikes.fbk.eu/#char=23,30;38,51> .
        }

        <fact:A5TXMj96r4OIW4ByKh790l> {
            <http://pikes.fbk.eu/#president_2> <http://premon.fbk.eu/resource/nb10-president.01@arg2> dbpedia:United_States .
        }

        {
            <fact:A5TXMj96r4OIW4ByKh790l> ks:expressedBy <http://pikes.fbk.eu/#char=101,110;118,122> .
        }

        <fact:GjR3kgUbE4MN-D3v6nRTx3> {
            <http://dbpedia.org/resource/Washington,_D.C.> a <http://www.newsreader-project.eu/ontologies/ORGANIZATION> .
        }

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a sumo:Process .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }
        @prefix frb: <http://framebase.org/ns/> .

        <fact:KTS8gueHU_GNCGpImPFiMD> {
            <http://pikes.fbk.eu/#capital_2> frb:fe-Relational_political_locales-Container_possessor dbpedia:United_States .
        }

        {
            <fact:KTS8gueHU_GNCGpImPFiMD> ks:expressedBy <http://pikes.fbk.eu/#char=23,30;38,51> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a sumo:DualObjectProcess .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:GjR3kgUbE4MN-D3v6nRTx3> {
            <http://dbpedia.org/resource/Washington,_D.C.> rdfs:label "capital" .
        }

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:FkZqkK8T_fEILEz9bWPPoE> {
            <http://pikes.fbk.eu/#name> <http://premon.fbk.eu/resource/pb17-name.01@argtmp> dbpedia:George_Washington .
        }

        {
            <fact:FkZqkK8T_fEILEz9bWPPoE> ks:expressedBy <http://pikes.fbk.eu/#char=60,65;72,89> .
        }

        <fact:EpJko-B_jg8E8TBwUo_Ajb> {
            <http://pikes.fbk.eu/#president_2> a pm:nb10-president.01 .
        }

        {
            <fact:EpJko-B_jg8E8TBwUo_Ajb> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a sumo:InternalChange .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:HdxRwoOYBLfEeU2VfAvNYc> {
            <http://pikes.fbk.eu/#name> <http://premon.fbk.eu/resource/fn15-being_named@entity> <http://dbpedia.org/resource/Washington,_D.C.> .
        }

        {
            <fact:HdxRwoOYBLfEeU2VfAvNYc> ks:expressedBy <http://pikes.fbk.eu/#char=53,55;60,65> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a ks:Entity .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:HdxRwoOYBLfEeU2VfAvNYc> {
            <http://pikes.fbk.eu/#name> frb:fe-Being_named-Entity <http://dbpedia.org/resource/Washington,_D.C.> .
        }

        {
            <fact:HdxRwoOYBLfEeU2VfAvNYc> ks:expressedBy <http://pikes.fbk.eu/#char=53,55;60,65> .
        }
        @prefix foaf: <http://xmlns.com/foaf/0.1/> .

        <fact:ObHRSopMIVjIJwETN_k7Xo> {
            dbpedia:United_States foaf:name "United States" .
        }

        {
            <fact:ObHRSopMIVjIJwETN_k7Xo> ks:expressedBy <http://pikes.fbk.eu/#char=38,51> .
        }

        <fact:FEAP8BnJOdBACDEKfJdSqA> {
            dbpedia:United_States foaf:name "U.S." .
        }

        {
            <fact:FEAP8BnJOdBACDEKfJdSqA> ks:expressedBy <http://pikes.fbk.eu/#char=118,122> .
        }

        <fact:EpJko-B_jg8E8TBwUo_Ajb> {
            dbpedia:George_Washington rdfs:label "president" .
        }

        {
            <fact:EpJko-B_jg8E8TBwUo_Ajb> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> .
        }

        <fact:GjR3kgUbE4MN-D3v6nRTx3> {
            <http://pikes.fbk.eu/#capital_2> a ks:Predicate .
        }

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:NrhpdAIPYiRBedKPt2yDBM> {
            dbpedia:United_States a ks:Entity .
        }

        {
            <fact:NrhpdAIPYiRBedKPt2yDBM> ks:expressedBy <http://pikes.fbk.eu/#char=118,122> , <http://pikes.fbk.eu/#char=38,51> .
        }

        <fact:A5TXMj96r4OIW4ByKh790l> {
            <http://pikes.fbk.eu/#president_2> ks:mod dbpedia:United_States .
        }

        {
            <fact:A5TXMj96r4OIW4ByKh790l> ks:expressedBy <http://pikes.fbk.eu/#char=101,110;118,122> .
        }

        <fact:GjR3kgUbE4MN-D3v6nRTx3> {
            <http://pikes.fbk.eu/#capital_2> <http://premon.fbk.eu/resource/fn15-relational_political_locales@locale> <http://dbpedia.org/resource/Washington,_D.C.> .
        }

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:HbGNzjd2RBQKIWNPAk9IGB> {
            <http://dbpedia.org/resource/Washington,_D.C.> rdfs:label "Washington D.C." .
        }

        {
            <fact:HbGNzjd2RBQKIWNPAk9IGB> ks:expressedBy <http://pikes.fbk.eu/#char=0,15> .
        }

        <fact:GjR3kgUbE4MN-D3v6nRTx3> {
            <http://pikes.fbk.eu/#capital_2> a sem:Event .
        }

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a sumo:IntentionalProcess .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a sumo:PsychologicalProcess .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:A5TXMj96r4OIW4ByKh790l> {
            <http://pikes.fbk.eu/#president_2> sem:hasActor dbpedia:United_States .
        }

        {
            <fact:A5TXMj96r4OIW4ByKh790l> ks:expressedBy <http://pikes.fbk.eu/#char=101,110;118,122> .
        }

        <fact:HdxRwoOYBLfEeU2VfAvNYc> {
            <http://pikes.fbk.eu/#name> <http://premon.fbk.eu/resource/pb17-name.01@arg1> <http://dbpedia.org/resource/Washington,_D.C.> .
        }

        {
            <fact:HdxRwoOYBLfEeU2VfAvNYc> ks:expressedBy <http://pikes.fbk.eu/#char=53,55;60,65> .
        }

        <fact:PJpi8alKE_4A8ByXupFizh> {
            <http://pikes.fbk.eu/#president_2> ks:rank "1.0"^^xs:double .
        }

        {
            <fact:PJpi8alKE_4A8ByXupFizh> ks:expressedBy <http://pikes.fbk.eu/#char=95,100> .
        }

        <fact:Iri2qZMZDspG1sDPIL1Vje> {
            <http://dbpedia.org/resource/Washington,_D.C.> rdfs:seeAlso dbpedia:Italian_language .
        }

        {
            <fact:Iri2qZMZDspG1sDPIL1Vje> ks:expressedBy <http://pikes.fbk.eu/#char=53,55> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a eso:IntentionalEvent .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:EpJko-B_jg8E8TBwUo_Ajb> {
            <http://pikes.fbk.eu/#president_2> a pm:fn15-leadership .
        }

        {
            <fact:EpJko-B_jg8E8TBwUo_Ajb> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> .
        }

        <fact:EpJko-B_jg8E8TBwUo_Ajb> {
            <http://pikes.fbk.eu/#president_2> <http://premon.fbk.eu/resource/fn15-leadership@leader> dbpedia:George_Washington .
        }

        {
            <fact:EpJko-B_jg8E8TBwUo_Ajb> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> .
        }

        <fact:GjR3kgUbE4MN-D3v6nRTx3> {
            <http://dbpedia.org/resource/Washington,_D.C.> rdfs:seeAlso dbpedia:Capital_city .
        }

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:PV56DYeno0PIgZ_VkrniPQ> {
            dbpedia:George_Washington foaf:name "George Washington" .
        }

        {
            <fact:PV56DYeno0PIgZ_VkrniPQ> ks:expressedBy <http://pikes.fbk.eu/#char=72,89> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a sumo:IntentionalPsychologicalProcess .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:GjR3kgUbE4MN-D3v6nRTx3> {
            <http://pikes.fbk.eu/#capital_2> a pm:fn15-relational_political_locales .
        }

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a eso:Replacing .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a pm:vb32-name-29.3 .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:EpJko-B_jg8E8TBwUo_Ajb> {
            <http://pikes.fbk.eu/#president_2> a sem:Event .
        }

        {
            <fact:EpJko-B_jg8E8TBwUo_Ajb> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> .
        }

        <fact:CnV_hOHiy3XCIWVVg7G0JG> {
            dbpedia:George_Washington a ks:Entity .
        }

        {
            <fact:CnV_hOHiy3XCIWVVg7G0JG> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> , <http://pikes.fbk.eu/#char=72,89> .
        }

        <fact:EpJko-B_jg8E8TBwUo_Ajb> {
            <http://pikes.fbk.eu/#president_2> <http://premon.fbk.eu/resource/nb10-president.01@arg0> dbpedia:George_Washington .
        }

        {
            <fact:EpJko-B_jg8E8TBwUo_Ajb> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> .
        }

        <fact:FEAP8BnJOdBACDEKfJdSqA> {
            dbpedia:United_States rdfs:label "U.S." .
        }

        {
            <fact:FEAP8BnJOdBACDEKfJdSqA> ks:expressedBy <http://pikes.fbk.eu/#char=118,122> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a sumo:Comparing .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a sumo:Physical .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> a pm:fn15-being_named .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:GjR3kgUbE4MN-D3v6nRTx3> {
            <http://pikes.fbk.eu/#capital_2> a ks:Entity .
        }

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:GjR3kgUbE4MN-D3v6nRTx3> {
            <http://pikes.fbk.eu/#capital_2> frb:fe-Relational_political_locales-Locale <http://dbpedia.org/resource/Washington,_D.C.> .
        }

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:HbGNzjd2RBQKIWNPAk9IGB> {
            <http://dbpedia.org/resource/Washington,_D.C.> a <http://www.newsreader-project.eu/ontologies/LOCATION> .
        }

        {
            <fact:HbGNzjd2RBQKIWNPAk9IGB> ks:expressedBy <http://pikes.fbk.eu/#char=0,15> .
        }

        <fact:F_lw_mh0iWRLufTOLPJDky> {
            <http://pikes.fbk.eu/#name> rdfs:label "named" .
        }

        {
            <fact:F_lw_mh0iWRLufTOLPJDky> ks:expressedBy <http://pikes.fbk.eu/#char=60,65> .
        }

        <fact:EpJko-B_jg8E8TBwUo_Ajb> {
            <http://pikes.fbk.eu/#president_2> frb:fe-Leadership-Leader dbpedia:George_Washington .
        }

        {
            <fact:EpJko-B_jg8E8TBwUo_Ajb> ks:expressedBy <http://pikes.fbk.eu/#char=101,110> .
        }

        <fact:KTS8gueHU_GNCGpImPFiMD> {
            <http://pikes.fbk.eu/#capital_2> ks:mod dbpedia:United_States .
        }

        {
            <fact:KTS8gueHU_GNCGpImPFiMD> ks:expressedBy <http://pikes.fbk.eu/#char=23,30;38,51> .
        }

        <fact:GjR3kgUbE4MN-D3v6nRTx3> {
            <http://pikes.fbk.eu/#capital_2> a frb:frame-Relational_political_locales-capital.n .
        }

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:HbGNzjd2RBQKIWNPAk9IGB> {
            <http://dbpedia.org/resource/Washington,_D.C.> foaf:name "Washington D.C." .
        }

        {
            <fact:HbGNzjd2RBQKIWNPAk9IGB> ks:expressedBy <http://pikes.fbk.eu/#char=0,15> .
        }"""

    test2 = """
        @prefix dbpedia: <http://dbpedia.org/resource/> .
        @prefix frb: <http://framebase.org/ns/> .
        @prefix ks: <http://dkm.fbk.eu/ontologies/knowledgestore#> .

        {
            <fact:GjR3kgUbE4MN-D3v6nRTx3> ks:expressedBy <http://pikes.fbk.eu/#char=23,30> .
        }

        <fact:KTS8gueHU_GNCGpImPFiMD> {
            <http://pikes.fbk.eu/#capital_2> frb:fe-Relational_political_locales-Container_possessor dbpedia:United_States .
        }"""

    test3 = """@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owltime: <http://www.w3.org/TR/owl-time#> .

{
	<http://www.newsreader-project.eu/time/_desc> a owltime:DateTimeDescription .
	
	<http://www.newsreader-project.eu/time/> owltime:hasDateTimeDescription <http://www.newsreader-project.eu/time/_desc> ;
		a owltime:DateTimeInterval , owltime:ProperInterval .
}
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xs: <http://www.w3.org/2001/XMLSchema#> .

{
	<http://www.newsreader-project.eu/time/> rdfs:label "" .
}
@prefix nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#> .

{
	<http://pikes.fbk.eu/#char=31,34> nif:endIndex "34"^^xs:int .
	
	<http://pikes.fbk.eu/#char=0,4;26,30> nif:beginIndex "0"^^xs:int .
}
@prefix ks: <http://dkm.fbk.eu/ontologies/knowledgestore#> .

{
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=122,132;137,143> .
	
	<http://pikes.fbk.eu/#char=67,72;95,100> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=19,24> .
	
	<http://pikes.fbk.eu/#char=8,15> nif:anchorOf "married" .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=8,15;19,24> .
	
	<http://pikes.fbk.eu/#char=0,4;8,15> a ks:ParticipationMention .
	
	<http://pikes.fbk.eu/#char=38,44> a ks:EntityMention ;
		nif:beginIndex "38"^^xs:int .
	
	<http://pikes.fbk.eu/#char=38,44;48,52> nif:anchorOf "affair [...] Jake" .
	
	<http://pikes.fbk.eu/#char=73,79;89,93> a ks:CompoundString .
}
@prefix dcterms: <http://purl.org/dc/terms/> .

{
	<http://pikes.fbk.eu/.naf> dcterms:identifier "" .
	
	<http://pikes.fbk.eu/#char=122,132> ks:synset <http://www.newsreader-project.eu/syn/02349212-v> .
	
	<http://pikes.fbk.eu/#char=38,44;48,52> a ks:CompoundString .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=26,34> .
	
	<http://pikes.fbk.eu/#char=31,34> nif:anchorOf "has" .
	
	<http://pikes.fbk.eu/#char=0,4;8,15> nif:endIndex "15"^^xs:int .
	
	<http://pikes.fbk.eu/#char=122,132> nif:beginIndex "122"^^xs:int .
	
	<http://pikes.fbk.eu/#char=48,52> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=80,84> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=48,52> nif:endIndex "52"^^xs:int .
	
	<http://pikes.fbk.eu/#char=26,30> nif:anchorOf "Mary" .
	
	<http://pikes.fbk.eu/.naf> ks:layer ks:layer_text .
	
	<http://pikes.fbk.eu/#char=0,4;26,30> nif:anchorOf "Mary [...] Mary" .
	
	<http://pikes.fbk.eu/#char=8,15;19,24> ks:componentSubString <http://pikes.fbk.eu/#char=8,15> .
	
	<http://pikes.fbk.eu/#char=60,62> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=8,15;19,24> nif:beginIndex "8"^^xs:int .
	
	<http://pikes.fbk.eu/#char=26,30;80,84> ks:componentSubString <http://pikes.fbk.eu/#char=80,84> .
	
	<http://pikes.fbk.eu/#char=26,30> a ks:EntityMention .
	
	<http://pikes.fbk.eu/#char=104,107> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=8,15;19,24> a ks:ParticipationMention .
	
	ks:NAF%20filter.null dcterms:title "NAF filter" .
	
	<entity:peter> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=19,24> .
	
	<http://pikes.fbk.eu/#char=8,15;19,24> nif:anchorOf "married [...] Peter" .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=0,4;8,15> .
	
	<http://pikes.fbk.eu/#char=73,79;89,93> nif:endIndex "93"^^xs:int .
	
	<http://pikes.fbk.eu/#char=19,24> nif:anchorOf "Peter" .
	
	<http://pikes.fbk.eu/#char=63,66> nif:beginIndex "63"^^xs:int .
	
	<http://pikes.fbk.eu/#char=48,52> nif:anchorOf "Jake" .
	
	<http://pikes.fbk.eu/#char=0,4;26,30> a ks:CompoundString .
	
	<http://pikes.fbk.eu/#char=8,15> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=31,34> ks:lemma "have" .
	
	<http://pikes.fbk.eu/#char=19,24> nif:endIndex "24"^^xs:int .
	
	<http://pikes.fbk.eu/#char=8,15;19,24> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=26,34> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/.naf> dcterms:created "2020-01-24T16:00:50.083+0100" .
	
	<http://pikes.fbk.eu/#char=31,34;38,44> nif:anchorOf "has [...] affair" .
	
	<http://pikes.fbk.eu/#char=60,62> nif:beginIndex "60"^^xs:int .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=104,107> , <http://pikes.fbk.eu/#char=73,79;89,93> .
	
	<http://pikes.fbk.eu/#char=31,34;38,44> ks:componentSubString <http://pikes.fbk.eu/#char=31,34> .
	
	<http://pikes.fbk.eu/#char=122,132> ks:lemma "commit" .
	
	<http://pikes.fbk.eu/> a ks:Text .
	
	<http://pikes.fbk.eu/#char=38,44> a ks:PredicateMention .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=31,34;38,44> , <http://pikes.fbk.eu/#char=111,117> .
	
	<http://pikes.fbk.eu/#char=95,100> nif:anchorOf "Peter" .
	
	<http://pikes.fbk.eu/#kill> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=73,79> .
	
	<http://pikes.fbk.eu/#char=60,62> a ks:AttributeMention .
	
	<http://pikes.fbk.eu/#char=73,79;89,93> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=0,4> nif:endIndex "4"^^xs:int .
	
	<http://pikes.fbk.eu/> dcterms:language <http://lexvo.org/id/iso639-3/eng> .
	
	<http://pikes.fbk.eu/#char=38,44;48,52> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=26,30;38,44> a ks:CompoundString .
	
	<http://pikes.fbk.eu/#char=73,79> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=26,30;80,84> nif:endIndex "84"^^xs:int .
	
	<http://pikes.fbk.eu/#char=137,143> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=38,44;48,52> nif:endIndex "52"^^xs:int .
	
	<http://pikes.fbk.eu/#char=122,132> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=67,79> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=73,79;89,93> a ks:ParticipationMention .
	
	<http://pikes.fbk.eu/#char=73,84> a ks:Mention .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=67,72> .
	
	<http://pikes.fbk.eu/#char=31,34> nif:beginIndex "31"^^xs:int .
	
	<http://pikes.fbk.eu/#char=26,30;38,44> nif:beginIndex "26"^^xs:int .
	
	<http://pikes.fbk.eu/#char=31,34;38,44> nif:beginIndex "31"^^xs:int .
	
	<http://pikes.fbk.eu/#char=19,24;95,100> ks:componentSubString <http://pikes.fbk.eu/#char=95,100> .
	
	<http://pikes.fbk.eu/#char=137,143> ks:synset <http://www.newsreader-project.eu/syn/00220522-n> .
	
	<http://pikes.fbk.eu/#char=0,4;8,15> nif:anchorOf "Mary [...] married" .
	
	<http://pikes.fbk.eu/#char=67,72> nif:endIndex "72"^^xs:int .
	
	<http://pikes.fbk.eu/#char=111,117> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=38,44;48,52> a ks:ParticipationMention .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=8,15> .
	
	<entity:peter> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=67,72> .
	
	<http://pikes.fbk.eu/#char=0,4> a ks:Mention .
	
	<attr:be-1v> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=60,62> .
	
	<http://pikes.fbk.eu/#char=67,79> a ks:ParticipationMention .
	
	<http://pikes.fbk.eu/#char=122,132;137,143> nif:endIndex "143"^^xs:int .
	
	<http://pikes.fbk.eu/#char=95,100> nif:beginIndex "95"^^xs:int .
	
	<http://pikes.fbk.eu/#char=73,84> a ks:ParticipationMention .
	
	<http://pikes.fbk.eu/#char=26,30;80,84> nif:anchorOf "Mary [...] Mary" .
	
	<http://pikes.fbk.eu/#char=67,72;95,100> nif:beginIndex "67"^^xs:int .
	
	<http://pikes.fbk.eu/.naf> ks:layer ks:layer_naf-filter .
	
	<http://pikes.fbk.eu/#char=0,4;80,84> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#prison_2> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=111,117> .
	
	<http://pikes.fbk.eu/#char=63,66> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=19,24;95,100> nif:beginIndex "19"^^xs:int .
	
	<http://pikes.fbk.eu/#char=73,79> nif:beginIndex "73"^^xs:int .
	
	<http://pikes.fbk.eu/.naf> ks:annotationOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=8,15> ks:lemma "marry" .
	
	<http://pikes.fbk.eu/#char=0,4;26,30> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=31,34> ks:synset <http://www.newsreader-project.eu/syn/00065639-v> .
	
	<http://pikes.fbk.eu/#char=19,24> a ks:NameMention .
	
	<http://pikes.fbk.eu/#char=26,30;80,84> a ks:CompoundString .
	
	<entity:mary> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=26,30> .
	
	<http://pikes.fbk.eu/#char=122,132;137,143> a ks:CompoundString .
	
	<http://pikes.fbk.eu/#char=104,107> nif:endIndex "107"^^xs:int .
	
	<http://pikes.fbk.eu/#char=48,52;89,93> ks:componentSubString <http://pikes.fbk.eu/#char=89,93> .
	
	<http://pikes.fbk.eu/#char=26,30;38,44> a ks:ParticipationMention .
	
	<http://pikes.fbk.eu/#char=26,30> nif:endIndex "30"^^xs:int .
	
	<http://pikes.fbk.eu/#char=95,100> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#marry> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=8,15> .
	
	<http://pikes.fbk.eu/#char=19,24> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=48,52;89,93> ks:componentSubString <http://pikes.fbk.eu/#char=48,52> .
	
	<http://pikes.fbk.eu/#char=111,117> nif:endIndex "117"^^xs:int .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=19,24;95,100> .
	
	<http://pikes.fbk.eu/#char=19,24;67,72> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=60,62> .
	
	<http://pikes.fbk.eu/#char=95,100;122,132> ks:componentSubString <http://pikes.fbk.eu/#char=95,100> .
	
	<http://pikes.fbk.eu/#char=111,117> ks:lemma "prison" .
	
	<http://pikes.fbk.eu/#affair> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=38,44> .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=38,44;48,52> .
	
	<http://pikes.fbk.eu/#char=95,100;122,132> nif:endIndex "132"^^xs:int .
	
	<http://pikes.fbk.eu/#char=111,117> a ks:EntityMention .
	
	<http://pikes.fbk.eu/#char=8,15;19,24> nif:endIndex "24"^^xs:int .
	
	<http://pikes.fbk.eu/#char=26,30;38,44> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=19,24;95,100> ks:componentSubString <http://pikes.fbk.eu/#char=19,24> .
	
	<http://pikes.fbk.eu/#char=31,34> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=31,34;38,44> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=60,62> nif:anchorOf "is" .
	
	<http://pikes.fbk.eu/#char=63,66> nif:anchorOf "why" .
	
	<http://pikes.fbk.eu/#char=95,100> a ks:NameMention .
	
	<http://pikes.fbk.eu/#char=0,4;8,15> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=137,143> ks:sst <http://www.newsreader-project.eu/sst/noun.act> .
	
	<http://pikes.fbk.eu/#char=80,84> nif:beginIndex "80"^^xs:int .
	
	<http://pikes.fbk.eu/#char=31,34;38,44> nif:endIndex "44"^^xs:int .
	
	<http://pikes.fbk.eu/#char=8,15> a ks:PredicateMention .
	
	<http://pikes.fbk.eu/.naf> a ks:Resource .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=122,132> .
	
	<http://pikes.fbk.eu/#char=26,30;80,84> nif:beginIndex "26"^^xs:int .
	
	<http://pikes.fbk.eu/#char=19,24;95,100> a ks:CompoundString .
	
	<http://pikes.fbk.eu/> dcterms:created "2020-01-24T15:59:54+01:00" .
	
	<http://pikes.fbk.eu/#char=89,93> nif:endIndex "93"^^xs:int ;
		a ks:Mention .
	
	<http://pikes.fbk.eu/#prison> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=111,117> .
	
	<http://pikes.fbk.eu/#char=48,52> a ks:NameMention .
	
	<http://pikes.fbk.eu/#char=104,107> nif:anchorOf "now" .
	
	<http://pikes.fbk.eu/#char=80,84> a ks:NameMention .
	
	<http://pikes.fbk.eu/#char=19,24> a ks:EntityMention .
	
	<http://pikes.fbk.eu/#char=67,72> a ks:Mention .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=0,4;26,30> .
	
	<http://pikes.fbk.eu/#char=48,52> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=104,107> a ks:TimeMention ;
		ks:sst <http://www.newsreader-project.eu/sst/adv.all> .
	
	<http://pikes.fbk.eu/#char=80,84> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=26,30;80,84> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=122,132;137,143> a ks:Mention .
	
	<http://pikes.fbk.eu/> ks:textHash "ITNSFFDMxkFIePKSaq6NRT" .
	
	<http://pikes.fbk.eu/#char=73,79> a ks:PredicateMention .
	
	<http://pikes.fbk.eu/#char=122,132> a ks:PredicateMention .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=31,34> .
	
	<http://pikes.fbk.eu/#char=60,62> nif:endIndex "62"^^xs:int .
	
	<http://pikes.fbk.eu/#char=122,132> ks:sst <http://www.newsreader-project.eu/sst/verb.possession> .
	
	<http://pikes.fbk.eu/#char=19,24;95,100> nif:anchorOf "Peter [...] Peter" ;
		nif:endIndex "100"^^xs:int .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=48,52;89,93> .
	
	<http://pikes.fbk.eu/#char=104,107> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=111,117> ks:sst <http://www.newsreader-project.eu/sst/noun.artifact> ;
		a ks:PredicateMention .
	
	<http://pikes.fbk.eu/#char=48,52;89,93> nif:anchorOf "Jake [...] Jake" .
	
	<http://pikes.fbk.eu/#char=122,132;137,143> a ks:ParticipationMention .
	
	<http://pikes.fbk.eu/#char=95,100> a ks:EntityMention .
	
	<http://pikes.fbk.eu/#char=73,79> ks:synset <http://www.newsreader-project.eu/syn/00355365-v> .
	
	<http://pikes.fbk.eu/#char=95,100;122,132> a ks:CompoundString .
	
	<http://pikes.fbk.eu/#char=8,15> ks:synset <http://www.newsreader-project.eu/syn/02488834-v> .
	
	<http://pikes.fbk.eu/> ks:annotatedWith <http://pikes.fbk.eu/.naf> .
	
	<http://pikes.fbk.eu/#char=48,52;89,93> nif:beginIndex "48"^^xs:int .
	
	<http://pikes.fbk.eu/#char=63,66> a ks:PredicateMention .
	
	<http://pikes.fbk.eu/#why> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=63,66> .
	
	<http://pikes.fbk.eu/#char=8,15;19,24> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=67,72;95,100> ks:componentSubString <http://pikes.fbk.eu/#char=95,100> .
	
	<http://pikes.fbk.eu/#char=111,117> ks:synset <http://www.newsreader-project.eu/syn/04005630-n> .
	
	<http://pikes.fbk.eu/#char=137,143> ks:lemma "murder" .
	
	<http://pikes.fbk.eu/> dcterms:title "" .
	
	<http://pikes.fbk.eu/#char=73,79> ks:sst <http://www.newsreader-project.eu/sst/verb.change> .
	
	<http://pikes.fbk.eu/#char=38,44> ks:sst <http://www.newsreader-project.eu/sst/noun.cognition> .
	
	<http://pikes.fbk.eu/#char=89,93> nif:anchorOf "Jake" .
	
	<http://pikes.fbk.eu/#char=19,24;95,100> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=48,52> a ks:EntityMention .
	
	<entity:jake> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=89,93> .
	
	<http://pikes.fbk.eu/#char=73,79;89,93> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#murder> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=137,143> .
	
	<http://pikes.fbk.eu/#char=48,52;89,93> a ks:CompoundString .
	
	<http://pikes.fbk.eu/#char=38,44;48,52> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=111,117> nif:beginIndex "111"^^xs:int .
	
	<http://pikes.fbk.eu/#char=89,93> nif:beginIndex "89"^^xs:int .
	
	<http://pikes.fbk.eu/#commit> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=122,132> .
	
	<http://pikes.fbk.eu/#char=137,143> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=0,4;80,84> ks:componentSubString <http://pikes.fbk.eu/#char=80,84> .
	
	<http://pikes.fbk.eu/#char=67,79> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=73,84> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=0,4> a ks:NameMention .
	
	<http://pikes.fbk.eu/#char=80,84> nif:anchorOf "Mary" .
	
	<http://pikes.fbk.eu/#char=26,30> nif:beginIndex "26"^^xs:int .
	
	<http://pikes.fbk.eu/#char=31,34> a ks:PredicateMention .
	
	<http://pikes.fbk.eu/#char=67,72> nif:anchorOf "Peter" .
	
	<http://pikes.fbk.eu/#char=0,4> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=111,117> nif:anchorOf "prison" .
	
	<http://pikes.fbk.eu/#have> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=31,34> .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=67,79> .
	
	<http://pikes.fbk.eu/#char=67,72;95,100> a ks:CompoundString .
	
	<http://pikes.fbk.eu/#char=73,79;89,93> nif:beginIndex "73"^^xs:int .
	
	<http://pikes.fbk.eu/#char=122,132;137,143> ks:componentSubString <http://pikes.fbk.eu/#char=122,132> .
	
	<http://pikes.fbk.eu/#char=80,84> a ks:EntityMention .
	
	<http://pikes.fbk.eu/#char=67,79> nif:anchorOf "Peter killed" .
	
	<entity:mary> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=80,84> .
	
	<entity:jake> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=48,52> .
	
	<http://pikes.fbk.eu/#char=38,44> ks:lemma "affair" .
	
	<entity:mary> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=0,4> .
	
	<http://pikes.fbk.eu/#char=73,79;89,93> ks:componentSubString <http://pikes.fbk.eu/#char=73,79> .
	
	<http://pikes.fbk.eu/#char=104,107> nif:beginIndex "104"^^xs:int .
	
	<http://pikes.fbk.eu/#char=122,132> nif:endIndex "132"^^xs:int .
	
	<http://pikes.fbk.eu/#char=48,52;89,93> nif:endIndex "93"^^xs:int .
	
	<http://pikes.fbk.eu/#char=95,100;122,132> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=73,84> nif:beginIndex "73"^^xs:int .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=26,30> .
	
	<http://pikes.fbk.eu/#char=0,4;26,30> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=0,4;80,84> ks:componentSubString <http://pikes.fbk.eu/#char=0,4> .
	
	<http://pikes.fbk.eu/#char=31,34;38,44> ks:componentSubString <http://pikes.fbk.eu/#char=38,44> .
	
	<http://pikes.fbk.eu/#char=26,30> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=38,44> a ks:Mention .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=73,79> .
	
	<http://pikes.fbk.eu/#char=95,100;122,132> a ks:ParticipationMention .
	
	<http://pikes.fbk.eu/#char=38,44;48,52> nif:beginIndex "38"^^xs:int .
	
	<http://pikes.fbk.eu/#char=67,72;95,100> nif:endIndex "100"^^xs:int ;
		nif:anchorOf "Peter [...] Peter" .
	
	<http://pikes.fbk.eu/.naf> ks:version "v3" .
	
	<http://pikes.fbk.eu/#char=48,52;89,93> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=26,30;38,44> nif:anchorOf "Mary [...] affair" ;
		ks:componentSubString <http://pikes.fbk.eu/#char=26,30> .
	
	<http://pikes.fbk.eu/#char=122,132;137,143> nif:anchorOf "committing [...] murder" .
	
	<http://pikes.fbk.eu/#char=73,79> nif:endIndex "79"^^xs:int .
	
	<http://pikes.fbk.eu/#char=0,4;26,30> ks:componentSubString <http://pikes.fbk.eu/#char=26,30> .
	
	<http://pikes.fbk.eu/#char=26,30;38,44> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/> a ks:Resource .
	
	<http://pikes.fbk.eu/#char=26,34> nif:anchorOf "Mary has" .
	
	<http://pikes.fbk.eu/#char=0,4;80,84> nif:beginIndex "0"^^xs:int .
	
	<http://pikes.fbk.eu/#char=73,79;89,93> nif:anchorOf "killed [...] Jake" .
	
	<http://pikes.fbk.eu/#char=26,30;38,44> nif:endIndex "44"^^xs:int .
	
	<http://pikes.fbk.eu/#char=122,132;137,143> nif:beginIndex "122"^^xs:int .
	
	<http://pikes.fbk.eu/#char=95,100;122,132> ks:componentSubString <http://pikes.fbk.eu/#char=122,132> .
	
	<http://pikes.fbk.eu/#char=137,143> a ks:EntityMention .
	
	<http://pikes.fbk.eu/#char=0,4;80,84> nif:endIndex "84"^^xs:int .
	
	<http://pikes.fbk.eu/#char=73,79> nif:anchorOf "killed" .
	
	<http://pikes.fbk.eu/#char=0,4> nif:anchorOf "Mary" .
	
	<http://pikes.fbk.eu/#char=67,72;95,100> a ks:Mention ;
		ks:componentSubString <http://pikes.fbk.eu/#char=67,72> .
	
	<http://pikes.fbk.eu/#char=0,4;8,15> ks:componentSubString <http://pikes.fbk.eu/#char=0,4> .
	
	<http://www.newsreader-project.eu/time/> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=104,107> .
	
	<http://pikes.fbk.eu/#char=19,24> nif:beginIndex "19"^^xs:int .
	
	<http://pikes.fbk.eu/#char=89,93> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=67,72> a ks:NameMention .
	
	<http://pikes.fbk.eu/#char=0,4> a ks:EntityMention .
	
	<http://pikes.fbk.eu/#char=19,24;67,72> nif:beginIndex "19"^^xs:int .
	
	<http://pikes.fbk.eu/#char=67,72> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=0,4;80,84> nif:anchorOf "Mary [...] Mary" .
	
	<http://pikes.fbk.eu/#char=38,44> ks:synset <http://www.newsreader-project.eu/syn/05671325-n> .
	
	<http://pikes.fbk.eu/#char=137,143> nif:anchorOf "murder" .
	
	<http://pikes.fbk.eu/#char=67,79> nif:beginIndex "67"^^xs:int .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=26,30;80,84> .
	
	<http://pikes.fbk.eu/#char=26,30;80,84> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=122,132;137,143> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=63,66> .
	
	<http://pikes.fbk.eu/#char=73,79;89,93> ks:componentSubString <http://pikes.fbk.eu/#char=89,93> .
	
	<http://pikes.fbk.eu/#char=8,15> nif:beginIndex "8"^^xs:int .
	
	<http://pikes.fbk.eu/#char=26,34> nif:beginIndex "26"^^xs:int .
	
	<http://pikes.fbk.eu/#char=89,93> a ks:NameMention .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=0,4;80,84> .
	
	<http://pikes.fbk.eu/#char=60,62> a ks:Mention .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=73,84> .
	
	<http://pikes.fbk.eu/#char=0,4;80,84> a ks:CompoundString .
	
	<http://pikes.fbk.eu/#char=0,4;8,15> nif:beginIndex "0"^^xs:int .
	
	<http://pikes.fbk.eu/#char=19,24;67,72> nif:endIndex "72"^^xs:int .
	
	ks:Stanford%20CoreNLP.null dcterms:title "Stanford CoreNLP" .
	
	<http://pikes.fbk.eu/#char=63,66> nif:endIndex "66"^^xs:int .
	
	<http://pikes.fbk.eu/#char=38,44;48,52> ks:componentSubString <http://pikes.fbk.eu/#char=38,44> .
	
	<http://pikes.fbk.eu/#char=19,24;67,72> ks:componentSubString <http://pikes.fbk.eu/#char=19,24> .
	
	<http://pikes.fbk.eu/#char=8,15> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=122,132> nif:anchorOf "committing" .
	
	<http://pikes.fbk.eu/#char=26,30;80,84> ks:componentSubString <http://pikes.fbk.eu/#char=26,30> .
	
	<http://pikes.fbk.eu/#char=104,107> ks:synset <http://www.newsreader-project.eu/syn/00048739-r> .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=38,44> .
	
	<http://pikes.fbk.eu/#char=26,34> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=137,143> a ks:PredicateMention .
	
	<http://pikes.fbk.eu/#char=19,24;95,100> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=67,72> a ks:EntityMention .
	
	<http://pikes.fbk.eu/#char=26,34> a ks:ParticipationMention .
	
	<http://pikes.fbk.eu/#char=19,24;67,72> a ks:CompoundString .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=89,93> .
	
	<http://pikes.fbk.eu/#char=19,24;67,72> nif:anchorOf "Peter [...] Peter" .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=137,143> .
	
	<http://pikes.fbk.eu/#char=137,143> nif:beginIndex "137"^^xs:int .
	
	<http://pikes.fbk.eu/#char=8,15> nif:endIndex "15"^^xs:int .
	
	<http://pikes.fbk.eu/#char=80,84> nif:endIndex "84"^^xs:int .
	
	<http://pikes.fbk.eu/#char=73,79> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=122,132> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=26,30;38,44> ks:componentSubString <http://pikes.fbk.eu/#char=38,44> .
	
	<http://pikes.fbk.eu/#char=95,100;122,132> nif:beginIndex "95"^^xs:int .
	
	<http://pikes.fbk.eu/#char=31,34;38,44> a ks:CompoundString .
	
	<http://pikes.fbk.eu/#char=31,34> ks:sst <http://www.newsreader-project.eu/sst/verb.body> .
	
	<http://pikes.fbk.eu/#char=89,93> a ks:EntityMention .
	
	<http://pikes.fbk.eu/#char=0,4;8,15> a ks:CompoundString .
	
	<http://pikes.fbk.eu/#char=111,117> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=48,52> nif:beginIndex "48"^^xs:int .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=80,84> .
	
	<http://pikes.fbk.eu/#char=95,100> nif:endIndex "100"^^xs:int .
	
	<http://pikes.fbk.eu/#char=73,79> ks:lemma "kill" .
	
	<http://pikes.fbk.eu/#char=38,44> nif:anchorOf "affair" .
	
	<http://pikes.fbk.eu/#char=38,44;48,52> ks:componentSubString <http://pikes.fbk.eu/#char=48,52> .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=26,30;38,44> , <http://pikes.fbk.eu/#char=0,4> .
	
	<http://pikes.fbk.eu/#char=26,34> nif:endIndex "34"^^xs:int .
	
	<http://pikes.fbk.eu/#char=111,117> a ks:ParticipationMention .
	
	<http://pikes.fbk.eu/.naf> dcterms:creator ks:NAF%20filter.null .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=48,52> .
	
	<http://pikes.fbk.eu/#char=19,24;67,72> ks:componentSubString <http://pikes.fbk.eu/#char=67,72> .
	
	<http://pikes.fbk.eu/.naf> a ks:NAF .
	
	<http://pikes.fbk.eu/#char=0,4;80,84> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=63,66> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=73,84> nif:endIndex "84"^^xs:int .
	
	<http://pikes.fbk.eu/#char=95,100;122,132> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=67,72> nif:beginIndex "67"^^xs:int .
	
	<http://pikes.fbk.eu/#char=38,44> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=0,4;26,30> nif:endIndex "30"^^xs:int .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=67,72;95,100> , <http://pikes.fbk.eu/#char=95,100;122,132> .
	
	<http://pikes.fbk.eu/#char=95,100> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=0,4;26,30> ks:componentSubString <http://pikes.fbk.eu/#char=0,4> .
	
	<http://pikes.fbk.eu/#char=8,15> ks:sst <http://www.newsreader-project.eu/sst/verb.social> .
	
	<http://pikes.fbk.eu/#char=19,24> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=38,44> nif:endIndex "44"^^xs:int .
	
	<http://pikes.fbk.eu/#char=19,24;67,72> a ks:Mention .
	
	<http://pikes.fbk.eu/.naf> dcterms:creator ks:Stanford%20CoreNLP.null .
	
	<http://pikes.fbk.eu/#char=8,15;19,24> ks:componentSubString <http://pikes.fbk.eu/#char=19,24> .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=95,100> .
	
	<http://pikes.fbk.eu/#char=26,30> a ks:NameMention .
	
	<http://pikes.fbk.eu/#char=48,52;89,93> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=0,4> nif:beginIndex "0"^^xs:int .
	
	<http://pikes.fbk.eu/> dcterms:creator "" .
	
	<http://pikes.fbk.eu/#char=67,79> nif:endIndex "79"^^xs:int .
	
	<entity:peter> <http://groundedannotationframework.org/gaf#denotedBy> <http://pikes.fbk.eu/#char=95,100> .
	
	<http://pikes.fbk.eu/#char=122,132;137,143> ks:componentSubString <http://pikes.fbk.eu/#char=137,143> .
	
	<http://pikes.fbk.eu/#char=31,34> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=31,34;38,44> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=26,30> ks:mentionOf <http://pikes.fbk.eu/> .
	
	<http://pikes.fbk.eu/#char=8,15;19,24> a ks:CompoundString .
	
	<http://pikes.fbk.eu/#char=137,143> nif:endIndex "143"^^xs:int .
	
	<http://pikes.fbk.eu/#char=0,4;8,15> a ks:Mention .
	
	<http://pikes.fbk.eu/#char=73,84> nif:anchorOf "killed Mary" .
	
	<http://pikes.fbk.eu/#char=95,100;122,132> nif:anchorOf "Peter [...] committing" .
	
	<http://pikes.fbk.eu/> ks:hasMention <http://pikes.fbk.eu/#char=19,24;67,72> .
	
	<http://pikes.fbk.eu/#char=0,4;8,15> ks:componentSubString <http://pikes.fbk.eu/#char=8,15> .
	
	<http://pikes.fbk.eu/#char=31,34;38,44> a ks:ParticipationMention .
}
@prefix sem: <http://semanticweb.cs.vu.nl/2009/11/sem/> .

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a sem:Event .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:E4ry4_SnVpHI4yV5NWhklp> {
	<http://pikes.fbk.eu/#affair> sem:hasActor <entity:mary> .
}

{
	<fact:E4ry4_SnVpHI4yV5NWhklp> ks:expressedBy <http://pikes.fbk.eu/#char=26,30;38,44> .
}
@prefix eso: <http://www.newsreader-project.eu/domain-ontology#> .

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a eso:EndingARelationship .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a ks:Entity .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:KVn_wDBmZo1OZ0cGSgt2nq> {
	<entity:mary> a <http://www.newsreader-project.eu/ontologies/PERSON> .
}

{
	<fact:KVn_wDBmZo1OZ0cGSgt2nq> ks:expressedBy <http://pikes.fbk.eu/#char=0,4> , <http://pikes.fbk.eu/#char=26,30> , <http://pikes.fbk.eu/#char=80,84> .
}
@prefix pm: <http://premon.fbk.eu/resource/> .

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a pm:nb10-affair.02 .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}
@prefix frb: <http://framebase.org/ns/> .

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a frb:frame-Commitment-commit.v .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:B-WGITSRAV7JL_C4piF7Gd> {
	<http://pikes.fbk.eu/#prison_2> a pm:fn15-prison .
}

{
	<fact:B-WGITSRAV7JL_C4piF7Gd> ks:expressedBy <http://pikes.fbk.eu/#char=111,117> .
}
@prefix sumo: <http://www.ontologyportal.org/SUMO.owl#> .

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a sumo:InternalChange .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:D3wV2iCTgm3Hm8zm7st-jC> {
	<http://pikes.fbk.eu/#kill> <http://premon.fbk.eu/resource/vb32-kill-42.3@agent> <entity:peter> .
}

{
	<fact:D3wV2iCTgm3Hm8zm7st-jC> ks:expressedBy <http://pikes.fbk.eu/#char=67,79> .
}

<fact:B-WGITSRAV7JL_C4piF7Gd> {
	<http://pikes.fbk.eu/#prison_2> a frb:frame-Prison-prison.n .
}

{
	<fact:B-WGITSRAV7JL_C4piF7Gd> ks:expressedBy <http://pikes.fbk.eu/#char=111,117> .
}

<fact:AAAAAAAAAAAAAAAAAAAAAA> {
	<attr:be-1v> ks:headSynset <http://wordnet-rdf.princeton.edu/wn30/02604760-v> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> <http://www.newsreader-project.eu/domain-ontology#BeginningARelationship@relationship-partner_1> <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a pm:fn15-point_of_dispute .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:ContentBearingProcess .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a pm:fn15-possession .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a sumo:Entity .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sem:Event .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a frb:frame-Killing-kill.v .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:AAAAAAAAAAAAAAAAAAAAAA> {
	<attr:be-1v> a ks:Attribute .
}

<fact:JU0CIi5LZ2wM1Bh7gmKw0x> {
	<http://pikes.fbk.eu/#commit> frb:fe-Commitment-Speaker <entity:peter> .
}

{
	<fact:JU0CIi5LZ2wM1Bh7gmKw0x> ks:expressedBy <http://pikes.fbk.eu/#char=95,100;122,132> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> rdfs:label "has" .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:Ceremony .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:DPAvtwr9CJzAhuYxv2LUrq> {
	<http://www.newsreader-project.eu/time/> rdfs:label "now" .
}

{
	<fact:DPAvtwr9CJzAhuYxv2LUrq> ks:expressedBy <http://pikes.fbk.eu/#char=104,107> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a pm:fn15-personal_relationship .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a pm:pb17-have.03 .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> rdfs:label "murder" .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> sem:hasActor <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}

<fact:N7G6MgxljzhOnT10zSYzcs> {
	<http://pikes.fbk.eu/#kill> sem:hasActor <entity:jake> .
}

{
	<fact:N7G6MgxljzhOnT10zSYzcs> ks:expressedBy <http://pikes.fbk.eu/#char=73,79;89,93> .
}

<fact:N7G6MgxljzhOnT10zSYzcs> {
	<http://pikes.fbk.eu/#kill> <http://www.newsreader-project.eu/domain-ontology#Killing@destroying-theme> <entity:jake> .
}

{
	<fact:N7G6MgxljzhOnT10zSYzcs> ks:expressedBy <http://pikes.fbk.eu/#char=73,79;89,93> .
}

<fact:B-WGITSRAV7JL_C4piF7Gd> {
	<http://pikes.fbk.eu/#prison> a ks:Entity .
}

{
	<fact:B-WGITSRAV7JL_C4piF7Gd> ks:expressedBy <http://pikes.fbk.eu/#char=111,117> .
}

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a sumo:InternalAttribute .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a sumo:Physical .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a sumo:Physical .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:GtagZXzSvVMKavhR4EkF2r> {
	<http://pikes.fbk.eu/#affair> <http://premon.fbk.eu/resource/fn15-point_of_dispute@question> <entity:jake> .
}

{
	<fact:GtagZXzSvVMKavhR4EkF2r> ks:expressedBy <http://pikes.fbk.eu/#char=38,44;48,52> .
}

<fact:B-WGITSRAV7JL_C4piF7Gd> {
	<http://pikes.fbk.eu/#prison_2> a ks:Predicate .
}

{
	<fact:B-WGITSRAV7JL_C4piF7Gd> ks:expressedBy <http://pikes.fbk.eu/#char=111,117> .
}

<fact:AqRe31pZEliId1FlO4xsw6> {
	<http://pikes.fbk.eu/#marry> <http://premon.fbk.eu/resource/pb17-marry.01@arg2> <entity:peter> .
}

{
	<fact:AqRe31pZEliId1FlO4xsw6> ks:expressedBy <http://pikes.fbk.eu/#char=8,15;19,24> .
}

<fact:DlgLLbJuj06EzRLdWXDxZC> {
	<http://pikes.fbk.eu/#have> <http://premon.fbk.eu/resource/vb32-have-100@pivot> <entity:mary> .
}

{
	<fact:DlgLLbJuj06EzRLdWXDxZC> ks:expressedBy <http://pikes.fbk.eu/#char=26,34> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> <http://premon.fbk.eu/resource/pb17-marry.01@arg1> <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}
@prefix dbyago: <http://dbpedia.org/class/yago/> .

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a dbyago:Matter105671325 .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:E4ry4_SnVpHI4yV5NWhklp> {
	<http://pikes.fbk.eu/#affair> <http://premon.fbk.eu/resource/nb10-affair.02@arg0> <entity:mary> .
}

{
	<fact:E4ry4_SnVpHI4yV5NWhklp> ks:expressedBy <http://pikes.fbk.eu/#char=26,30;38,44> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a pm:pb17-kill.01 .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:DPAvtwr9CJzAhuYxv2LUrq> {
	<http://www.newsreader-project.eu/time/> a owltime:DateTimeInterval .
}

{
	<fact:DPAvtwr9CJzAhuYxv2LUrq> ks:expressedBy <http://pikes.fbk.eu/#char=104,107> .
}

<fact:FcA-qOqmnDjKEnFeqf2NEn> {
	<http://pikes.fbk.eu/#kill> <http://premon.fbk.eu/resource/fn15-killing@victim> <entity:mary> .
}

{
	<fact:FcA-qOqmnDjKEnFeqf2NEn> ks:expressedBy <http://pikes.fbk.eu/#char=73,84> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a sumo:LinguisticCommunication .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a pm:pb17-commit.02 .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:B-WGITSRAV7JL_C4piF7Gd> {
	<http://pikes.fbk.eu/#prison_2> a sem:Event .
}

{
	<fact:B-WGITSRAV7JL_C4piF7Gd> ks:expressedBy <http://pikes.fbk.eu/#char=111,117> .
}

<fact:DlgLLbJuj06EzRLdWXDxZC> {
	<http://pikes.fbk.eu/#have> sem:hasActor <entity:mary> .
}

{
	<fact:DlgLLbJuj06EzRLdWXDxZC> ks:expressedBy <http://pikes.fbk.eu/#char=26,34> .
}

<fact:PmqGmTbiek2J96YfPqHcBE> {
	<http://pikes.fbk.eu/#have> sem:hasActor <http://pikes.fbk.eu/#affair> .
}

{
	<fact:PmqGmTbiek2J96YfPqHcBE> ks:expressedBy <http://pikes.fbk.eu/#char=31,34;38,44> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> rdfs:label "married" .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a ks:Predicate .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:IvtEoKvKDdGKBxefvKD7Fr> {
	<http://pikes.fbk.eu/#commit> sem:hasActor <http://pikes.fbk.eu/#murder> .
}

{
	<fact:IvtEoKvKDdGKBxefvKD7Fr> ks:expressedBy <http://pikes.fbk.eu/#char=122,132;137,143> .
}

<fact:DlgLLbJuj06EzRLdWXDxZC> {
	<http://pikes.fbk.eu/#have> <http://premon.fbk.eu/resource/fn15-possession@owner> <entity:mary> .
}

{
	<fact:DlgLLbJuj06EzRLdWXDxZC> ks:expressedBy <http://pikes.fbk.eu/#char=26,34> .
}

<fact:FcA-qOqmnDjKEnFeqf2NEn> {
	<http://pikes.fbk.eu/#kill> frb:fe-Killing-Victim <entity:mary> .
}

{
	<fact:FcA-qOqmnDjKEnFeqf2NEn> ks:expressedBy <http://pikes.fbk.eu/#char=73,84> .
}

<fact:B-WGITSRAV7JL_C4piF7Gd> {
	<http://pikes.fbk.eu/#prison_2> <http://premon.fbk.eu/resource/fn15-prison@penal_institution> <http://pikes.fbk.eu/#prison> .
}

{
	<fact:B-WGITSRAV7JL_C4piF7Gd> ks:expressedBy <http://pikes.fbk.eu/#char=111,117> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:Declaring .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:IO046vChT5INqE00JPL9yY> {
	<entity:jake> rdfs:label "Jake" .
}

{
	<fact:IO046vChT5INqE00JPL9yY> ks:expressedBy <http://pikes.fbk.eu/#char=48,52> , <http://pikes.fbk.eu/#char=89,93> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a sumo:Process .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a sumo:Communication .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> frb:fe-Personal_relationship-Partner_1 <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a dbyago:Murder100220522 .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a sumo:BiologicalAttribute .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:KVn_wDBmZo1OZ0cGSgt2nq> {
	<entity:mary> a ks:Entity .
}

{
	<fact:KVn_wDBmZo1OZ0cGSgt2nq> ks:expressedBy <http://pikes.fbk.eu/#char=0,4> , <http://pikes.fbk.eu/#char=26,30> , <http://pikes.fbk.eu/#char=80,84> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a pm:vb32-have-100 .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a eso:BeginningARelationship .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:Process .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a ks:Predicate .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}
@prefix dbpedia: <http://dbpedia.org/resource/> .

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> rdfs:seeAlso dbpedia:Affair .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a sumo:Destruction .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:N7G6MgxljzhOnT10zSYzcs> {
	<http://pikes.fbk.eu/#kill> <http://premon.fbk.eu/resource/vb32-kill-42.3@patient> <entity:jake> .
}

{
	<fact:N7G6MgxljzhOnT10zSYzcs> ks:expressedBy <http://pikes.fbk.eu/#char=73,79;89,93> .
}
@prefix owl: <http://www.w3.org/2002/07/owl#> .

<fact:MRiweE2yofsKF4A7tEWOCC> {
	<entity:mary> owl:sameAs <entity:mary> .
}

{
	<fact:MRiweE2yofsKF4A7tEWOCC> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;26,30> , <http://pikes.fbk.eu/#char=0,4;80,84> , <http://pikes.fbk.eu/#char=26,30;80,84> .
}

<fact:IZoNnD9GWpoBb1MvNjbtUA> {
	<http://pikes.fbk.eu/#why> a pm:fn15-reason .
}

{
	<fact:IZoNnD9GWpoBb1MvNjbtUA> ks:expressedBy <http://pikes.fbk.eu/#char=63,66> .
}

<fact:DPAvtwr9CJzAhuYxv2LUrq> {
	<http://www.newsreader-project.eu/time/> a ks:Entity .
}

{
	<fact:DPAvtwr9CJzAhuYxv2LUrq> ks:expressedBy <http://pikes.fbk.eu/#char=104,107> .
}

<fact:B-WGITSRAV7JL_C4piF7Gd> {
	<http://pikes.fbk.eu/#prison> rdfs:label "prison" .
}

{
	<fact:B-WGITSRAV7JL_C4piF7Gd> ks:expressedBy <http://pikes.fbk.eu/#char=111,117> .
}

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a sem:Event .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:IntentionalProcess .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:BWPBkBEIMwICvBlJ1kYs5R> {
	<entity:peter> a <http://www.newsreader-project.eu/ontologies/PERSON> .
}

{
	<fact:BWPBkBEIMwICvBlJ1kYs5R> ks:expressedBy <http://pikes.fbk.eu/#char=19,24> , <http://pikes.fbk.eu/#char=67,72> , <http://pikes.fbk.eu/#char=95,100> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a sumo:SocialInteraction .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:JV4oJvKp1aWIfqDDJ0LukT> {
	<entity:jake> ks:mod <attr:be-1v> .
}

{
	<fact:JV4oJvKp1aWIfqDDJ0LukT> ks:expressedBy <http://pikes.fbk.eu/#char=60,62> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a sumo:Physical .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:E4KO2UbjT6CIO3j2on8aCk> {
	<entity:peter> owl:sameAs <entity:peter> .
}

{
	<fact:E4KO2UbjT6CIO3j2on8aCk> ks:expressedBy <http://pikes.fbk.eu/#char=19,24;67,72> , <http://pikes.fbk.eu/#char=19,24;95,100> , <http://pikes.fbk.eu/#char=67,72;95,100> .
}

<fact:PmqGmTbiek2J96YfPqHcBE> {
	<http://pikes.fbk.eu/#have> <http://www.newsreader-project.eu/domain-ontology#HavingInPossession@possession-theme> <http://pikes.fbk.eu/#affair> .
}

{
	<fact:PmqGmTbiek2J96YfPqHcBE> ks:expressedBy <http://pikes.fbk.eu/#char=31,34;38,44> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a sumo:Damaging .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:Entity .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a sumo:Damaging .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:AqRe31pZEliId1FlO4xsw6> {
	<http://pikes.fbk.eu/#marry> <http://www.newsreader-project.eu/domain-ontology#EndingARelationship@relationship-partner_2> <entity:peter> .
}

{
	<fact:AqRe31pZEliId1FlO4xsw6> ks:expressedBy <http://pikes.fbk.eu/#char=8,15;19,24> .
}

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a sumo:Entity .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a sumo:Entity .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:D3wV2iCTgm3Hm8zm7st-jC> {
	<http://pikes.fbk.eu/#kill> sem:hasActor <entity:peter> .
}

{
	<fact:D3wV2iCTgm3Hm8zm7st-jC> ks:expressedBy <http://pikes.fbk.eu/#char=67,79> .
}

<fact:DlgLLbJuj06EzRLdWXDxZC> {
	<http://pikes.fbk.eu/#have> <http://premon.fbk.eu/resource/pb17-have.03@arg0> <entity:mary> .
}

{
	<fact:DlgLLbJuj06EzRLdWXDxZC> ks:expressedBy <http://pikes.fbk.eu/#char=26,34> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a eso:HavingInPossession .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a sumo:Killing .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a ks:Entity .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a pm:fn15-killing .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:DPAvtwr9CJzAhuYxv2LUrq> {
	<http://www.newsreader-project.eu/time/> a sumo:SubjectiveAssessmentAttribute .
}

{
	<fact:DPAvtwr9CJzAhuYxv2LUrq> ks:expressedBy <http://pikes.fbk.eu/#char=104,107> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a ks:Entity .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:KVn_wDBmZo1OZ0cGSgt2nq> {
	<entity:mary> rdfs:label "Mary" .
}

{
	<fact:KVn_wDBmZo1OZ0cGSgt2nq> ks:expressedBy <http://pikes.fbk.eu/#char=0,4> , <http://pikes.fbk.eu/#char=26,30> , <http://pikes.fbk.eu/#char=80,84> .
}

<fact:DPAvtwr9CJzAhuYxv2LUrq> {
	<http://www.newsreader-project.eu/time/> a sumo:NormativeAttribute .
}

{
	<fact:DPAvtwr9CJzAhuYxv2LUrq> ks:expressedBy <http://pikes.fbk.eu/#char=104,107> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a sumo:IntentionalProcess .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:IZoNnD9GWpoBb1MvNjbtUA> {
	<http://pikes.fbk.eu/#why> a ks:Entity .
}

{
	<fact:IZoNnD9GWpoBb1MvNjbtUA> ks:expressedBy <http://pikes.fbk.eu/#char=63,66> .
}

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> rdfs:label "affair" .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a pm:pb17-marry.01 .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:IZoNnD9GWpoBb1MvNjbtUA> {
	<http://pikes.fbk.eu/#why> a sem:Event .
}

{
	<fact:IZoNnD9GWpoBb1MvNjbtUA> ks:expressedBy <http://pikes.fbk.eu/#char=63,66> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a pm:fn15-commitment .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> <http://www.newsreader-project.eu/domain-ontology#BeginningARelationship@relationship-partner_2> <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a sumo:Abstract .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a frb:frame-Possession-own.v .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> <http://www.newsreader-project.eu/domain-ontology#BeginningARelationship@relationship-partners> <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a sumo:Committing .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> <http://premon.fbk.eu/resource/vb32-marry-36.2@co-agent> <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:Physical .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a ks:Predicate .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:FcA-qOqmnDjKEnFeqf2NEn> {
	<http://pikes.fbk.eu/#kill> <http://premon.fbk.eu/resource/pb17-kill.01@arg1> <entity:mary> .
}

{
	<fact:FcA-qOqmnDjKEnFeqf2NEn> ks:expressedBy <http://pikes.fbk.eu/#char=73,84> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a pm:vb32-kill-42.3 .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a eso:Killing .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

<fact:IO046vChT5INqE00JPL9yY> {
	<entity:jake> foaf:name "Jake" .
}

{
	<fact:IO046vChT5INqE00JPL9yY> ks:expressedBy <http://pikes.fbk.eu/#char=48,52> , <http://pikes.fbk.eu/#char=89,93> .
}

<fact:AqRe31pZEliId1FlO4xsw6> {
	<http://pikes.fbk.eu/#marry> sem:hasActor <entity:peter> .
}

{
	<fact:AqRe31pZEliId1FlO4xsw6> ks:expressedBy <http://pikes.fbk.eu/#char=8,15;19,24> .
}

<fact:B-WGITSRAV7JL_C4piF7Gd> {
	<http://pikes.fbk.eu/#prison> rdfs:seeAlso dbpedia:Prison .
}

{
	<fact:B-WGITSRAV7JL_C4piF7Gd> ks:expressedBy <http://pikes.fbk.eu/#char=111,117> .
}

<fact:B-WGITSRAV7JL_C4piF7Gd> {
	<http://pikes.fbk.eu/#prison_2> frb:fe-Prison-Penal_institution <http://pikes.fbk.eu/#prison> .
}

{
	<fact:B-WGITSRAV7JL_C4piF7Gd> ks:expressedBy <http://pikes.fbk.eu/#char=111,117> .
}

<fact:BWPBkBEIMwICvBlJ1kYs5R> {
	<entity:peter> foaf:name "Peter" .
}

{
	<fact:BWPBkBEIMwICvBlJ1kYs5R> ks:expressedBy <http://pikes.fbk.eu/#char=19,24> , <http://pikes.fbk.eu/#char=67,72> , <http://pikes.fbk.eu/#char=95,100> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> rdfs:label "killed" .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:DlgLLbJuj06EzRLdWXDxZC> {
	<http://pikes.fbk.eu/#have> frb:fe-Possession-Owner <entity:mary> .
}

{
	<fact:DlgLLbJuj06EzRLdWXDxZC> ks:expressedBy <http://pikes.fbk.eu/#char=26,34> .
}

<fact:AqRe31pZEliId1FlO4xsw6> {
	<http://pikes.fbk.eu/#marry> <http://www.newsreader-project.eu/domain-ontology#EndingARelationship@relationship-partners> <entity:peter> .
}

{
	<fact:AqRe31pZEliId1FlO4xsw6> ks:expressedBy <http://pikes.fbk.eu/#char=8,15;19,24> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:SocialInteraction .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a sumo:IntentionalProcess .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:DPAvtwr9CJzAhuYxv2LUrq> {
	<http://www.newsreader-project.eu/time/> a sumo:Entity .
}

{
	<fact:DPAvtwr9CJzAhuYxv2LUrq> ks:expressedBy <http://pikes.fbk.eu/#char=104,107> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a ks:Entity .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a sumo:Process .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:IO046vChT5INqE00JPL9yY> {
	<entity:jake> a <http://www.newsreader-project.eu/ontologies/PERSON> .
}

{
	<fact:IO046vChT5INqE00JPL9yY> ks:expressedBy <http://pikes.fbk.eu/#char=48,52> , <http://pikes.fbk.eu/#char=89,93> .
}

<fact:N7G6MgxljzhOnT10zSYzcs> {
	<http://pikes.fbk.eu/#kill> <http://premon.fbk.eu/resource/fn15-killing@victim> <entity:jake> .
}

{
	<fact:N7G6MgxljzhOnT10zSYzcs> ks:expressedBy <http://pikes.fbk.eu/#char=73,79;89,93> .
}

<fact:AqRe31pZEliId1FlO4xsw6> {
	<http://pikes.fbk.eu/#marry> <http://www.newsreader-project.eu/domain-ontology#BeginningARelationship@relationship-partner_2> <entity:peter> .
}

{
	<fact:AqRe31pZEliId1FlO4xsw6> ks:expressedBy <http://pikes.fbk.eu/#char=8,15;19,24> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a ks:Entity .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a sem:Event .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:IO046vChT5INqE00JPL9yY> {
	<entity:jake> a ks:Entity .
}

{
	<fact:IO046vChT5INqE00JPL9yY> ks:expressedBy <http://pikes.fbk.eu/#char=48,52> , <http://pikes.fbk.eu/#char=89,93> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a ks:Predicate .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:N7G6MgxljzhOnT10zSYzcs> {
	<http://pikes.fbk.eu/#kill> frb:fe-Killing-Victim <entity:jake> .
}

{
	<fact:N7G6MgxljzhOnT10zSYzcs> ks:expressedBy <http://pikes.fbk.eu/#char=73,79;89,93> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> <http://www.newsreader-project.eu/domain-ontology#EndingARelationship@relationship-partner_2> <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}

<fact:DPAvtwr9CJzAhuYxv2LUrq> {
	<http://www.newsreader-project.eu/time/> a sumo:RelationalAttribute .
}

{
	<fact:DPAvtwr9CJzAhuYxv2LUrq> ks:expressedBy <http://pikes.fbk.eu/#char=104,107> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a sumo:ContentBearingProcess .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a pm:vb32-marry-36.2 .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:PmqGmTbiek2J96YfPqHcBE> {
	<http://pikes.fbk.eu/#have> <http://premon.fbk.eu/resource/vb32-have-100@theme> <http://pikes.fbk.eu/#affair> .
}

{
	<fact:PmqGmTbiek2J96YfPqHcBE> ks:expressedBy <http://pikes.fbk.eu/#char=31,34;38,44> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a ks:Predicate .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a sumo:Physical .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:FcA-qOqmnDjKEnFeqf2NEn> {
	<http://pikes.fbk.eu/#kill> <http://www.newsreader-project.eu/domain-ontology#Killing@destroying-theme> <entity:mary> .
}

{
	<fact:FcA-qOqmnDjKEnFeqf2NEn> ks:expressedBy <http://pikes.fbk.eu/#char=73,84> .
}

<fact:IZoNnD9GWpoBb1MvNjbtUA> {
	<http://pikes.fbk.eu/#why> rdfs:label "why" .
}

{
	<fact:IZoNnD9GWpoBb1MvNjbtUA> ks:expressedBy <http://pikes.fbk.eu/#char=63,66> .
}

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a sumo:Attribute .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:DPAvtwr9CJzAhuYxv2LUrq> {
	<http://www.newsreader-project.eu/time/> a ks:Time .
}

{
	<fact:DPAvtwr9CJzAhuYxv2LUrq> ks:expressedBy <http://pikes.fbk.eu/#char=104,107> .
}

<fact:DPAvtwr9CJzAhuYxv2LUrq> {
	<http://www.newsreader-project.eu/time/> a sumo:Abstract .
}

{
	<fact:DPAvtwr9CJzAhuYxv2LUrq> ks:expressedBy <http://pikes.fbk.eu/#char=104,107> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a sem:Event .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:PmqGmTbiek2J96YfPqHcBE> {
	<http://pikes.fbk.eu/#have> <http://premon.fbk.eu/resource/pb17-have.03@arg1> <http://pikes.fbk.eu/#affair> .
}

{
	<fact:PmqGmTbiek2J96YfPqHcBE> ks:expressedBy <http://pikes.fbk.eu/#char=31,34;38,44> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> rdfs:label "committing" .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a sumo:InternalChange .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:AAAAAAAAAAAAAAAAAAAAAA> {
	<attr:be-1v> rdfs:label "is" .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:Wedding .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:B-WGITSRAV7JL_C4piF7Gd> {
	<http://pikes.fbk.eu/#prison> a dbyago:Prison104005630 .
}

{
	<fact:B-WGITSRAV7JL_C4piF7Gd> ks:expressedBy <http://pikes.fbk.eu/#char=111,117> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:ContentBearingPhysical .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a ks:Entity .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:IvtEoKvKDdGKBxefvKD7Fr> {
	<http://pikes.fbk.eu/#commit> <http://premon.fbk.eu/resource/pb17-commit.02@arg1> <http://pikes.fbk.eu/#murder> .
}

{
	<fact:IvtEoKvKDdGKBxefvKD7Fr> ks:expressedBy <http://pikes.fbk.eu/#char=122,132;137,143> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:Communication .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a ks:Predicate .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:D3wV2iCTgm3Hm8zm7st-jC> {
	<http://pikes.fbk.eu/#kill> <http://premon.fbk.eu/resource/pb17-kill.01@arg0> <entity:peter> .
}

{
	<fact:D3wV2iCTgm3Hm8zm7st-jC> ks:expressedBy <http://pikes.fbk.eu/#char=67,79> .
}

<fact:KyKdew8eKLyLnc8vnoXVJX> {
	<http://pikes.fbk.eu/#affair> a sumo:PsychologicalAttribute .
}

{
	<fact:KyKdew8eKLyLnc8vnoXVJX> ks:expressedBy <http://pikes.fbk.eu/#char=38,44> .
}

<fact:N7G6MgxljzhOnT10zSYzcs> {
	<http://pikes.fbk.eu/#kill> <http://premon.fbk.eu/resource/pb17-kill.01@arg1> <entity:jake> .
}

{
	<fact:N7G6MgxljzhOnT10zSYzcs> ks:expressedBy <http://pikes.fbk.eu/#char=73,79;89,93> .
}

<fact:DPAvtwr9CJzAhuYxv2LUrq> {
	<http://www.newsreader-project.eu/time/> a sumo:Attribute .
}

{
	<fact:DPAvtwr9CJzAhuYxv2LUrq> ks:expressedBy <http://pikes.fbk.eu/#char=104,107> .
}

<fact:GtagZXzSvVMKavhR4EkF2r> {
	<http://pikes.fbk.eu/#affair> ks:mod <entity:jake> .
}

{
	<fact:GtagZXzSvVMKavhR4EkF2r> ks:expressedBy <http://pikes.fbk.eu/#char=38,44;48,52> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a sumo:Process .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:G7wdakF2tW3KWOFUBZvzo1> {
	<http://pikes.fbk.eu/#have> a sumo:Entity .
}

{
	<fact:G7wdakF2tW3KWOFUBZvzo1> ks:expressedBy <http://pikes.fbk.eu/#char=31,34> .
}

<fact:DlgLLbJuj06EzRLdWXDxZC> {
	<http://pikes.fbk.eu/#have> <http://www.newsreader-project.eu/domain-ontology#HavingInPossession@possession-owner> <entity:mary> .
}

{
	<fact:DlgLLbJuj06EzRLdWXDxZC> ks:expressedBy <http://pikes.fbk.eu/#char=26,34> .
}

<fact:KVn_wDBmZo1OZ0cGSgt2nq> {
	<entity:mary> foaf:name "Mary" .
}

{
	<fact:KVn_wDBmZo1OZ0cGSgt2nq> ks:expressedBy <http://pikes.fbk.eu/#char=0,4> , <http://pikes.fbk.eu/#char=26,30> , <http://pikes.fbk.eu/#char=80,84> .
}

<fact:BWPBkBEIMwICvBlJ1kYs5R> {
	<entity:peter> rdfs:label "Peter" .
}

{
	<fact:BWPBkBEIMwICvBlJ1kYs5R> ks:expressedBy <http://pikes.fbk.eu/#char=19,24> , <http://pikes.fbk.eu/#char=67,72> , <http://pikes.fbk.eu/#char=95,100> .
}

<fact:PmqGmTbiek2J96YfPqHcBE> {
	<http://pikes.fbk.eu/#have> <http://premon.fbk.eu/resource/fn15-possession@possession> <http://pikes.fbk.eu/#affair> .
}

{
	<fact:PmqGmTbiek2J96YfPqHcBE> ks:expressedBy <http://pikes.fbk.eu/#char=31,34;38,44> .
}

<fact:BWPBkBEIMwICvBlJ1kYs5R> {
	<entity:peter> a ks:Entity .
}

{
	<fact:BWPBkBEIMwICvBlJ1kYs5R> ks:expressedBy <http://pikes.fbk.eu/#char=19,24> , <http://pikes.fbk.eu/#char=67,72> , <http://pikes.fbk.eu/#char=95,100> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a sumo:Entity .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:GtagZXzSvVMKavhR4EkF2r> {
	<http://pikes.fbk.eu/#affair> sem:hasActor <entity:jake> .
}

{
	<fact:GtagZXzSvVMKavhR4EkF2r> ks:expressedBy <http://pikes.fbk.eu/#char=38,44;48,52> .
}

<fact:D3wV2iCTgm3Hm8zm7st-jC> {
	<http://pikes.fbk.eu/#kill> <http://premon.fbk.eu/resource/fn15-killing@killer> <entity:peter> .
}

{
	<fact:D3wV2iCTgm3Hm8zm7st-jC> ks:expressedBy <http://pikes.fbk.eu/#char=67,79> .
}

<fact:OKxRsjHKWuYANdAKYXW7X3> {
	<entity:jake> owl:sameAs <entity:jake> .
}

{
	<fact:OKxRsjHKWuYANdAKYXW7X3> ks:expressedBy <http://pikes.fbk.eu/#char=48,52;89,93> .
}

<fact:D3wV2iCTgm3Hm8zm7st-jC> {
	<http://pikes.fbk.eu/#kill> frb:fe-Killing-Killer <entity:peter> .
}

{
	<fact:D3wV2iCTgm3Hm8zm7st-jC> ks:expressedBy <http://pikes.fbk.eu/#char=67,79> .
}

<fact:JU0CIi5LZ2wM1Bh7gmKw0x> {
	<http://pikes.fbk.eu/#commit> <http://premon.fbk.eu/resource/fn15-commitment@speaker> <entity:peter> .
}

{
	<fact:JU0CIi5LZ2wM1Bh7gmKw0x> ks:expressedBy <http://pikes.fbk.eu/#char=95,100;122,132> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a sumo:Process .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a sumo:ContentBearingPhysical .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:GtagZXzSvVMKavhR4EkF2r> {
	<http://pikes.fbk.eu/#affair> frb:fe-Point_of_dispute-Question <entity:jake> .
}

{
	<fact:GtagZXzSvVMKavhR4EkF2r> ks:expressedBy <http://pikes.fbk.eu/#char=38,44;48,52> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> a frb:frame-Killing-kill.v .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:B-WGITSRAV7JL_C4piF7Gd> {
	<http://pikes.fbk.eu/#prison_2> a ks:Entity .
}

{
	<fact:B-WGITSRAV7JL_C4piF7Gd> ks:expressedBy <http://pikes.fbk.eu/#char=111,117> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> <http://www.newsreader-project.eu/domain-ontology#EndingARelationship@relationship-partner_1> <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}

<fact:JHGgQ1BY4rhOF8YIHs2oer> {
	<http://pikes.fbk.eu/#commit> a sem:Event .
}

{
	<fact:JHGgQ1BY4rhOF8YIHs2oer> ks:expressedBy <http://pikes.fbk.eu/#char=122,132> .
}

<fact:BuyhFoeVMPHC4_iXqLHtT_> {
	<http://pikes.fbk.eu/#murder> rdfs:seeAlso dbpedia:Murder .
}

{
	<fact:BuyhFoeVMPHC4_iXqLHtT_> ks:expressedBy <http://pikes.fbk.eu/#char=137,143> .
}

<fact:IZoNnD9GWpoBb1MvNjbtUA> {
	<http://pikes.fbk.eu/#why> a ks:Predicate .
}

{
	<fact:IZoNnD9GWpoBb1MvNjbtUA> ks:expressedBy <http://pikes.fbk.eu/#char=63,66> .
}

<fact:PmqGmTbiek2J96YfPqHcBE> {
	<http://pikes.fbk.eu/#have> frb:fe-Possession-Possession <http://pikes.fbk.eu/#affair> .
}

{
	<fact:PmqGmTbiek2J96YfPqHcBE> ks:expressedBy <http://pikes.fbk.eu/#char=31,34;38,44> .
}

<fact:Jzaoc2wTxsXBgHX6-xy465> {
	<http://pikes.fbk.eu/#kill> a pm:fn15-killing .
}

{
	<fact:Jzaoc2wTxsXBgHX6-xy465> ks:expressedBy <http://pikes.fbk.eu/#char=73,79> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> <http://premon.fbk.eu/resource/fn15-personal_relationship@partner_1> <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}

<fact:NxBsWNqtHMXIyhygjettfs> {
	<http://pikes.fbk.eu/#marry> a sumo:LinguisticCommunication .
}

{
	<fact:NxBsWNqtHMXIyhygjettfs> ks:expressedBy <http://pikes.fbk.eu/#char=8,15> .
}

<fact:AqRe31pZEliId1FlO4xsw6> {
	<http://pikes.fbk.eu/#marry> <http://premon.fbk.eu/resource/vb32-marry-36.2@co-agent> <entity:peter> .
}

{
	<fact:AqRe31pZEliId1FlO4xsw6> ks:expressedBy <http://pikes.fbk.eu/#char=8,15;19,24> .
}

<fact:GtagZXzSvVMKavhR4EkF2r> {
	<http://pikes.fbk.eu/#affair> <http://premon.fbk.eu/resource/nb10-affair.02@arg1> <entity:jake> .
}

{
	<fact:GtagZXzSvVMKavhR4EkF2r> ks:expressedBy <http://pikes.fbk.eu/#char=38,44;48,52> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> <http://premon.fbk.eu/resource/vb32-marry-36.2@agent> <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}

<fact:CN_2L0tPDWfLfGIDab5YUn> {
	<http://pikes.fbk.eu/#marry> <http://www.newsreader-project.eu/domain-ontology#EndingARelationship@relationship-partners> <entity:mary> .
}

{
	<fact:CN_2L0tPDWfLfGIDab5YUn> ks:expressedBy <http://pikes.fbk.eu/#char=0,4;8,15> .
}

<fact:FcA-qOqmnDjKEnFeqf2NEn> {
	<http://pikes.fbk.eu/#kill> <http://premon.fbk.eu/resource/vb32-kill-42.3@patient> <entity:mary> .
}

{
	<fact:FcA-qOqmnDjKEnFeqf2NEn> ks:expressedBy <http://pikes.fbk.eu/#char=73,84> .
}

<fact:AqRe31pZEliId1FlO4xsw6> {
	<http://pikes.fbk.eu/#marry> <http://www.newsreader-project.eu/domain-ontology#BeginningARelationship@relationship-partners> <entity:peter> .
}

{
	<fact:AqRe31pZEliId1FlO4xsw6> ks:expressedBy <http://pikes.fbk.eu/#char=8,15;19,24> .
}

<fact:FcA-qOqmnDjKEnFeqf2NEn> {
	<http://pikes.fbk.eu/#kill> sem:hasActor <entity:mary> .
}

{
	<fact:FcA-qOqmnDjKEnFeqf2NEn> ks:expressedBy <http://pikes.fbk.eu/#char=73,84> .
}   """
    return (test1, test2, test3)
