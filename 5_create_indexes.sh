#!/usr/bin/env bash
INPUT=data/json_format/keyphrase_5
OUTPUT=data/indexes/lucene-index-keyphrase_5

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

