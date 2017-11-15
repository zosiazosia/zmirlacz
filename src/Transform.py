from keras.applications.vgg19 import VGG19
from keras.preprocessing import image
from keras.applications.vgg19 import preprocess_input
from keras.models import Model
import numpy as np
import cv2
import Person
import matplotlib.pyplot as plt
import os
from scipy import spatial


#jako pola base_mode?
#jako pole tree?
class Transform:
    def __init__(self):
        self.base_model = VGG19(weights='imagenet')
        self.model = Model(inputs=self.base_model.input, outputs=self.base_model.get_layer('block4_pool').output)
        self.tree
        self.persons = []
        self.indexes = []

    def transform(self, img):
        imgT  = cv2.resize(img, (224, 224))
        x = image.img_to_array(imgT)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        block4 = self.model.predict(x)
        print("shape", block4.shape)
        a = block4
        b = ((a.sum(axis=0)).mean(axis=0)).mean(axis=0)
        return b

#build tree from all currently available vectors
    def build_tree(self):
        tab = []
        i = 0
        for p in self.persons:
            person = Person.MyPerson(p)
            for v in person.vectors:
                tab[i] = v
                self.indexes[i] = person.i
                i = i+1

        self.tree = spatial.KDTree(tab)

#img already as a transformed vector
    def classify(self, img):
        #5 nearest vectors
        dist, ind = self.tree.query(img, k=5)

        p_id = []
        i = 0
        for v in ind:
            nr = self.indexes[v]

            i = i+1





