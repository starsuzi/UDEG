#!/usr/bin/env bash
INPUT=data/json_format/lexrank
OUTPUT=data/indexes/lucene-index-lexrank

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

