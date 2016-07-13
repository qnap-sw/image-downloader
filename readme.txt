Setup
------------
step 1: install Firefox
step 2: install pip
key command for terminal:
easy_install pip

step 3: install python site-package
key command for terminal:
pip install Google-Search-API
pip install Google-Search-API --upgrade

step 4:
key command for terminal: 
git clone https://github.com/qnap-sw/Google-Search-API.git
or browser download and unzip

step 5: copy unzip Google-Search-API/google/modules/images.py to site-packages/modules/images.py
mac site-package location: /Users/${username}/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/google/modules/images.py

step 6:
key command for terminal:  
git clone https://github.com/qnap-sw/image-downloader.git
or browser download and unzip

Usage
------------
cd image-downloader-master
python main.py [csv file]
