#!/usr/bin/env bash

#INPUT_BASE_PATH="data/output/total/pegasus_reddit/"
INPUT_BASE_PATH="data/output/non_offensive/lexrank/"
#QREL_PATH="data/text_format/qrels_test_text_binary.txt"
#QREL_PATH="data/text_format/qrels_test_non-offensive_text_binary.txt"
QREL_PATH="data/text_format/qrels_test_non-offensive_text_0_3.txt"

for RUN in ${INPUT_BASE_PATH}*.txt
do
    echo "Evaluating ${RUN}"
    echo "${INPUT_BASE_PATH}"
    # -m ndcg_cut.10 -m P.10  -m map -m recip_rank
    # -q
    anserini/tools/eval/trec_eval.9.0.4/trec_eval -m map -q \
                                            ${QREL_PATH} \
                                            ${RUN} > ${RUN%.*}.results
    anserini/tools/eval/trec_eval.9.0.4/trec_eval -m ndcg_cut.10 \
                                            ${QREL_PATH} \
                                            ${RUN}
done

#P.10