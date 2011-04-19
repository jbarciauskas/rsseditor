from bottle import Bottle, route, run, view, get, post, request, static_file, template, debug
from rsseditor import RssEditor
from rsseditor import FeedLoader
import os
from pprint import pprint

app = Bottle()
debug(True)

@app.route('/static/js/:filename')
def send_static(filename):
    return static_file(filename, root='./static/js')

@app.route('/')
@view('main.tpl')
def main():
    return {}

@app.post('/loadFeed')
def loadFeed():
    feedUrl = request.forms.get('feedUrl')
    feedLoader = FeedLoader()
    index = feedLoader.add(feedUrl)
    editor = RssEditor(feedLoader)
    feedItems = editor.renderFeed()
    return template('feed', itemList=feedItems, feedKey=index)

@app.post('/editFeedValue/:feedKey')
def editFeedValue(feedKey):
    path = request.forms.get('path')
    value = request.forms.get('value')
    feedLoader = FeedLoader(int(feedKey))
    editor = RssEditor(feedLoader)
    for key in request.forms:
        editor.edit(key, request.forms[key])
    return "Success"

run(app, host='localhost', port=8080)
