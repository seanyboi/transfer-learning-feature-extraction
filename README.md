STEP 1: Create the config file for common variables to be used

STEP 2: Divide the dataset into the format that Keras accepts

STEP 3: Take the dataset and divide them into batches. Once divided into batches the images are then preprocessed and ran through the VGG16 network pre trained on ImageNet to extract features. Labels are encoded and the appropriate label is put into a row along with the feature vector for the image.

STEP 4: Classification algorithm (LogisticRegression) is used to recognise the new classes.

When confronted with a deep learning project - often throw a feature extraction with keras to see what happens.
In some cases accuracy is sufficient, other times need to tune hyper parameters. Other times explore fine tuning or even training from scratch with custom cnn
