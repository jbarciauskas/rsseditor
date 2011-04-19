import urllib2
from BeautifulSoup import BeautifulStoneSoup
from propertyaccessor.PropertyAccessor import PropertyAccessor

class RssEditor:
    def __init__(self, feedLoader):
        self.feedLoader = feedLoader

    def renderFeed(self):
        soup = BeautifulStoneSoup(self.feedLoader.retrieve())
        entries = soup('item')
        itemList = []
        pathTemplate = "[{0}].{1}.string"
        i = 0
        for entry in entries:
            itemDict = {}
            for value in ['link', 'title', 'description']:
                itemDict[value] = {}
                itemDict[value]['path'] = pathTemplate.format(i, value)
            itemDict['title']['value'] = entry.title.string.encode('utf8')
            itemDict['description']['value'] = entry.description.string
            itemDict['link']['value'] = entry.link.string
            i += 1
            itemList.append(itemDict)
        return itemList

    def edit(self, path, newValue):
        soup = BeautifulStoneSoup(self.feedLoader.retrieve())
        entries = soup('item')
        wrapper = PropertyAccessor(entries)
        wrapper.setValue(path, newValue)
        self.feedLoader.save(soup.prettify())
        return self.renderFeed()

class FeedLoader:
    feeds = []
    def __init__(self, feedKey=None):
        self.feedKey = feedKey

    def add(self, url):
        page = urllib2.urlopen(url)
        feedString = page.read()
        index = len(FeedLoader.feeds)
        FeedLoader.feeds[index:] = [feedString]
        self.feedKey = index
        return index

    def retrieve(self,feedKey=None):
        if(feedKey == None):
            if(self.feedKey == None):
                raise Exception("No feed key set when retrieving")
            else:
                return FeedLoader.feeds[self.feedKey]
        else:
            return FeedLoader.feeds[feedKey]

    def save(self, feedString, feedKey=None):
        if(feedKey == None):
            if(self.feedKey == None):
                raise Exception("No feed key set when saving")
            else:
                FeedLoader.feeds[self.feedKey] = feedString
        else:
            FeedLoader.feeds[feedKey] = feedString

