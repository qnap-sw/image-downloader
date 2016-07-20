import csv
import sys

# resolved csv
# row 1 is key, row 2 is options, row 3 4... is value
# csv_name = raw_input("please input csv name: ")
csv_name = sys.argv[1]
csv_file = open(csv_name)
csv_reader = csv.reader(csv_file)
csv_data = list(csv_reader)

from Crawler import PictureCrawler


class MainApp(object):

    # need to check action
    for index, task in enumerate(csv_data[2:]):
        crawler = PictureCrawler()
        crawler.CsvIndex = index + 3
        crawler.Action = task[0]
        crawler.SearchEngine = task[1]
        crawler.Query = task[2]
        crawler.Limit = task[3]
        crawler.ImageSize = task[4]
        crawler.AspectRatio = task[5]
        crawler.ColorType = task[6]
        crawler.ImageType = task[7]
        if task[8] != "":
            crawler.FileType = task[8]
        if task[11] != "":
            crawler.DownloadPath = task[11]

        # set log information
        crawler.SearchLog['Action'] = crawler.Action
        crawler.SearchLog['Search engine'] = crawler.SearchEngine
        crawler.SearchLog['Query'] = crawler.Query
        crawler.SearchLog['Limit'] = crawler.Limit
        crawler.SearchLog['Aspect ratio'] = crawler.AspectRatio
        crawler.SearchLog['Image size'] = crawler.ImageSize
        crawler.SearchLog['Color in image'] = crawler.ColorType
        crawler.SearchLog['Image type'] = crawler.ImageType
        crawler.SearchLog['File type'] = crawler.FileType
        if task[11] != "":
            crawler.SearchLog['Download path'] = crawler.DownloadPath

        if crawler.Action.startswith('#'):
            print crawler.Action + 'is inactive'
        elif crawler.Action == 'image.query.download':
            results = crawler.handle_search()
            print "run task: " + "search " + crawler.Query + "....."
            crawler.handle_download(results)
        else:
            print 'unknown action'

    print "Complete all tasks....."
