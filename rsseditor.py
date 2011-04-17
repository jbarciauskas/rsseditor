import urllib2
import feedparser
from propertyaccessor.PropertyAccessor import PropertyAccessor

class RssEditor:
    def __init__(self, feedLoader):
        self.feedLoader = feedLoader

    def renderFeed(self):
        entries = self.feedLoader.retrieve()
        itemStrings = []
        divTemplate = '<div class="{0}" path="entries[{1}].{0}">{2}</div>\n'
        i = 0
        for entry in entries:
            itemStrings.append("<div>\n")
            itemStrings.append(divTemplate.format('title', i, entry.title.encode('utf8')))
            itemStrings.append(divTemplate.format('description', i, entry.description))
            itemStrings.append(divTemplate.format('link', i, entry.link))
            itemStrings.append("</div>\n")
            i += 1
        return ''.join(itemStrings)

    def edit(self, path, newValue):
        feed = self.feedLoader.retrieve()
        wrapper = PropertyAccessor(feed)
        wrapper.setValue(path, newValue)
        self.feedLoader.save(feed.toXml())

class FeedLoader:
    def __init__(self, url):
        self.url = url

    def retrieve(self):
        return feedparser.parse(self.url)

    def save(self, feedString):
        print feedString



loader = FeedLoader("http://news.ycombinator.com/rss")
editor = RssEditor(loader)

print editor.renderFeed()
editor.edit('entries[1].title', 'asdf')

