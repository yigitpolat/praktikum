# Empty Bottle Detection System

This project aims to develop an additional feature for a cocktail maker robot by implementing an empty bottle detection
system. The objective is to enable the robot to determine whether a bottle is empty or still filled. The development of
this feature is crucial for ensuring efficient and accurate cocktail preparation.

To achieve this goal, various techniques were explored to capture readable photos of the bottle system for detection
purposes. The initial approach involved utilizing the robot's built-in camera, but it proved ineffective due to
positioning limitations and resulting in unclear images. Subsequently, an alternative method utilizing LED lights and
strips to enhance visibility was attempted, but it did not yield satisfactory results.

Currently, our primary focus revolves around the implementation of Python-based image processing code specifically
designed for different bottle types. We aim to significantly improve the system's ability to identify and differentiate
between empty and filled bottles. This approach holds promise for improving the detection accuracy by leveraging
advanced image analysis algorithms.

In summary, this project aims to develop an additional feature for a cocktail maker robot – an empty bottle detection
system. By implementing effective techniques for capturing and analyzing bottle images, the robot will be able to
identify whether each bottle is empty or filled. This feature will significantly enhance the cocktail-making process,
ensuring optimal ingredient management and facilitating efficient and precise mixology.

## Assumptions and Limitations

TODO: Add related images - Didem

### The Robot’s Built-in Camera

The use of the built-in camera of the cocktail maker robot for bottle detection presented several challenges and
limitations, which led us to explore alternative approaches.

- Positioning Constraints: Due to the inherent design and positioning of the robot, it was not feasible to directly face
  the camera towards the bottle area for capturing clear and accurate images. The camera's fixed placement restricted
  its ability to obtain a direct view of the bottle system, which compromised the quality and clarity of the captured
  images.
- Image Resolution: Another limitation was the inadequate resolution of the images captured by the robot's camera. The
  low resolution resulted in a lack of detail, making it difficult to discern the contents of the bottles accurately.
  This constraint significantly hindered the effectiveness of the bottle detection system.
- Obstacles and Interference: The location of the robot arm, situated at the back side of the bottle system, introduced
  numerous obstacles and potential sources of interference between the camera and the bottles. These obstacles
  obstructed the camera's line of sight, further compromising the quality of the captured images and impeding the
  detection process.

Considering these limitations, it became evident that an alternative solution was necessary to overcome the positioning
challenges, improve image resolution, and mitigate obstacles and interference. Hence, the focus shifted towards
implementing a different approach, employing Python image processing techniques, to enhance the accuracy and reliability
of the bottle detection system. By leveraging advanced image analysis algorithms, we aim to address these limitations
and achieve more robust and precise bottle detection results.

### Image Background

Another significant limitation arose from the complexity of the image background. Even if we were to use a camera with
superior image quality and ensure an unobstructed view of the bottle system, the image recognition module would face
difficulties in accurately detecting the bottles due to the irregular and cluttered background.

The presence of a non-uniform or visually busy background can introduce unnecessary visual noise, making it harder for
the image recognition module to distinguish the bottles from their surroundings. This limitation becomes particularly
pronounced when relying on computer vision algorithms that rely on identifying specific patterns and features within the
image.

To address this limitation, we recognized the need for a more controlled environment. It led us to implement a white
background within the system. By utilizing a simple and uniform background, such as white, we aim to reduce background
distractions and improve the accuracy of the bottle detection system. The white background provides a clear contrast
against the bottles, enhancing the visibility of their shapes and features, thereby facilitating more effective image
recognition.

It is important to acknowledge that this solution necessitates specific environmental conditions and requires careful
setup and calibration. Any variations or deviations from the controlled white background may adversely affect the
system's performance and introduce potential inaccuracies.

In summary, the irregular and visually complex image background presented a significant limitation for accurate bottle
detection, even with a higher-quality front-facing camera. The adoption of a controlled white background within the
system was identified as a suitable solution to mitigate this limitation and enhance the effectiveness of the image
recognition module.

### Lights

