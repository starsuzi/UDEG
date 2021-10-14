INPUT=data/antique/json_format/pegasus_xsum_4mc
OUTPUT=data/antique/indexes/lucene-index-pegasus_xsum_4mc

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

