'''Converts Antique collection to Anserini jsonl files.'''
import ir_datasets
import json
import os
import argparse

#flags.DEFINE_string('collection_path', None, 'MS MARCO .tsv collection file.')

parser = argparse.ArgumentParser()

parser.add_argument('--input_folder',
                    help='json collection file',
                    default = './data/text_format/docs_test_text.txt')
    
parser.add_argument("--output_folder",
                    help="output directory.",
                    type=str,
                    default = './data/json_format/pegasus_xsum')

parser.add_argument('--max_docs_per_file', 
                    default=1000000, 
                    help='Maximum number of documents in each jsonl file.')   

parser.add_argument('--predictions',  
                    help='File containing predicted summary.',
                    default = './data/text_format/tokenized/test_pegasus_xsum')                 

args = parser.parse_args()

# load dataset
dataset = ir_datasets.load('antique/test')

def convert_collection():
    
    print('Converting collection...')
    with open(args.input_folder) as f_corpus, open(args.predictions) as f_pred:
        file_index = 0
        for i, (line_doc, line_pred) in enumerate(zip(f_corpus, f_pred)):
            # Write to a new file when the current one reaches maximum capacity.
            if i % args.max_docs_per_file == 0:
                if i > 0:
                    output_jsonl_file.close()
                output_path = os.path.join(args.output_folder, f'docs{file_index:02d}.json')
                output_jsonl_file = open(output_path, 'w')
                file_index += 1

            doc_id, doc_text = line_doc.rstrip().split('\t')
            pred_text = line_pred.rstrip()

            contents = ''
            contents += (doc_text + ' ') 
            contents += (pred_text + ' ')

            output_dict = {'id': doc_id, 'contents': contents}
            output_jsonl_file.write(json.dumps(output_dict) + '\n')

            if i % 100000 == 0:
                print('Converted {} docs in {} files'.format(i, file_index))

    output_jsonl_file.close()


if __name__ == '__main__':
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    convert_collection()
    print('Done!')