Another aspect that was explored to enhance the bottle detection system was the implementation of lighting techniques.
However, the trials conducted with different lighting configurations yielded unsatisfactory results. Two different
approaches were attempted, each with its own limitations:

- Single LED Lights on Top of Each Bottle: Initially, single LED lights were placed on top of each bottle in an attempt
  to improve visibility and facilitate differentiation between empty and filled sections. Surprisingly, this approach
  resulted in a deterioration of image quality. The use of individual LED lights added unwanted shadows and uneven
  illumination, making it more challenging to accurately detect the bottle contents.
- LED Strip Placement in the Middle of Bottles: As an alternative, an LED strip was positioned in the middle of the
  bottles to provide uniform lighting and emphasize the distinction between empty and filled parts. However, similar to
  the previous method, this approach also resulted in poorer image quality. The LED strip caused reflections and glares
  on the bottles, introducing additional noise and hindering the accuracy of the bottle detection process.

Considering the limitations encountered in the lighting trials, the decision was made to proceed without additional
lights. It was determined that the existing lighting conditions, when combined with the implemented white background,
provided a sufficient level of illumination and contrast for accurate bottle detection.
It is important to note that the absence of additional lighting may limit the system's performance in certain
challenging lighting conditions, such as low light environments. However, given the limitations observed with the
attempted lighting configurations, it was deemed more practical and effective to rely on the inherent lighting
conditions and concentrate efforts on improving the image processing algorithms.
In summary, the trials conducted with different lighting techniques, including single LED lights and LED strips, did not
yield the desired results and led to a degradation in image quality. As a result, the decision was made to continue the
bottle detection system development without additional lighting. While this approach may have limitations in challenging
lighting conditions, it allows us to focus on refining the image processing algorithms to achieve accurate bottle
detection using the available lighting conditions.

## Bottle Extraction from Images

### Testing Failures: Methodologies Discarded


#### Template Matching

OpenCV template matching is primarily relies on pixel-level comparisons without considering higher-level features. As a
result of our experimentation, template matching mode TM_CCOEFF_NORMED gave the highest performance within 6 modes;
TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, M_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED. 

we saw that template matching was working incorrectly due to the following
items.

- Bottle Shapes: The large variation in bottle shapes, sizes, and orientations can make it challenging to find a single
  template that accurately represents all instances of bottles. Eventhough if we try to get a template for each bottle,
  which is not feasible for the efficiency of the cocktail machine, it does not seem reasonable to solve the problems in
  the next item.
- Environmental Factors: Template matching relies on finding exact matches, and even slight variations in the appearance
  of bottles, such as different lights or reflection can lead to inaccurate results.
  Therefore, alternative approaches such as deep learning-based object detection algorithms, which can learn and
  generalize from large datasets, might be more suitable for reliable bottle detection in diverse real-world scenarios.

### Pre-trained AI models

- Image Classification: VGG16, ResNet50,
  InceptionV3: https://learnopencv.com/image-classification-pretrained-imagenet-models-tensorflow-keras/
- Object Detection: Faster R-CNN, YOLO, SSD. https://foundationsofdl.com/2019/06/02/visual-recognition/

### HSV Color Space

- https://www.freedomvc.com/index.php/2022/01/17/basic-background-remover-with-opencv/

### Edge Detection Algorithms

#### Canny

- https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html

#### Contours

- https://learnopencv.com/edge-detection-using-opencv
- https://docs.opencv.org/3.4/d3/d05/tutorial_py_table_of_contents_contours.html
- https://learnopencv.com/contour-detection-using-opencv-python-c/#contour-applications

### Methodology

As deep learning models require large amounts of labeled training data and extensive computational resources for
training, efficient image processing techniques are chosen when developing an application to find bottle fill level. By
leveraging traditional image processing algorithms such as thresholding, edge detection, and contour analysis, it
becomes possible to extract relevant features like the bottle's outline and water height.

## Run the code

```sh
git clone <git-url>
cd <cloned-directory>
python3 -m venv venv
source venv/bin/activate
pytno3 -m pip install -r requirements.txt


```

## Authors

- Didem Öngü (didem.oengue@tum.de)
- Yigit Polat (yigit.polat@tum.de)

