import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img

def sigmoid_fv(x):
    return 1 / (1 + np.power(np.e, -x))  #np.power() kitevőre emel
    #return 1 / (1 + np.e ** -x)

def sigmoid_derivated(x):
    return sigmoid_fv(x) * (1 - sigmoid_fv(x))

def histogram(mtx):
    res = np.zeros(256)
    for i in range(0, 256):
        res[i] = np.sum(mtx == i)
    return res

x = np.arange(-3, 3, 0.01)
y = sigmoid_fv(x)
dy = sigmoid_derivated(x)

# "g" -> szinezés, label = "" -> jelmagyarázat
# plt.plot(x, y, "g", label = "Sigmoid függvény") #1. x tengely értékei, 2. y tengely értékei
# plt.plot(x, dy, "r", label = "Sigmoid deriváltja")
# plt.xlabel("X értékek")  # x tengely felirata
# plt.ylabel("Y értékek")   #y tengely felirata
# plt.title("Sigmoid függvény")    #grafikon címe
# plt.legend()  #ez jeleníti meg a jelmagyarázatot
# plt.show()

#2 alábrán lesz a 2 diagram
# fig, ax = plt.subplots(1, 2)  # 1 sor, 2 oszlopban lesz
# ax[0].plot(x, y, "g", label = "Sigmoid függvény")
# ax[0].set_xlabel("Figure 1")
# ax[1].plot(x, dy, "r", label = "Sigmoid deriváltja")
# ax[1].set_xlabel("Figure 2")
# plt.show()

#2. feladat
mtx = np.random.randint(0, 256, (300, 400))
hist = np.histogram(mtx, bins = 256)  #mátrix histogramja = egyes elemek gyakorisága
#bins = mennyi tartomány legyen
#plt.bar(range(256), hist[0])  #plt.bar() oszlopdiagramot csinál!
#plt.bar(range(256), histogram(mtx))
#plt.show()

#3. feladat
def converted_to_grayscale(image):
    return image[:, :, 0] * 0.2989 + image[:, :, 1] * 0.5870 + image[:, :, 2] * 0.1140

#image = img.imread("flowers.jpg")
#image_gray = converted_to_grayscale(image)
#fig, ax = plt.subplots(1, 3)
# ax[0].imshow(image[:, :, 0], cmap = "gray")  #cmap = "gray", szürkeskálás
# ax[1].imshow(image[:, :, 1])
# ax[2].imshow(image[:, :, 2], cmap = "gray")
# plt.imshow(image)
#plt.show()

#plt.imshow(image_gray, cmap="gray")
#plt.show()

#4. feladat
def torolt_sorok(image):
    avg = np.average(image)  #kép intenzitás átlaga
    for i in range(image.shape[0]):
        if np.average(image[i, :]) > avg:
            image[i, :] = 0
    return image

# image = img.imread("flowers.jpg")
# img = converted_to_grayscale(image)  # ez alakítja át 2D-sé
# image_uj = torolt_sorok(img)
# plt.imshow(image_uj, cmap = "gray")
# plt.show()

#5.feladat
def mean_filter(image, mask_size):
    # nev_image = np.zeros_like(image)
    # for i in range(n // 2), image.shape[0] - n // 2):
    #     for j in range(n // 2), image.shape[1] - n // 2):
    #         nev_image[i, j] = np.average(image[i - n // 2: 1 + n // 2, j - n // 2:])
    res_image = np.zeros_like(image)
    for i in range(mask_size, image.shape[0] - mask_size):
        for j in range(mask_size, image.shape[1] - mask_size):
            res_image[i, j] = np.mean(image[i - mask_size: i + mask_size, j - mask_size: j + mask_size])
    return res_image

image = img.imread("flowers.jpg")
image_gray = converted_to_grayscale(image)
new_im = mean_filter(image, 3)
fig, ax = plt.subplots(1, 2)
ax[0].imshow(image, cmap="gray")
ax[1].imshow(new_im, cmap="gray")
plt.show()
