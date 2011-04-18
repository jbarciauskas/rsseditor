import unittest

from rsseditor import RssEditor
from rsseditor import FeedLoader

class RssEditorTest(unittest.TestCase):
    def setUp(self):
        self.feedLoader = FeedLoader('http://news.ycombinator.com/rss')
        self.classUnderTest = RssEditor(self.feedLoader)

    def testEditTitle(self):
        self.assertEqual(self.feedLoader.retrieve().find("asdf"), -1)
        self.classUnderTest.edit("[1].title.string", "asdf")
        self.assertNotEqual(self.feedLoader.retrieve().find("asdf"), -1)
