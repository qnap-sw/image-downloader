import csv 
import sys

#resolved csv
# row 1 is key, row 2 is options, row 3 4... is value
csv_name = raw_input("please input csv name: ")
csv_file = open(csv_name)
csv_reader = csv.reader(csv_file)
csv_data = list(csv_reader)

from Crawler import PictureCrawler

class mainApp(object):

    # set search option
	for task in csv_data[3:]:crawler = PictureCrawler()
	    crawler.Action = task[0]
	    crawler.SearchEngine = task[1] 
	    crawler.Query = task[2]
	    crawler.Limit = task[3]
	    crawler.ImageSize = task[4]
	    crawler.AspectRatio = task[5]
	    crawler.Color = task[6]
	    crawler.ImageType = task[7]
	    crawler.FileType = task[8]

	    if task[9] != "":
	    	crawler.DownloadPath = task[9]
            if crawler.Action == 'image.query.download':
            	crawler.handle_download(crawler.handle_search())
            else:
                print crawler.Action + 'is inactive'




