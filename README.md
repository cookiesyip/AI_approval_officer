# AI_approval_officer

The process is for detecting check box or signed/chopped area from the given document

## png transformation

The png/jpg files are the most suitable for training.testing process. If your files are in pdf format, we provide the code pdf2image.py for transformation.

please ensure that your files be saved in folder "pdfs",and create an empty folder "images". The result will be saved in folder "images"

To run the code:
```python
python pdf2image.py
```
## Data cleansing

Before data cleansing, please make sure your files are sorted in the following format(here we will use our dataset for instance):
```
└─title

	└─images (folder including all images)
 
	└─labels (folder including all labels)
```
(for label files. please refer to the following section "Data labeling")

then, run the code:
```python
python cleansing.py
```

The result should be in the following format. You can change the ratio of images in train/test/valid in the "cleansing.py"
```
└── yolov8_dataset

	└── train
 
		└── images (folder including all training images)
  
		└── labels (folder including all training labels)
  
	└── test
 
		└── images (folder including all testing images)
  
		└── labels (folder including all testing labels)
  
	└── valid
 
		└── images (folder including all testing images)
  
		└── labels (folder including all testing labels)
```
## Data labeling

You may get confused where the labeled files come from, here is the entire process:

1.Open the link of Make Sense: https://www.makesense.ai/ , click "Get Started" to start

2.Upload all images, and add the label(s) you need

3.Tedious labeling

4.Once labeling finished, click "Action" --> "export annotation", remember to select "yolo" format

Now the data labeling is done
