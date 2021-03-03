#!/usr/bin/env bash
INPUT=data/json_format/pegasus_xsum_beam8_minlen5_3mc
OUTPUT=data/indexes/lucene-index-pegasus_xsum_beam8_minlen5_3mc

if [ ! -d "${OUTPUT}" ]
then 
    sh ./anserini/target/appassembler/bin/IndexCollection -collection JsonCollection \
    -generator DefaultLuceneDocumentGenerator -threads 1 \
    -input ${INPUT} \
    -index ${OUTPUT} \
    -storePositions -storeDocvectors -storeRaw
  
else
    echo "Index already exists"
fi

