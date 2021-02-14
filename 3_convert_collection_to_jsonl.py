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
                    default = './data/json_format/temp')

parser.add_argument('--max_docs_per_file', 
                    default=1000000, 
                    help='Maximum number of documents in each jsonl file.')   

parser.add_argument('--predictions',  
                    help='File containing predicted summary.')                 

args = parser.parse_args()

# load dataset
dataset = ir_datasets.load('antique/test')

def convert_collection():
    print('Converting collection...')
    
    file_index = 0
    for i,doc in enumerate(dataset.docs_iter()):
        # Start writting to a new file whent the current one reached its maximum  
        # capacity. 
        if i % args.max_docs_per_file == 0:
            if i > 0:
                output_jsonl_file.close()
            output_path = os.path.join(
                args.output_folder, 'docs{:02d}.json'.format(file_index))
            output_jsonl_file = open(output_path, 'w')
            file_index += 1

        doc_id = doc[0]
        doc_text = doc[1]
        
        output_dict = {'id': doc_id, 'contents': doc_text}
        output_jsonl_file.write(json.dumps(output_dict) + '\n')
        
        if i % 100000 == 0:
            print('Converted {} docs in {} files'.format(i, file_index))

    output_jsonl_file.close()


if __name__ == '__main__':
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    convert_collection()
    print('Done!')