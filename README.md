# Empty Bottle Detection System

This project aims to develop an additional feature for a cocktail maker machine by implementing an empty bottle
detection system. The objective is to enable the robot to determine whether a bottle is empty or still filled. The
development of
this feature is crucial for ensuring efficient and accurate cocktail preparation.

We considered a variety of methodologies, including the utilization of pre-trained AI models. There were certain
advantages and disadvantages associated with this approach that influenced our decision not to employ it in this
specific project. Currently, our primary focus revolves around the implementation of Python-based image processing code
specifically designed for different bottle types. We aim to significantly improve the system's ability to identify and
differentiate between empty and filled bottles. This approach holds promise for improving the detection accuracy by
leveraging advanced image analysis algorithms.

## Assumptions and Limitations

To achieve this goal, various techniques were explored to capture readable photos of the bottle system for detection
purposes. The initial approach involved utilizing the robot's built-in camera, but it proved ineffective due to
positioning limitations and resulting in unclear images. Subsequently, an alternative method utilizing LED lights and
strips to enhance visibility of the liquid level was attempted, but it did not yield satisfactory results.

### The Robot’s Built-in Camera

The use of the built-in camera of the cocktail maker robot for bottle detection presented several challenges and
limitations, which led us to explore alternative approaches.

- Positioning Constraints: Due to the inherent design and positioning of the robot, it was not feasible to directly face
  the camera towards the bottle area for capturing clear and accurate images. The location of the robot arm, situated at
  the back side of the bottle system, introduced
  numerous obstacles and potential sources of interference between the camera and the bottles. These obstacles
  obstructed the camera's line of sight, further compromising the quality of the captured images and impeding the
  detection process.
- Image Resolution: Another limitation was the inadequate resolution of the images captured by the robot's camera. The
  low resolution resulted in a lack of detail, making it difficult to differentiate the contents of the bottles
  accurately.
  This constraint significantly hindered the effectiveness of the bottle detection system.

Examples:

- [Image-1](./images/robot-camera-1.png)
- [Image-2](./images/robot-camera-2.png)
- [Image-3](./images/robot-camera-3.png)
- [Image-4](./images/robot-camera-4.png)

### Lights

Another aspect that was explored to enhance the empty bottle detection system was the implementation of lighting
techniques.
However, the trials conducted with different lighting configurations yielded unsatisfactory results. Two different
approaches were attempted, each with its own limitations:

- Single LED Lights on Top of Each Bottle: Initially, single LED lights were placed on top of each bottle in an attempt
  to improve visibility and facilitate differentiation between empty and filled sections. The use of individual LED
  lights added unwanted shadows and uneven
  illumination, making it more challenging to accurately detect the bottle contents.
  Examples:
    - [Image-5](./images/robot-camera-5.png)
    - [Image-6](./images/robot-camera-6.png)
    - [Image-7](./images/robot-camera-7.png)
- LED Strip Placement in the Middle of Bottles: As an alternative, an LED strip was positioned in the middle of the
  bottles to provide uniform lighting and emphasize the distinction between empty and filled parts. However, similar to
  the previous method, this approach also resulted in poorer image quality. The LED strip caused reflections and glares
  on the bottles, introducing additional noise and hindering the accuracy of the bottle detection process.
  Examples:
    - [Image-8](./images/robot-camera-8.png)
    - [Image-9](./images/robot-camera-9.png)
    - [Image-10](./images/robot-camera-10.png)
    - [Image-11](./images/robot-camera-11.png)

In summary, the trials conducted with different lighting techniques, including single LED lights and LED strips, did not
yield the desired results and led to a degradation in image quality. As a result, the decision was made to continue the
bottle detection system development without additional lighting.

### Image Background

Another significant limitation arose from the complexity of the image background. Even if we were to use smartphone
camera with
superior image quality and ensure an unobstructed view of the bottle system, the image recognition module would face
difficulties in accurately detecting the bottles due to the irregular and cluttered background. The presence of a
non-uniform or visually busy background can introduce unnecessary visual noise, making it harder for
the image recognition module to distinguish the bottles from their surroundings. This limitation becomes particularly
apparent when relying on computer vision algorithms that rely on identifying specific patterns and features within the
image.

Examples:

- [Image-12](./images/busy-background-1.JPG)
- [Image-13](./images/busy-background-2.JPG)
- [Image-14](./images/busy-background-3.JPG)
- [Image-15](./images/busy-background-4.JPG)

To address this limitation, we recognized the need for a more controlled environment. It led us to implement a white
background within the system. By utilizing a simple and uniform background, such as white, we aim to reduce background
distractions and improve the accuracy of the bottle detection system. The white background provides a clear contrast
against the bottles, enhancing the visibility of their shapes and features, thereby facilitating more effective image
recognition.

Examples:

