import urllib2
from BeautifulSoup import BeautifulStoneSoup
from propertyaccessor.PropertyAccessor import PropertyAccessor

class RssEditor:
    def __init__(self, feedLoader):
        self.feedLoader = feedLoader

    def renderFeed(self):
        soup = self.feedLoader.retrieve()
        entries = soup('item')
        itemStrings = []
        divTemplate = '<div class="{0}" path="[{1}].{0}.string">{2}</div>\n'
        i = 0
        for entry in entries:
            itemStrings.append("<div>\n")
            itemStrings.append(divTemplate.format('title', i, entry.title.string.encode('utf8')))
            itemStrings.append(divTemplate.format('description', i, entry.description.string))
            itemStrings.append(divTemplate.format('link', i, entry.link.string))
            itemStrings.append("</div>\n")
            i += 1
        return ''.join(itemStrings)

    def edit(self, path, newValue):
        soup = self.feedLoader.retrieve()
        entries = soup('item')
        wrapper = PropertyAccessor(entries)
        wrapper.setValue(path, newValue)
        self.feedLoader.save(soup.prettify())

class FeedLoader:
    def __init__(self, url):
        self.url = url

    def retrieve(self):
        page = urllib2.urlopen(self.url)
        soup = BeautifulStoneSoup(page)
        return soup

    def save(self, feedString):
        print feedString



loader = FeedLoader("http://news.ycombinator.com/rss")
editor = RssEditor(loader)

print editor.renderFeed()
editor.edit('[1].title.string', 'asdf')

