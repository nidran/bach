import os
import struct
import torch
from PIL import Image
# import matplotlib.pyplot as plt
import numpy as np
import torchvision
from torch.autograd import Variable
from torch.utils.data import TensorDataset,DataLoader
from torchvision import models
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import copy
import torchvision.transforms as transforms
import time
import sys

# input
imagepath = sys.argv[1]

net = models.alexnet(pretrained=False)
net1 = models.alexnet(pretrained=False)
net2 = models.alexnet(pretrained=False)
net3 = models.alexnet(pretrained=False)
new_classifier = nn.Sequential(*list(net.classifier.children())[:-1])
new_classifier.add_module('fc',nn.Linear(4096,2))
new_classifier.add_module('softmax',nn.LogSoftmax())
net.classifier = new_classifier
net.load_state_dict(torch.load('NormalvsRest.best.pth.tar'))

new_classifier1 = nn.Sequential(*list(net1.classifier.children())[:-1])
new_classifier1.add_module('fc',nn.Linear(4096,2))
new_classifier1.add_module('softmax',nn.LogSoftmax())
net1.classifier = new_classifier1
net1.load_state_dict(torch.load('modelben1ins0.pth.tar'))

new_classifier2 = nn.Sequential(*list(net2.classifier.children())[:-1])
new_classifier2.add_module('fc',nn.Linear(4096,2))
new_classifier2.add_module('softmax',nn.LogSoftmax())
net2.classifier = new_classifier2
net2.load_state_dict(torch.load('modelinvvsbenre.pth.tar'))

new_classifier3 = nn.Sequential(*list(net3.classifier.children())[:-1])
new_classifier3.add_module('fc',nn.Linear(4096,2))
new_classifier3.add_module('softmax',nn.LogSoftmax())
net3.classifier = new_classifier3
net3.load_state_dict(torch.load('modelinv0ins1.pth.tar'))

feat=[]
test_out=[]
labels=[]
test_labels=[]
net.train(False)

im=Image.open(imagepath)

im = im.resize((224,224))
im = np.array(im)
img_tensor = torch.Tensor(im).transpose(0,2).unsqueeze(0)
img_tensor=img_tensor/255.0
img_var = Variable(img_tensor)
print(fc)

outr= net(img_var)
_, predicted = torch.max(outr.data, 1)

if predicted.numpy() == 0:
    print(0)
else:
    test=[]

    outr= net1(img_var)
    _, predicted1 = torch.max(outr.data, 1)
#                 test_out.append(predicted.numpy())

    outr= net2(img_var)
    _, predicted2 = torch.max(outr.data, 1)

    outr= net3(img_var)
    _, predicted3 = torch.max(outr.data, 1)

    if predicted1.numpy()==0:
        test.append(2)
    else:
        test.append(3)

    if predicted2.numpy()==0:
        test.append(1)
    else:
        test.append(3)

    if predicted3.numpy()==0:
        test.append(1)
    else:
        test.append(2)
    print(test)
    test=np.bincount(test)
    print(np.argmax(test))

