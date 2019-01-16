from keras.datasets import mnist
(train_images, train_labels),(test_images, test_labels) = mnist.load_data()
print "train imags ndim :",train_images.ndim
print "train imags shape :",train_images.shape
print "train imags dtype :",train_images.dtype
print "train labels ndim :",train_labels.ndim
print "train labels shape :",train_labels.shape
print "train labels dtype :",train_labels.dtype
print "test images ndim :",test_images.ndim
print "test images shape :",test_images.shape
print "test images dtype :",test_images.dtype
print "test labels ndim :",test_labels.ndim
print "test labels shape :",test_labels.shape
print "test labels dtype :",test_labels.dtype
print "len of train labels :",len(train_labels)
print "len of test labels :",len(test_labels)
print "test labels :",test_labels
aslice=train_images[10:12,0:5,0:5]
print "slice shape : ",aslice.shape
print "slice : ",aslice
little_slice = aslice[0:2,0:2,0:2]
print "little slice : ",little_slice

digit = train_images[4]
import matplotlib.pyplot as plt
plt.imshow(digit,cmap=plt.cm.binary)
plt.show()

from keras import models
from keras import layers

network = models.Sequential()
network.add(layers.Dense(512,activation='relu',input_shape=(28*28,)))
network.add(layers.Dense(10,activation='softmax'))
network.compile(optimizer='rmsprop',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

train_images=train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images=test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

from keras.utils import to_categorical
print "train_labels : ",train_labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
print "train_labels : ",train_labels
#print "train_labels : ",train_labels
network.fit(train_images,train_labels,epochs=5,batch_size=128)
test_loss,test_acc=network.evaluate(test_images,test_labels)
print "test_acc : ",test_acc
print "test_loss : ",test_loss


