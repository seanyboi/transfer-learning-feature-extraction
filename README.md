# H1 Transfer Learning (Feature Extraction)

### H3 STEP 1

Create the config file for common variables to be used

#### H3 STEP 2

Divide the dataset into the format that Keras accepts

### H3 STEP 3

Take the dataset and divide them into batches. Once divided into batches the images are then preprocessed and ran through the VGG16 network pre trained on ImageNet to extract features. Labels are encoded and the appropriate label is placed into a row along with the feature vector for the image.

### H3 STEP 4

Classification algorithm (LogisticRegression) is used to recognise the new classes.


Dataset can be found here: https://mmspg.epfl.ch/downloads/food-image-datasets/
