## Welcome to Aims captcha defeator

This extension will help you bypass the first captcha on the aims website, the next big version of this extension will include a text detection model to bypass the second captcha as well, but for now, it will only fill the first captcha for you.
(Star this repository if you like it)
### How to install (for debian)
> sudo apt-get install subversion     
> svn checkout https://github.com/cmaspi/extension/trunk/captchaDefeator  

Go to your browser, switch on the developer mode in extensions, then add extension by selecting captchaDefeator

You can refer 
### 1. [Tutorial for brave](https://github.com/cmaspi/extension/blob/main/captchaDefeator/tutorials/brave_tutorial.pdf)
### 2. Tutorial for firefox
    1. Go to about:debugging#/runtime/this-firefox
    2. Then click on Load Temporary Add-on
    3. Then select manifest.json in the downloaded directory


### How this extension works?
The first login page has a really bad captcha, the src link of the captcha which can be found in the html of the page has the captcha text itself. The extension just exploits this fact. Additionally, this would contribute in the second part of this extension that is to train a model which can solve captcha on second page since that isn't labelled. You can check the [captcha dataset](https://github.com/cmaspi/extension/tree/main/dos/images) I built by running my [python script](https://github.com/cmaspi/extension/blob/main/dos/getImage.py) that downloads labelled captcha images from aims.
### Next Goal
The next goal of this extension is to bypass the captcha on the second page, this would require CNN, if you want to build one on your own, you can refer my [pre-processing functions](https://github.com/cmaspi/extension/blob/main/initial_phase/total.py)

### Features
You can also just now press enter after entering your credentials to login unlike without this extension where you would have to drag your cursor to click on "sign in"
