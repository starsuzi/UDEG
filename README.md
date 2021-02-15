## 1. Installing anserini

Here, we use the open-source information retrieval toolkit [anserini](http://anserini.io/) which is built on [Lucene](https://lucene.apache.org/).
Below are the installation steps for a mac computer (tested on OSX 10.14) based on their [colab demo](https://colab.research.google.com/drive/1s44ylhEkXDzqNgkJSyXDYetGIxO9TWZn).


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

[`anserini/`](./anserini/): source folder for [anserini](https://github.com/castorini/anserini), indexes for the information corpuses, and [trec_eval](https://github.com/usnistgov/trec_eval).

```
+---anserini 
|   +---eval
|   |   \---trec_eval.9.0.4
|   \---target
|       +---appassembler
|       |   +---bin
```


## 2. 파일 순서대로 실행
* input, output를 잘 설정하기!
* 2_extract_summary가 pegasus 코드이고, 모델 바꿀때마다 input, output 잘 설정하기.

data folder은 다음과 같음.
```
+---data 
|   +---indexes
|   |   +---lucene-index-baseline
|   |   |       
|   |   +---lucene-index-pegasus_xsum 
|   +---json_format
|   |   +---baseline
|   |   |     docs00.json
|   |   +---pegasus_xsum
|   |   |   docs00.json
|   +---output
|   |   +---non_offensive
|   |   |   +---baseline
|   |   |   |   run.baseline.bm25.results
|   |   |   |   run.baseline.bm25.txt
|   |   |   |   run.baseline.bm25+rm3.results
|   |   |   |   run.baseline.bm25+rm3.txt
|   |   |   |   run.baseline.qld.results
|   |   |   |   run.baseline.qld.txt
|   |   |   |   run.baseline.qld+rm3.results
|   |   |   |   run.baseline.qld+rm3.txt
|   |   |   +---pegasus_xsum
|   |   |   |   run.pegasus_xsum.bm25.results
|   |   |   |   run.pegasus_xsum.bm25.txt
|   |   |   |   run.pegasus_xsum.bm25+rm3.results
|   |   |   |   run.pegasus_xsum.bm25+rm3.txt
|   |   |   |   run.pegasus_xsum.qld.results
|   |   |   |   run.pegasus_xsum.qld.txt
|   |   |   |   run.pegasus_xsum.qld+rm3.results
|   |   |   |   run.pegasus_xsum.qld+rm3.txt
|   |   +---total
|   |   |   +---baseline
|   |   |   |   run.baseline.bm25.results
|   |   |   |   run.baseline.bm25.txt
|   |   |   |   run.baseline.bm25+rm3.results
|   |   |   |   run.baseline.bm25+rm3.txt
|   |   |   |   run.baseline.qld.results
|   |   |   |   run.baseline.qld.txt
|   |   |   |   run.baseline.qld+rm3.results
|   |   |   |   run.baseline.qld+rm3.txt
|   |   |   +---pegasus_xsum
|   |   |   |   run.pegasus_xsum.bm25.results
|   |   |   |   run.pegasus_xsum.bm25.txt
|   |   |   |   run.pegasus_xsum.bm25+rm3.results
|   |   |   |   run.pegasus_xsum.bm25+rm3.txt
|   |   |   |   run.pegasus_xsum.qld.results
|   |   |   |   run.pegasus_xsum.qld.txt
|   |   |   |   run.pegasus_xsum.qld+rm3.results
|   |   |   |   run.pegasus_xsum.qld+rm3.txt
|   +---text_format
|   |   +---tokenized
|   |   |   test_pegasus_reddit
|   |   |   test_pegasus_xsum
|   |   |   test_text_tokenized
|   |   docs_test_text.txt
|   |   qrels_test_non-offensive_text_binary.txt
|   |   qrels_test_non-offensive_text.txt
|   |   qrels_test_text_binary.txt
|   |   qrels_test_text.txt
|   |   queries_test_non-offensive_text.txt
|   |   queries_test_text.txt
|   |   test_text.txt
```