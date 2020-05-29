## BACH Challenge
Our Approach to https://iciar2018-challenge.grand-challenge.org

![alt text](https://github.com/nidran/bach/blob/master/bach.png?raw=true)

# The challenge - 
There were two goals in this challenge. 
The part A of the challenge consists in automatically classifying H&E stained breast histology microscopy images in four classes: normal, benign, in situ carcinoma and invasive carcinoma. 
The part B consists in performing pixel-wise labelling of whole-slide images in the same four classes. For these purposes, challenge participants will be provided with approx. 400+ labeled microscopy images, and 10 pixel-wise labeled and 20 non-labeled whole-slide images. 
This challenge is a follow-up of the one of Bioimaging2015

Dataset
The dataset is composed of Hematoxylin and eosin (H&E) stained breast histology microscopy and whole-slide images. Challenge participants should evaluate the performance of their method on either/both sets of images.

CLICK HERE TO REQUEST THE DATASET

1. Microscopy images 
Microscopy images are labelled as normal, benign, in situ carcinoma or invasive carcinoma according to the predominant cancer type in each image. The annotation was performed by two medical experts and images where there was disagreement were discarded.

			
Normal	Benign	in situ carcinoma	Invasive carcinoma
The dataset contains a total of 400 microscopy images, distributed as follows:

Normal: 100
Benign: 100
in situ carcinoma: 100
Invasive carcinoma: 100
Microscopy images are on .tiff format and have the following specifications:

Color model: R(ed)G(reen)B(lue)
Size: 2048 x 1536 pixels
Pixel scale: 0.42 µm x 0.42 µm
Memory space: 10-20 MB (approx.)
Type of label: image-wise
Note that the microscopy image dataset is an extension of the one used in this article, made publicly avaiable at this repository. For the BACH challenge, please download the new, more complete dataset, via the DOWNLOAD tab.

The patient-wise origin of each microscopy image is partially available on the following file. The anonimization process does not allow to retrieve the origin of all images, but it is safe to assume that all undentified images come from different patients of the identified ones.

View public_html/patient_microscopy on Dropbox.

2. Whole-slide images
Whole-slide images are high resolution images containing the entire sampled tissue. In this sense, microscopy images are just details of the whole-slide images. Because of that, each whole-slide image can have multiple normal, benign, in situ carcinoma and invasive carcinoma regions. The annotation of the whole-slide images was performed by two medical experts and images where there was disagreement were discarded. Each image has a corresponding list of labelled coordinates that enclose benign, in situ carcinoma and invasive carcinoma regions (the remaning tissue is considered normal and thus is not relevant for performance evaluation).



Whole-slide images are on .svs format and have the following specifications:

Color model: R(ed)G(reen)B(lue)
Size: variable (eg: 42113 x 62625 pixels)
Pixel scale: 0,467 µ/pixel
Memory space: 8 GB (approx.) when in numpy array (pyhton), 200-250 MB (approx.) in .svs
Acquisition system: Leica SCN400
Type of label: pixel-wise
Annotations of the coordinates of the points that enclose each region are made avaliable as a .xml file.

The patient-wise origin of the WSI is provided in the following file.

View public_html/patient_wsi on Dropbox.

Reading the dataset
Microscopy images are available in .tiff format.

Whole-slide images are available in .svs format.

For convinience, a Python script for reading the .svs and the .xml containing for the annotations of the whole-slide images is available together with the remaining data.

View public_html/code on Dropbox.

The provided scripts require OpenSlide.
For Windows users:

open a command-line and install openslide-python: pip install openslide-python
download the Windows binaries here;
unzip the binaries and add the bin folder to your path variable.
For Linux users:

open a terminal and install openslide-python: pip install openslide-python
install openslide: sudo apt-get install python-openslide
Requires opencv version 3.2.0 (at least);

The .xml reading script returns a list containing, for each region of interest:

the coordinates of the perimeter of the region (X,Y -- columns,rows in Python indexing - origin at the left upper corner)
the label of the region
the perimeter of the region, in micrometers
the area of the region, in square micrometers
the pixel scale, micrometers/pixel
 
