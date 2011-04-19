<div class="editable-block">
    <h1 class="display feedTitle">{{title}}</h1>
    <form class="form" action="/editFeedValue/{{feedKey}}">
        <input type="text" class="text" size="50" name="feedTitle"/>
        <input type="submit" class="save" value=" Save " />
        <input type="submit" class="cancel" value=" Cancel " />
    </form>
</div>
%for item in itemList:
<div class="editable-block">
    <h2 class="display title">{{item['title']['value']}}</h2>
    <form class="form" action="/editFeedValue/{{feedKey}}">
        <input type="text" class="text" size="50" name="{{item['title']['path']}}"/>
        <input type="submit" class="save" value=" Save " />
        <input type="submit" class="cancel" value=" Cancel " />
    </form>
</div>
<div class="indent editable-block">
    <div class="display description">{{!item['description']['value']}}</div>
    <form class="form" action="/editFeedValue/{{feedKey}}">
        <input type="text" class="text" size="50" name="{{item['description']['path']}}"/>
        <input type="submit" class="save" value=" Save " />
        <input type="submit" class="cancel" value=" Cancel " />
    </form>
</div>
<div class="indent editable-block">
    <div class="display description">{{!item['link']['value']}}</div>
    <form class="form" action="/editFeedValue/{{feedKey}}">
        <input type="text" class="text" size="50" name="{{item['link']['path']}}"/>
        <input type="submit" class="save" value=" Save " />
        <input type="submit" class="cancel" value=" Cancel " />
    </form>
</div>
<br/>
%end

