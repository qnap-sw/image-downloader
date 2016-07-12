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
    print csv_data
    for task in csv_data[3:]:
        crawler = PictureCrawler()
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

        if crawler.Action.startswith('#'):
            print crawler.Action + 'is inactive'
        elif crawler.Action == 'image.query.download':
            print "run task: " + "search " + crawler.Query + "....."
            crawler.handle_download(crawler.handle_search())
        else:
            print 'unknown action'
