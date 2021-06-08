import tensorflow as tf
import sys

image_path = sys.argv[1]

# lê os dados da imagem
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Carrega o arquivo de de nomeclatura
label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("mosq_labels.txt")]

# Carrega os grafos do arquivo da rede neural
with tf.gfile.FastGFile("mosq_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Alimenta a rede neural com os dados de imagem e faz a primeira previsão
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})
    
    # Ordena o nome do candidato de acordo com o índice de confiança
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))
