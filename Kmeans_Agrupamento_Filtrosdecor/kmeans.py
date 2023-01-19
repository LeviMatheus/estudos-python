from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import io
#from google.colab.patches import cv2_imshow

#link: https://dev.to/bitproject/extracting-colors-from-images-using-k-means-clustering-3hpe

url_pedras = "https://i.imgur.com/RArtpOd.png" #uma imagem que fica melhor para exemplificar a seleção de cores com k=10 ou 12, 5 já fica legal também.
url_utf = "https://blog-static.infra.grancursosonline.com.br/wp-content/uploads/2016/03/03191047/logo-UTFPR.jpg" #teste com o logo da utf k=10
url_lena = "https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png" #tste com a lena, k = 10 o modelo ficou bom também
img = io.imread(url_lena)
img_init = img.copy()
#print(img)
'''plt.figure(figsize=(6,6))
plt.imshow(img_init)
plt.show()'''
#print(img.shape)
img = img.reshape((img.shape[0] * img.shape[1], img.shape[2]))#convertendo para formato 2-dim

k = 10 #modificar o tamanho do valor k altera a percepção das cores
clt = KMeans(n_clusters=k) #criando o cluster para k vizinhos com base no algoritmo selecionado
clt.fit(img) #aplicando o modelo aos nossos dados, no caso, a imagem
#print(clt.labels_)#mostrando resultados apos o fitting
label_indx = np.arange(0,len(np.unique(clt.labels_)) + 1)#inicializando o array de tamanho == #clusters, definindo os indices para o histograma
hist,_ = np.histogram(clt.labels_, bins = label_indx)#Cada ponto de "dados" da matriz de imagem consistirá em seu próprio rótulo de classe de cor, portanto, plotamos a frequência de cada cor. Quanto mais uma determinada cor aparece em uma imagem, mais pontos de dados ela terá associados a ela
hist = hist.astype("float")
hist /= hist.sum() #normalizando os números no array para obter proporções que totalizem 1
print(hist)
hist_bar = np.zeros((50, 300, 3), dtype= "uint8")#criando grade para manter as cores e componentes proporcionais
#50 pixels de altura, 300 pixels de comprimento
#loop sobre a porcentagem de cada cluster e a cor de cada cluster
#iterando nas 2 arrays contendo as frequencias de cores e os centros do cluster
startX = 0
for (percent,color) in zip(hist, clt.cluster_centers_):
    endX = startX + (percent * 300)#para combinar com o tamanho da grade
    cv2.rectangle(hist_bar, (int(startX), 0), (int(endX), 50),#as imagens estavam em representação numérica, agora isso desfaz isso
      color.astype("uint8").tolist(), -1)#convertendo os números em uma representação de cor
    startX = endX

#agora plotar a imagem original e a extração de cor/quantidade
plt.figure(figsize=(15,15))
plt.subplot(121)
plt.imshow(img_init)
plt.subplot(122)
plt.imshow(hist_bar)
plt.show()
