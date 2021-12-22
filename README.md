# TODO
* Ajouter la StreetViewAPI dans le dossier "ImagesAcquisition" et sauver les raw images en zip dans "Data/RawImages"
* Ajouter le cleaning de ces images (encore dans "ImagesAcquisition" et mettre l'output path vers "Data/CleanedImages".
* Ajouter l'obtention des clusters par VGG16. Soit avec un nouveau truc dans "DataProcessing/UnusedProcessing", soit directement à partir de l'étape 2), sauver les clusters dans "Data/Features/UnusedFeatures/VGGclusters.csv"
* Mettre le modèle généralisable dans "GeneralizableModel" une fois fini
* APPLIQUER A UNE NOUVELLE VILLE
* Commenter (ETRE CONSISTANT AVEC LES COMMENTAIRES DES AUTRES e.g in SurveyResultsCleaning)
* Write README
* Update PPT avec vue
* Update rapport avec commentaires Adam
* Ajouter Documentation

# The Best Location for You to Live

This project aims at building a tool that allows anyone to find their ideal residence place in a given city by specifying their personal level of importance for the location's visual appeal and environmental parameters.
This repository mainly contains the steps followed to build a model able to evaluate a picture's appeal by means of image analysis. An interactive map is also available to see the application on a city, with different layers for environmental parameters.

## Description

An in-depth paragraph about your project and overview of use.

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

* Paul Habert(https://github.com/plhbt)
* Yannick Neypatraiky(https://github.com/nyannickandre)
* Thomas Rimbot(https://github.com/Thomas-debug-creator)

## Acknowledgments
We would like to thank the Laboratoire d’Economie Urbaine et de l’Environnement, and more particularly Professor Philippe Thalmann and his doctoral student Adam Swietek for their precious advice. Many thanks to everyone who answered the discrete choices survey, and to Professors Jamila Sam and Barbara Jobstmann for allowing us to present this project to their class.

