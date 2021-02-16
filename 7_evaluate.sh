#!/usr/bin/env bash

#INPUT_BASE_PATH="data/output/total/pegasus_reddit/"
INPUT_BASE_PATH="data/output/non_offensive/pegasus_reddit/"
#QREL_PATH="data/text_format/qrels_test_text_binary.txt"
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
    anserini/tools/eval/trec_eval.9.0.4/trec_eval -m map -m recip_rank -m P.10 -m ndcg_cut.10 \
                                            ${QREL_PATH} \
                                            ${RUN}
done

#P.10