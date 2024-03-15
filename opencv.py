import cv2 as cv

img = cv.imread('cat.jpg')

(b, g, r) = img[0, 0] # b = blue; g = green; r = red;
print('Vermelho:', r, 'Verde:', g, 'Azul:', b) 
print("Altura:", img.shape[0], "e Largura:", img.shape[1])


#Caso queira ver um tipo de imagem em específico, invés da ultima, apague as '#' e comente um código posterior.


#O bloco de códigos a seguir faz com que a imagem tenha suas cores alteradas
#-Abaixo estão dois laços de repetição que, enquanto aumentam, primeiramente  
#-pegam a posição do pixel relativo a altura(linha) depois a largura(coluna).
#for y in range(0, img.shape[0]):#Altura(linha)
    #for x in range(0, img.shape[1]):#Largura(coluna)
        #img[y, x] = (255,90,120) #Cor

#Este código faz com que a imagem receba um tipo de efeito diferente,
#-Ao invés de ficar com uma única cor, ela acaba recebendo um tipo de "fade"
#-que provém da sobra dos valores x e y por 256, dentro do laço.
#for y in range(0, img.shape[0]): 
    #for x in range(0, img.shape[1]):
        #img[y, x] = (x%256,y%256,x%256)#Diminuir os valores também faz a imagem ser alterada.

#for y in range(0, img.shape[0]): 
    #for x in range(0, img.shape[1]):
        #img[y, x] = (0,(x*y)%256,0)#Alterar os valores b e r fazem com que a cor mude neste caso,
                                   #-aumentar ou diminuir o g, faz com que o "cubículo" aumente ou diminua.
         

#Com esse bloco de códigos consigo mexer em pixeis específicos através dos laços de repetição.
for y in range(0, img.shape[0], 10): 
    for x in range(60, img.shape[1], 130): 
        img[y:y+5, x: x+5] = (0,255,255)
    for y in range(0, img.shape[0], 5):
        for x in range(0, img.shape[1], 5):
            if 59 >= x  or 191 <= x:
                img[y:y+5, x: x+5] = (255,50,100)


cv.imshow('cat', img)

cv.waitKey(0)
