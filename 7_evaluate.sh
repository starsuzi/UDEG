#!/usr/bin/env bash

INPUT_BASE_PATH="data/output/non_offensive/pegasus_xsum/"
QREL_PATH="data/text_format/qrels_test_non-offensive_text_binary.txt"

for RUN in ${INPUT_BASE_PATH}*.txt
do
    echo "Evaluating ${RUN}"
    echo "${INPUT_BASE_PATH}"
    # -m P.30
    # -q
    anserini/tools/eval/trec_eval.9.0.4/trec_eval -m map -q \
                                            ${QREL_PATH} \
                                            ${RUN} > ${RUN%.*}.results
    anserini/tools/eval/trec_eval.9.0.4/trec_eval -m map -m recip_rank \
                                            ${QREL_PATH} \
                                            ${RUN}
done

#P.10