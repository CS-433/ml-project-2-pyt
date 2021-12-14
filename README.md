# Project2_ML

The goal would be to realize a study like the London case study [[1](https://dl.acm.org/doi/10.1145/3342240)] but add the notion of qualitative perception through a survey.  

In the paper they estimate house price by associating it to the visual appeal of the house view. In our project the goal would be to focus on the visual appeal. By using a survey, it would be possible to see how the visual appeal relates to the object on image and 

## How we want to use the survey results  

In our study, we would want to reproduce similar type of map through a survey. Multiple individuals would be asked to compare two views of a house or street.  

-	Information on the person surveyed:  
origin, gender, age, percentage of lifetime lives in town/countryside 
 
-	Grade the view:  
Select a view in a one vs one battle of pictures. This will allow to create a rank/grade of the appeal all the views. 

The survey can be found here: https://toto1205.itch.io/ml2-project
 
## How we use the view  

Since each view is an image, a CNN could be used to determine the visual features (houses, roads, trees etc…) of a view. Therefore each view could be stored as a vector, the following is from the second paper [[2](https://ieeexplore.ieee.org/document/)] and schematized how a specific view can be stored as a binary vector depending on what is seen on the image.  
 
But in our case we would want to determine the proportion, between 0 and 1, of each features on the pictures, for example if the pixels associated to a road takes 40% of the entire image then the it will be stored as 0.4 . This would allow to associate each view to its vector of features. 
 
## Defining the training dataset 

With the survey results associated to the analysis of the view, we could build a table where each row would be composed of the grade for a single view followed by the transposed vector of features of the view.  
 
### Goal of the project  
Using the information given in the previous sections, the project will proceed as such:  
-	Get at least one dataset of view for Lausanne, from Google Street View. 
- 	Develop the CNN to be able to obtain coherent views for a large dataset, and to be able to associated a view with its vector of features.
-	Make the survey associated to the all the views, and then define the train and test dataset
- 	Run the linear regression on the training datasets and adjust the prediction model  
-	Make the predictions for the appeal of the test set and superpose them with environmental parameters (from GIs or other) to get the environmental quality map of the city. 