- [Image-16](./images/white-background-1.JPG)
- [Image-17](./images/white-background-2.JPG)
- [Image-18](./images/white-background-3.JPG)
- [Image-19](./images/white-background-4.JPG)

## Methodologies Discarded (Testing Failures)

### Contours

Contours provide an effective way to separate objects from the background, especially when the
background is uniform, such as a white background. However, first we needed to extract the white plane from the whole
image. So that, we used two-layer contour finding approach to enhance the precision of object recognition in our image
processing system. In the first layer, our algorithm discerns the white surface from the background, enabling us to
isolate the specific region of interest. In the second layer, we leverage this recognized white surface to
further isolate and identify bottles within the designated area. To achieve this goal, we applied the following steps
and code can be found [here](./coctail-machine/countours/countours.py):

- The input image is converted into a black and white format, reducing it to a single channel. This simplifies the
  task of identifying object boundaries.
- GaussianBlur is applied to the image to reduce noise and smoothen it. This step helps to make the edges more
  pronounced and continuous.
- Thresholding operation is used to create a binary image, where pixel values below a
  specified [threshold](./images/countours-1.png) are set to
  black, while those above it are set to white. This [binary image](./images/countours-2.png) serves as the basis for
  contour detection.
- Apply the Canny edge detection algorithm to the thresholded image. This step will highlight the edges of objects
  within the binary image, making them stand out more.
    - As previously mentioned, our initial objective was to utilize contour detection to locate the white surface.
      Unfortunately, the presence of a whiteboard in the room, which shared a similar color with the white surface,
      posed a significant challenge. The Canny edge detection algorithm proved [ineffective](./images/countours-3.png)
      in distinguishing between the edges of the white surface and those of the whiteboard due to their color
      resemblance. However, we decided to proceed with contour finding as Canny showed success in highlighting the
      precise edges of the bottles within the same visual space.
- The findContours function in OpenCV is then utilized to locate and extract the contours of the bottles within the
  processed image. This algorithm allows for the precise identification and extraction of bottle shapes within the
  image, facilitating subsequent analysis and object recognition tasks in computer vision applications.

#### Conclusion

In conclusion, our experience with contour detection methodology has demonstrated its limitations as a reliable approach
for our specific use case. It became evident that even minor variations in the image necessitated the adjustment of
hardcoded parameters, which unfortunately failed to consistently yield [accurate results](./images/countours-4.png).
This realization underscores the need for a more adaptable and robust solution that can better accommodate the dynamic
nature of our visual data, ensuring a higher degree of accuracy and reliability in object recognition.

### Pre-trained AI models

- Generalization: Pre-trained models, having been trained on extensive datasets, often have a superior ability to
  generalize from diverse data, making them adaptable to various scenarios and environments. This adaptability can be a
  significant advantage when dealing with the diverse range of bottle shapes and environmental conditions our system
  might encounter.
- Lack of Specific Models: One of the primary limitations of pre-trained models is the unavailability of models
  specifically trained for the task of detecting empty or filled bottles. Most pre-trained models are designed for
  generic object detection or classification and may not suit the unique characteristics of our application.
- Fine-Tuning Complexity: Fine-tuning a pre-trained model for a specific task, such as empty bottle detection, can be a
  complex and resource-intensive process. It often requires a substantial amount of labeled data for the new task and
  extensive computational resources for training. Given that our project necessitates the identification of bottle fill
  levels, the costs and complexities associated with fine-tuning a model for this specific purpose were prohibitive.

We considered pre-trained models for image classification such as VGG16, ResNet50, and InceptionV3 for their performance
in generic object classification. However, these models, while excellent for general image recognition, do not meet the
specific requirements of our bottle detection task. For object detection, we also explored models like Faster R-CNN,
YOLO, and SSD. These models are particularly well-suited for identifying and localizing objects within an image.
Nevertheless, our project's focus on detecting empty or filled bottles necessitates a custom approach due to the unique
nature of our task.

#### Conclusion

As there are no readily available pre-trained models tailored to the specific task of detecting empty or filled bottles,
and fine-tuning these models can be resource-intensive, we opted for a different approach. Instead, we chose to focus on
efficient image processing techniques. These techniques, including thresholding, edge detection, and contour analysis,
allow us to extract essential features like the bottle's outline and water level without the need for extensive
computational resources. This approach aligns with the efficiency requirements of the cocktail machine and the
complexities of our diverse real-world operating conditions.

### HSV Color Space

The HSV (Hue, Saturation, Value) color space was explored as a potential method for bottle detection within the cocktail
machine's environment. The HSV color space wasn't selected because bottles exhibit a wide range of colors, making
color-based filtering alone insufficient for distinguishing empty and filled bottles, especially when [color variations
are significant](./images/hsv.png). Additionally, this method is most effective when detecting objects with consistent
color ranges, which may not apply to our task. Real-world scenarios, like the dynamic environment of the cocktail maker
robot, can introduce unpredictable factors affecting color perception. This can lead to inconsistent and less reliable
results.

