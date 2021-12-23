# TODO
* Ajouter la StreetViewAPI dans le dossier "ImagesAcquisition" et sauver les raw images en zip dans "Data/RawImages"
* Ajouter le cleaning de ces images (encore dans "ImagesAcquisition" et mettre l'output path vers "Data/CleanedImages".
* Revoir paths dans "DataProcessing/UnusedProcessing/ClusterImagesVGG16", sauver les clusters dans "Data/Features/UnusedFeatures/VGGclusters.csv"
* Mettre le modèle généralisable dans "GeneralizableModel" une fois fini
* APPLIQUER A UNE NOUVELLE VILLE
* Commenter (ETRE CONSISTANT AVEC LES COMMENTAIRES DES AUTRES e.g in SurveyResultsCleaning)
* Write README (add link to yolov3.weights)

# The Best Location for You to Live

This project aims at building a tool that allows anyone to find their ideal residence place in a given city by specifying their personal level of importance for the location's visual appeal and environmental parameters.
This repository mainly contains the steps followed to build a model able to evaluate a picture's appeal by means of image analysis. An interactive map is also available to see the application on a city, with different layers for environmental parameters.

## Project documentation

The project's report, as well as the pitch presentation, can be found under the folder Documentation. This will guide you through the adventure of the project, while explaining choices behind data preprocessing, feature selection, models, and many more...

## How to give it a try

__Foreword note:__ If you do not choose to run the exact same notebooks by using the files already created by running some code, you will need to unzip files.

On this repository, you can use and replicate models for a given location. By going through the ImagesAcquisition folder, you will be able to change the location of the focused area where you want to get images from. To do so, you will need to get a Google API to access to Google Street View, you can get an API key for three free months by following this link: [get-api-key](https://developers.google.com/maps/documentation/javascript/get-api-key). After gathering your images from your chosen location, you will be able to clean your images using DataProcessing/UnusedProcessing/ClusterImagesVGG16.py if these ones are not good enough for you. Also note that if you do choose to run VGG16 to further clean your images, you will need to download weigths that are used to train VGG16. These weights can be downloaded at: [yolov3.weights](https://pjreddie.com/darknet/yolo/).

The [survey](https://toto1205.itch.io/ml2-project) on which models will try to predict the views appeal has already been done, and tried to represent many types of areas with variances in images. This way, your models will be trained by using a representative sample. However, if some views are very far off this representative sample, you might end up having unexpected results.
 
After having your cleaned images, you will need to get features to run a model from it. The best features that were kept while doing the modeling on the former dataset were 6 colors (green, grey, black, white, blue and red), and an object feature which is the sum of sizes of the detected objects on an image. The first 6 features can be found by using the file DataProcessing/ImageSegmentation.ipynb, and the last object feature is computed by running DataProcessing/ObjectRecognitionYoloV3.ipynb. By doing this, you will write csv files which summarize features for your own images.

Many models have been computed to get the best appeal predictions, and you can find what is the best possible regression and/or classification by jumping into ModelSelection/FinalModel.ipynb. Finally, by choosing the best model and running GeneralizableModel/ApplicationModel.ipynb, you will be able to get appeals of Street Views within your chosen area and build the [website](https://the-best-location-to-live.github.io/the-best-location-to-live/) which will give you the visual preferences on where are the best location to live in, considering the Street Views.

## Getting Started

### Dependencies

* Library to download:
* Standard python library numpy,matplotlib.pyplot, random, itertools
* scipy
* pandas
* pyreadr
* sklearn
* skfeature-chappers
* skrebate
* boruta 
* sklearn-genetic, DEAP
* scipy_cut_tree_balanced
* pyHSICLasso


### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```


## Authors

* [Paul Habert](https://github.com/plhbt)
* [Yannick Neypatraiky](https://github.com/nyannickandre)
* [Thomas Rimbot](https://github.com/Thomas-debug-creator)

## Acknowledgments
We would like to thank the Laboratoire d’Economie Urbaine et de l’Environnement, and more particularly Professor Philippe Thalmann and his doctoral student Adam Swietek for their precious advice. Many thanks to everyone who answered the discrete choices survey, and to Professors Jamila Sam and Barbara Jobstmann for allowing us to present this project to their class.

