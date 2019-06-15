# import the necessary packages
import os

# initialise the path to the *original* input directory of images
ORIG_INPUT_DATASET = "Food-5K"

# initalise the base path to the *new* directory that will contain
# our images after computing the training and testing split
BASE_PATH = "dataset"

# define the names of training, testing and validation directories
TRAIN = "training"
TEST = "evaluation"
VAL = "validation"

# initalise the list of class label names
CLASSES = ["non_food", "food"]

# set the batch size
BATCH_SIZE = 32

# initalise the label encoder file path and the output directory to
# where the extracted features from ImageNet model (in CSV file format) will be stored
LE_PATH = os.path.sep.join(["output", "le.cpickle"])
BASE_CSV_PATH = "output"

# set the path to the serialized model after training
MODEL_PATH = os.path.sep.join(["output", "model.cpickle"])
