from google import google, images
import os
import time


class PictureCrawler(object):

    # search conditions
    def __init__(self):
        self.Action = 'image.query.download'
        self.SearchEngine = 'google'
        self.Query = None
        self.Limit = 50
        self.ImageSize = 'any'
        self.AspectRatio = 'any'
        self.ColorType = 'any'
        self.IamgeType = 'any'
        self.FileType = 'any'
        self.DownloadPath = os.path.dirname(os.path.realpath(__file__)) + "/pictures"
  
    def handle_search(self):
        if self.Query is not None:
            options = images.ImageOptions()
            if self.ImageSize != 'any':
                if self.ImageSize not in ['any','large','medium','icon']:
                    options.larger_than = self.ImageSize
                else:
                    options.size_category = self.ImageSize
            if self.ImageType != 'any':
                options.image_type = self.ImageType
            if self.ColorType != 'any':
                if self.ColorType not in ['color','gray']:
                    options.color = self.ColorType
                else:
                    options.color_type = self.ColoType
            results = google.search_images(self.Query, options, num_images = int(self.Limit))
            return results

    def handle_download(self, searchResults):
        folderName = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        save_dir = self.DownloadPath + "/" + folderName
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        images.fast_download(searchResults, path = save_dir, threads=12)
        



    

