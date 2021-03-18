import ir_datasets
import os
import sys
import argparse

# get the command line arguments
parser = argparse.ArgumentParser()

parser.add_argument("--output_doc_text_only",
                    help="output document directory in text format.",
                    type=str,
                    default = './data/text_format/test_text.txt')

parser.add_argument("--output_doc",
                    help="output document directory in text format.",
                    type=str,
                    default = './data/text_format/docs_test_text.txt')

parser.add_argument("--output_quer",
                    help="output queries directory in text format.",
                    type=str,
                    default = './data/text_format/queries_test_non-offensive_text.txt')

parser.add_argument("--output_qrel",
                    help="output qrels directory in text format.",
                    type=str,
                    default = './data/text_format/qrels_test_non-offensive_text.txt')

args = parser.parse_args()

# creating output path if it does not exist
output_doc_text_only_dir = os.path.split(args.output_doc_text_only)[0]
output_doc_dir = os.path.split(args.output_doc)[0]
output_queries_dir = os.path.split(args.output_quer)[0]
output_qrels_dir = os.path.split(args.output_qrel)[0]

if not os.path.isdir(output_doc_text_only_dir):
    os.makedirs(output_doc_text_only_dir, exist_ok=True)
if not os.path.isdir(output_doc_dir):
    os.makedirs(output_doc_dir, exist_ok=True)
if not os.path.isdir(output_queries_dir):
    os.makedirs(output_queries_dir, exist_ok=True)
if not os.path.isdir(output_qrels_dir):
    os.makedirs(output_qrels_dir, exist_ok=True)

# skip if file already exists
if os.path.isfile(args.output_doc_text_only):
    print("file {} already exists - stopping now".format(args.output_doc_text_only))
    sys.exit(0)
if os.path.isfile(args.output_doc):
    print("file {} already exists - stopping now".format(args.output_doc))
    sys.exit(0)
if os.path.isfile(args.output_quer):
    print("file {} already exists - stopping now".format(args.output_quer))
    sys.exit(0)
if os.path.isfile(args.output_qrel):
    print("file {} already exists - stopping now".format(args.output_qrel))
    sys.exit(0)

# load dataset
dataset = ir_datasets.load('antique/test/non-offensive')

# document text only extraction
with open(args.output_doc_text_only, mode="w") as outfile: 
    for doc_text_only in dataset.docs_iter():
        outfile.write("%s\n" % doc_text_only[1])
# document extraction
with open(args.output_doc, mode="w") as outfile: 
    for doc in dataset.docs_iter():
        outfile.write("{0}\t{1}\n".format(doc[0],doc[1]))
# queries extraction
with open(args.output_quer, 'w') as outfile:
    for quer in dataset.queries_iter():
        outfile.write("{0}\t{1}\n".format(quer[0],quer[1]))
# qrels extraction
with open(args.output_qrel, 'w') as outfile:
    for qrel in dataset.qrels_iter():
        outfile.write("{0}\t{1}\t{2}\t{3}\n".format(qrel[0],qrel[3],qrel[1],qrel[2]))