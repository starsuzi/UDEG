INPUT_BASE_PATH="data/antique/output/pegasus_xsum_4mc/"

#for P, R, map, recip_rank
QREL_PATH="data/antique/qrels_test_text_binary.txt"
#for ndcg_cut
#QREL_PATH="data/antique/qrels_test_text_0_3.txt"

for RUN in ${INPUT_BASE_PATH}*.txt
do
    echo "Evaluating ${RUN}"
    echo "${INPUT_BASE_PATH}"
    # -m recip_rank -m recall.10 -m P.3 -m map 
    # -m ndcg_cut.3 
    anserini/tools/eval/trec_eval.9.0.4/trec_eval -m recip_rank -q \
                                            ${QREL_PATH} \
                                            ${RUN} > ${RUN%.*}.results.mrr
    anserini/tools/eval/trec_eval.9.0.4/trec_eval  -m recip_rank -m recall.10 -m P.3 -m map   \
                                            ${QREL_PATH} \
                                            ${RUN}
done