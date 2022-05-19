### This extension currently fills the first captcha which is kids play because the label for captcha can be found in the DOM tree. It would be good if it were able to fill the second Captcha.

The task at our hand is to make the extension fill the second captcha.
We would require the following

1. ~~dataset for captcha images,~~
2. ~~a preprocessing function,~~
3. ~~a deep learning model to classify the image,~~
4. writing the same preprocessing function using opencv.js
5. Loading the model in tensorflow.js
6. Extracting the captcha image from browser cache

Problems
--------

I'm a complete novice at Javascript, all my attempts of writing a content script go in vain. The problems I faced include 

1. not being able to import opencv.js in a content script.
2. the captcha image on 2nd page of AIMS is accessible only once, that is when the browser loads it. So, either it must be taken from cache or a new captcha should be generated and retrieved directly (my thoughts).
   
-------
A CNN model with 99.6% accuracy on this captcha dataset can be found [here](https://github.com/cmaspi/Defeating-AIMS-Captcha)

