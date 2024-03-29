## AutoFaUmfelderkennungTrafficSigns
We want to do a Custom Object Detection to detect traffic signs. In the following you can find a short manual for Ubuntu (18.04.)

# Step 1: Installation
$ pip install tensorflow

If you have a GPU that you can use with Tensorflow:

$ pip install tensorflow-gpu

Additional Dependencies:

$ pip install pillow Cython lxml jupyter matplotlib

Next we need Protobuf

$ sudo apt update
$ sudo apt install python-protobuf

# Step 1.1: Cloning Repository
First change into the Tensorflow directory:

(if you do not knwo where your Tensorflow directory is, jou can use the following command)

$ pip show Tensorflow

Okay, know we can got into the Tensorflow directory

$ cd <path_to_your_tensorflow_installation>

Next, we clone the repository

$ git clone https://github.com/SaschaLuethje/AutoFaUmfelderkennungTrafficSigns.git

From this point on, this directory will be referred to as the models directory

# Step 1.2: Setting up the environment
Every time you start a new terminal window to work with the pre-trained models, it is important to compile Protobuf and change your PYTHONPATH.
Run the following from your terminal:

$ cd <path_to_your_tensorflow_installation>/models/research/
$ protoc object_detection/protos/*.proto --python_out=.
$ export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

You can run a quick test to confirm that everything is working properly:

$ python object_detection/builders/model_builder_test.py

# Step 2: Dataset
In the following we create our dataset. If you do not want to do it by yourself you can download the dataset here: (TODO) and skip Step 2.

We are using the 'German Traffic Sign Recognition Benchmark' (https://benchmark.ini.rub.de/gtsrb_news.html) it contains more tahn 40 classes and mote than 50.000 images in total. You can download the dataset here: (https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/published-archive.html).
Please notice, that we need the images in jpg. Therefore you need to convert the images from PPM to jpg. you can use the customScripts/myPPMtoJPGConverter.py script for this.

# Step 2.1: Collect images
Every imageset needs an annotation CSV file. This file contains information about the images (Width, Heights, ClassId, bounding boxes, etc...). The GTSRB dataset already has a CSV file but unfortunatelly we need to perform some changes on it.
1. Split the CSV file into multiple once, once for every image. You can use the following script (customScripts/myCsvDividerScript.py).
for example:
$ python myCsvDividerScript.py 'GT-00014.csv' 'Stop'
2. Next you should split the data into train (ca. 90%) and test set (ca. 10%). Create the following folders for this. images/train & images/test and put the images with the corresponding csv files there.
3. Use myCsvCombineScript.py script to combine the single csv files into a single one again (one for test and for train)


# Step 2.2: Create Label Map (.pbtxt)
Classes need to be listed in the label map. This will look like the following:
item {
    id: 1
    name: 'Stop'
}
Note that id must start from 1, because 0 is a reserved id.
Save this file as label_map.pbtxt in models/annotations/

# Step 2.3: Create trainval.txt
trainval.txt is a list of image names without file extensions. To create trainval.txt you can simple use the following command ls >> trainval.txt. Save the file in models/annotations/

# Step 2.4: Create TFRecord (.record)
TFRecord is an important data format designed for Tensorflow. (Read more about it here (https://www.skcript.com/svr/why-every-tensorflow-developer-should-know-about-tfrecord/)). Before you can train your custom object detector, you must convert your data into the TFRecord format. We’re going to use customScripts/create_tfrecord.py to convert our data set. Run this script for both datasets (train and test).

# Step 3: Download pre-trained model
There are many pre-trained object detection models available in the model zoo. In order to train them using our custom data set, the models need to be restored in Tensorflow using their checkpoints (.ckpt files), which are records of previous model states.

For this tutorial, we’re going to download ssd_mobilenet_v2_coco here (TODO) and save its model checkpoint files (model.ckpt.meta, model.ckpt.index, model.ckpt.data-00000-of-00001) to our models/checkpoints/ directory.

# Step 4: Modify Config (.config) File
Each of the pretrained models has a config file that contains details about the model. To detect our custom class, the config file needs to be modified accordingly. If you want to train a new model with different configurations, this is the file you need to change.

# Step 5: Train
Follow the steps below:

$ cd tensorflow/models 
$ mkdir train # Make directory for storing training progress
$ mkdir eval # Make directory for storing validation results
$ python research/object_detection/legacy/train.py \
    --logtostderr \
    --train_dir=train \
    --pipeline_config_path=ssd_mobilenet_v2_coco.config
    
# Step 6: Evaluation
Evaluation can be run in parallel with training. You can visualize model training progress using Tensorboard:

$ tensorboard --logdir=./

Based on the graphs output by Tensorboard, you may decide when you want to stop training. Usually, you may stop the process when the loss function is tapering off and no longer decreasing by a significant amount.

# Step 7: Model export
Once you finish training your model, you can export your model to be used for inference.

$ mkdir fine_tuned_model
$ python research/object_detection/export_inference_graph.py \    
--input_type image_tensor \    
--pipeline_config_path ssd_mobilenet_v2_coco.config \    
--trained_checkpoint_prefix  train/model.ckpt-<the_highest_checkpoint_number> \    
--output_directory fine_tuned_model

# Step 8: Testing
For testing you can use the following script customScripts/Object_detection_image.py. it takes one image and displays the image again but now with bounding boxes.



