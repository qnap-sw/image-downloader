# image-downloader
Download multiple Google search images via a csv condition

## Requirement
easy_install ,pip , git ,Firefox

Please note that you should also install PhantomJS (headless browser) in order to use images search.
Image search uses the selenium & the phantomjs driver, therefore you MUST have [PhantomJS installed](https://www.npmjs.com/package/phantomjs) to use it.


Installation
------------
install phantomjs
```
sudo npm install -g phantomjs
```
install python site-package Google-Search-API
```
pip install git+https://github.com/qnap-sw/Google-Search-API.git
```
download the main process
```
git clone https://github.com/qnap-sw/image-downloader.git
```
Usage
------------
```
cd image-downloader
python main.py [csv name]
```



