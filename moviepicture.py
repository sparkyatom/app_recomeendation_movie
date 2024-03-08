def pic_downloader(name):
    from icrawler.builtin import GoogleImageCrawler

    # storage is the directory where the images will be saved
    google_Crawler = GoogleImageCrawler(storage={'root_dir': r'C:\Users\sande\Desktop\HANDS ON MACHINE LEARNING\pics'})

    # keyword is the search query
    # max_num is the number of images to be downloaded
    google_Crawler.crawl(keyword=name+"movie", max_num=10,overwrite=True)

