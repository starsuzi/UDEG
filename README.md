# Unsupervised Document Expansion for Information Retrieval with Stochastic Text Generation

Official Code Repository for the paper "Unsupervised Document Expansion for Information Retrieval with Stochastic Text Generation" (SDP@NAACL 2021): https://aclanthology.org/2021.sdp-1.2/

## Abstract
One of the challenges in information retrieval (IR) is the vocabulary mismatch problem, which happens when the terms between queries and documents are lexically different but semantically similar. While recent work has proposed to expand the queries or documents by enriching their representations with additional relevant terms to address this challenge, they usually require a large volume of query-document pairs to train an expansion model. In this paper, we propose an Unsupervised Document Expansion with Generation (UDEG) framework with a pre-trained language model, which generates diverse supplementary sentences for the original document without using labels on query-document pairs for training. For generating sentences, we further stochastically perturb their embeddings to generate more diverse sentences for document expansion. We validate our framework on two standard IR benchmark datasets. The results show that our framework significantly outperforms relevant expansion baselines for IR.

## Dependencies
* Python 3.7.9
* Pytorch 1.7.0
* Transformers 4.3

## Run
### 1. Installing anserini

We use the open-source information retrieval toolkit [anserini](http://anserini.io/).

```bash
# install maven
sudo apt-get install maven

# cloning / installing anserini
git clone https://github.com/castorini/anserini.git --recurse-submodules
cd anserini/
# changing jacoco from 0.8.2 to 0.8.3 in pom.xml to build correctly
mvn clean package appassembler:assemble

# compile evaluation tools and other scripts
cd tools/eval && tar xvfz trec_eval.9.0.4.tar.gz && cd trec_eval.9.0.4 && make && cd ../../..
cd tools/eval/ndeval && make && cd ../../..
```

### 2. Data Preprocessing
```bash
python 0_0_extract_text.py
python 0_1_convert_qrels_to_binary.py
python 0_2_convert_qrels_to_ndcg_scale.py
```

### 3. Data Tokenization
```bash
python 1_convert_text_to_tokenized.py
```

### 4. Abstractive Generation with Stochastic Text Generation
```bash
python 2_abstract_summary_multi.py
```
We provide the abstractly & stochastically generated output file in this repository (test_pegasus_xsum_4mc.tar.gz).

### 5. Convert to json format
We refer to the repository of https://github.com/nyu-dl/dl4ir-doc2query.
```bash
python 3_concat_collection_summary_to_json.py
```
### 6. Indexing, Retrieval, Evaluation
We refer to the repository of https://github.com/boudinfl/ir-using-kg#data.
```bash
sh 4_create_indexes.sh
sh 5_retrieve.sh
sh 6_evaluate.sh
```

## Cite
```BibTex
@inproceedings{jeong-etal-2021-unsupervised,
    title = "Unsupervised Document Expansion for Information Retrieval with Stochastic Text Generation",
    author = "Jeong, Soyeong  and
      Baek, Jinheon  and
      Park, ChaeHun  and
      Park, Jong",
    booktitle = "Proceedings of the Second Workshop on Scholarly Document Processing",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.sdp-1.2",
    doi = "10.18653/v1/2021.sdp-1.2",
    pages = "7--17"
}
```