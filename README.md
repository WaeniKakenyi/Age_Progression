# **Age Progression/Regression by Generative Adversarial Network (GAN) Project**

![my-image jpg](https://user-images.githubusercontent.com/110460207/212765482-111aa449-eb24-4e8d-934b-8e1e72a16c9e.png)



##
The goal of this project is to generate an image or video of a person as they would look at a future point in time. This can be used for various purposes such as forensic investigations, personal curiosity, or creating visual effects in movies and TV shows.

# **Pre- requisites** 
* Python 3.7.9
* TensorFlow v2.11
* Pytorch 1.0.

# **Datasets**
UTKFace (Access from the [github link](https://susanqq.github.io/UTKFace/))

## Prepare the training dataset
You may use any dataset with labels of age and gender. In this demo, we use the UTKFace dataset. It is better to use aligned and cropped faces. Please save and unzip `UTKFace.tar.gz` to the folder `data`.


# **Data Pre-processing**
* Resizing & Normalization - We resize the images to a uniform size and normalize the pixel values to a range of between o and 1 to help converge the model better
* Data Augmentation - Generating additional training data by applying random transformations to the original images to help the model learn better such as rotation range, zoom range, horizontal flip, fill mode. 
* Noise Reduction - This helps the learning of the model easier as it identifies patterns and helps with the ovefitting












## Deployment 
Based on our evaluation,       model was the best based on our         criteria, so we deployed it. We used Streamlit to deploy the model, where users can upload images. After uploading the photo, the model provides an image as young or old, based on how the user uses the slider tool to indicate the age they want to view. This is the link to the deployed model.

## Citation 
* Zhifei Zhang, Yang Song, and Hairong Qi. "Age Progression/Regression by Conditional Adversarial Autoencoder." IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017.
* Elmahmudi, A., Ugail, H. A framework for facial age progression and regression using exemplar face templates. Vis Comput 37, 2023–2038 (2021).
* @inproceedings{Li2020AgePA,
title={Age Progression and Regression with Spatial Attention Modules},
author={Qi Li and Yunfan Liu and Zhenan Sun},
booktitle={AAAI},
year={2020}
}


## License

GNU General Public License v3.0

## 🔗 Badges

![numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![tensorflow](https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=blue)
![keras](https://img.shields.io/badge/keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![openCV](https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=black)
![streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=pink)
![pytorch](https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=orange)
![scikitlearn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
