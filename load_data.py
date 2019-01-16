from keras.datasets import mnist
(train_images, train_labels),(test_images, test_labels) = mnist.load_data()
print "train imags shape :",train_images.shape
print "train labels shape :",train_labels.shape
print "test images shape :",test_images.shape
print "test labels shape :",test_labels.shape
print "len of train labels :",len(train_labels)
print "len of test labels :",len(test_labels)
print "test labels :",test_labels

