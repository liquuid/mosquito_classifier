# Classificador de mosquitos (Aedes, Anopheles, Culex) 
O pesquisador pode usar esse classificador para descobrir qual é o tipo de mosquito de uma grande base de dados

![el](mosq/aedes/pic_012.jpg)
![el](mosq/anopheles/pic_053.jpg)
![el](mosq/culex/pic_017.jpg)

# Requisitos

* [docker](https://www.docker.com/products/docker-toolbox)
* [tensorflow](https://www.tensorflow.org/install)
* [python](https://www.python.org/downloads)
* [numpy](https://pypi.python.org/pypi/numpy)

# Como usar 

1. Inicie uma imagem docker `docker run -it -v ~/mosquito_classifier/:/mosquito_classifier/ docker.io/tensorflow/tensorflow:1.15.3`

2. Rode o script mosq com a imagem desejada `python /mosquito_classifier/mosq.py <caminho_para_o_arquivo>`

# Precisão
![accuracy](screenshots/accuracy.png)

# Resultados
![results](screenshots/tet.png)
