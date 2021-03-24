import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img

#1. feladat
g = open("arfolyam.txt", "r")
row = []
row2 = []
elso = g.readline()
elso = elso.split()
masodik = g.readline()
masodik = masodik.split()
for i in range(10):
    row.append(float(elso[i]))
for i in range(10):
    row2.append(float(masodik[i]))
g.close()

# plt.plot(range(1, 11), row, "blue", label="pénznem1")
# plt.plot(range(1, 11), row2, "orange", label="pénznem2")
# plt.xlabel("napok")
# plt.ylabel("HUF")
# plt.title("Árfolyamváltozás")
# plt.legend()
#plt.show()

#2. feladat
def converted_to_grayscale(image):
    return image[:, :, 0] * 0.2989 + image[:, :, 1] * 0.5870 + image[:, :, 2] * 0.1140

def binary_image(gray_image):
    avg = np.average(gray_image)
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            if gray_image[i, j] > avg:
                gray_image[i, j] = 255
            else:
                gray_image[i, j] = 0
    return gray_image

#image = img.imread("flowers.jpg")
#gray_image = converted_to_grayscale(image)
#binaris_kep = binary_image(gray_image)
#plt.plot(binaris_kep.shape[0], binaris_kep.shape[1])
#plt.imshow(binaris_kep, cmap="gray")
#plt.show()

#3. feladat
def negativ_kep(mtx):
    for i in range(mtx.shape[0]):
        for j in range(mtx.shape[1]):
            mtx[i, j] = 255 - mtx[i, j]
    return mtx

image = img.imread("flowers.jpg")
img_gray = converted_to_grayscale(image)
neg_img = negativ_kep(img_gray)
plt.imshow(neg_img, cmap="gray")
plt.show()