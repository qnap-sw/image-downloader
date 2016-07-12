from google import google, images
import os
import time    
import json


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
        self.ImageType = 'any'
        self.FileType = 'any'
        self.DownloadPath = os.path.dirname(os.path.realpath(__file__)) + "/pictures"
        self.ImageSizeIndex = {
            'large': 'l',
            'medium': 'm',
            'icon': 'i',
            'qsvga': 'qsvga',
            'vga': 'vga',
            'svga': 'svga',
            'xga': 'xga',
            'MP_2': '2mp',
            'MP_4': '4mp',
            'MP_6': '6mp',
            'MP_8': '8mp',
            'MP_10': '10mp',
            'MP_12': '12mp',
            'MP_15': '15mp',
            'MP_20': '20mp',
            'MP_40': '40mp',
            'MP_70': '70mp'
        }
        self.AspectRatioIndex = {
            'tall': 't',
            'square': 's',
            'wide': 'w',
            'panoramic': 'xw'
        } 
        self.ColorTypeIndex = {
            'full color': 'color',
            'black-white': 'gray',
            'transparent': 'trans',
            'color.red': 'red',
            'color.green': 'green',
            'color.blue': 'blue'
        }
        self.ImageTypeIndex = {
            'face': 'face',
            'photo': 'photo',
            'clip-art': 'clipart',
            'line-drawing': 'lineart',
            'animated': 'animated'
        }

        self.FileTypeIndex = {
            'jpg': 'jpg',
            'gif': 'gif',
            'png': 'png',
            'bmp': 'bmp',
            'svg': 'svg',
            'webp': 'webp',
            'ico': 'ico'
        }

        self.SearchLog = {
            'Action': self.Action,
            'Search engine': self.SearchEngine,
            'Query': self.Query,
            'Limit': self.Limit,
            'Aspect ratio': self.AspectRatio,
            'Color in image': self.ColorType,
            'File type': self.FileType,
            'Download path': self.DownloadPath
        }
      
    def handle_search(self):
        if self.Query is not None:
            options = images.ImageOptions()
            if self.ImageSize != 'any':
                if self.ImageSize not in ['large','medium','icon']:
                    options.larger_than = self.ImageSizeIndex[self.ImageSize]
                else:
                    options.size_category = self.ImageSizeIndex[self.ImageSize]
            if self.ImageType != 'any':
                options.image_type = self.ImageTypeIndex[self.ImageType]
            if self.ColorType != 'any':
                if self.ColorType not in ['full color', 'black-white', 'transparent']:
                    options.color = self.ColorTypeIndex[self.ColorType]
                else:
                    options.color_type = self.ColorTypeIndex[self.ColorType]
            if self.AspectRatio != 'any':
                options.aspect_ratio = self.AspectRatioIndex[self.AspectRatio]
            if self.FileType != 'any':
                options.file_type = self.FileTypeIndex[self.FileType]
        results = google.search_images(self.Query, options, num_images=int(self.Limit))
        return results

    def handle_download(self, search_results):
        folder_name = time.strftime("%Y%m%d%H:%M:%S", time.localtime())
        save_dir = self.DownloadPath + "/" + folder_name
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        images.fast_download(search_results, path=save_dir, threads=12)
        with open(save_dir + '/search_record.log', 'w') as outfile:
            json.dump(self.SearchLog, outfile)