#### Conclusion

We chose an alternative approach involving image processing methods such as template matching. This
methods provide a more versatile and robust means of detecting empty and filled bottles, regardless of color or
environmental conditions, better meeting the project's specific requirements.

## Methodology

### Template Matching - Bottle Extraction

OpenCV template matching is primarily relies on pixel-level comparisons without considering higher-level features. As a
result of our experimentation, template matching
mode [TM_CCOEFF_NORMED](./cocktail-machine/template_matching/find_best_template_matching_mode.py) gave the highest
performance within 6 modes; TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, M_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED.

Examples:

- [Result-1](./images/result-1.png)

### Image Processing - Bottle Fill Level

The selection of OpenCV image processing methodologies was a strategic decision aimed at precisely and
efficiently assessing the liquid levels contained within the bottles. Leveraging OpenCV's versatile and well-established
toolkit for image processing, the approach incorporated a series of essential steps as describe below:

- The images used are from a monochrome camera but saved as three-channel image files. However, only one channel is used
  for processing as all three are identical.
- The images show poor contrast and reflective patches along the bottle's edge.
- A Gaussian kernel is applied to smooth the image, reducing noise while preserving its structure.
- An image histogram is plotted to identify an appropriate threshold for separating the liquid from the rest of the
  image.
- Poor contrast in the histogram is noted.
- A global threshold is manually chosen from the histogram, and an inverted binary image is created using threshold
  function.
- The resulting binary image captures the liquid but also includes parts of the bottle's top and less illuminated glass
  areas.
- The next step involves using OpenCV's findContours() function to identify foreground shapes.
- To identify the main contour representing the liquid, contours are sorted by area, and the largest one is selected and
  outlined over the original image.
- After selecting the correct contour, a bounding box is drawn around it, and its aspect ratio (width-to-height ratio)
  is calculated.
- The aspect ratio value can be used to determine the fill level of the bottle, and a threshold can be set to identify
  low liquid levels.

Examples:

- [Result-2](./images/result-2.png)
- [Result-3](./images/result-3.png)
- [Result-4](./images/result-4.png)

#### Conclusion

While the previously mentioned approach is effective and yields accurate results in environments with stable conditions,
it's important to acknowledge that it may necessitate fine-tuning when introduced to settings where variables are
subject to change. Even minor alterations in the environment, such as variations in lighting or liquid
properties, can significantly impact the behavior of the detection system. In such dynamic environments, adaptability
becomes crucial. Thus, ongoing monitoring and adjustments to the algorithm's parameters may be required to maintain
reliable liquid level detection and ensure that the system can effectively respond to the evolving conditions,
reflecting the inherent sensitivity of computer vision applications to environmental changes.

## CPEE - Model Integration

The CPEE is accessible via the following
link: [CPEE Execution Interface](https://cpee.org/flow/edit.html?monitor=https://cpee.org/flow/engine/22616/). Our model
is named "test.xml" and resides within the "liquid-level" folder.

Our model accepts an input in the form of an image in base64 format. Specifically, it expects an overall image of the
cocktail maker machine with multiple bottles present. The CPEE orchestrates the execution of the model and returns three
boolean variables indicating the fullness of three distinct bottle types.

The execution process within the CPEE is broken down into several key steps:

- Initialization ("Base"): This initial step initializes all the variables required for the model's operation.

- Service Call ("Crop Bottles"): In this step, the CPEE makes a service call to an endpoint labeled "cropbottles." This
  service is responsible for identifying and cropping each individual bottle from the input image, saving them as
  base64-encoded images within an array of three.

- Service Calls ("Get 'X' Fill Level"): Following the "cropbottles" step, there are three subsequent service calls to
  the "filllevels" endpoint. These calls are made three times, each time with a specific bottle type. The CPEE sets the
  variables that represent the fullness of the bottles to the determined values for each bottle.

The execution process, orchestrated by the Cloud Process Execution Engine, allows us to process an image of the cocktail
machine and determine the fullness of three different bottle types. This integration provides information to increase
the functionality of the cocktail machine.

## Run the code

### Deploy the code

```sh
git clone https://github.com/yigitpolat/praktikum.git
cd praktikum
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 cocktail-machine/template_matching_service/main.py
```

### Make API requests

- Option
  1: [Use Cloud Process Execution Engine (CPEE)](https://cpee.org/flow/edit.html?monitor=https://cpee.org/flow/engine/22616/)
- Option 2: Use Postman by importing the [data](./postman-collection/postman_collection.json)

## Authors

- Didem Öngü (didem.oengue@tum.de)
- Yigit Polat (yigit.polat@tum.de)

