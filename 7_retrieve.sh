#!/usr/bin/env bash
mkdir -p data/output/baseline

EXP="baseline"
INDEX="data/indexes/lucene-index-baseline"
OUTPUT_BASE_PATH="data/output/baseline/"
TOPICS="data/text_format/queries_test_non-offensive_text.txt"

for MODEL in "bm25" "qld"
do
    if [ ! -f "${OUTPUT_BASE_PATH}/run.${EXP}.${MODEL}.txt" ]
    then
        # retrieve documents using the given model TsvInt
        sh anserini/target/appassembler/bin/SearchCollection \
            -topicreader TsvInt \
            -index  ${INDEX} \
            -topics ${TOPICS} \
            -output ${OUTPUT_BASE_PATH}/run.${EXP}.${MODEL}.txt -${MODEL}
    fi

    if [ ! -f "${OUTPUT_BASE_PATH}/run.${EXP}.${MODEL}+rm3.txt" ]
    then
        # compute model with pseudo-relevance feedback RM3
        sh anserini/target/appassembler/bin/SearchCollection \
            -topicreader TsvInt \
            -index  ${INDEX} \
            -topics ${TOPICS} \
            -output ${OUTPUT_BASE_PATH}/run.${EXP}.${MODEL}+rm3.txt -${MODEL} -rm3
    fi
done