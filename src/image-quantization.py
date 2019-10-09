import numpy as np
from PIL import Image 

# Problem : Daha düşük bit sayılarında görüntü nasıl görünür?

# İmge ilgili klsörden okunuyor
img = Image.open('../images/ataturk.jpeg')

# Ekrana imge bilgileri bastırılıyor
print (img.size, img.mode, img.format)

# İmge nümerik işlemler için numpy arrayi haline getiriliyor
img = np.asarray(img)

# İmgenin dimension değerine bakılıyor eğer 3 ise imge gray hale getiriliyor
if(img.ndim==3):

    img = Image.fromarray(img)

    img = img.convert('L')

# Kuantalama değeri kullanıcıdan alınıyor
k = input('Kuantalama değeri giriniz 0-7 bit değeri? \n')

# Input değeri 
k=int(k)

# İmge değerleri 

img = np.double(img)

img_k = (img/255)*(2**k-1)

# Ekrana bastırmak için round işlemi ile yuvarlama yapılıyor
img_k = np.around(img_k)

img = (img_k/(2**k-1))*255

img = np.asarray(img,dtype=np.uint8)

# Kuantalanmış imgeleri değere göre isimlendiriliyor
k = str(k)

new_image_name = k + "_ataturk.jpg"

# Kuantalanmış montaj 8 bit şeklinde kayıt ediliyor

Image.fromarray(img.astype(np.uint8)).save("../images/quantization/" + new_image_name ) 

img = Image.fromarray(img)

img.show()
