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

## 2. 파일 순서대로 실행
* input, output를 잘 설정하기!
* 2_extract_summary가 pegasus 코드이고, 모델 바꿀때마다 input, output 잘 설정하기.