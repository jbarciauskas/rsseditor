%for item in itemList:
%    for key in item:
%        thing = item[key]
<div class='editable-block'>
    <div class='display'>{{thing['value']}}</div>
    <form class='form' action="/editFeedValue/{{feedKey}}">
        <input type='text' class='text' size="50" name="{{thing['path']}}"/>
        <input type='submit' class='save' value=' Save ' />
        <input type='submit' class='cancel' value=' Cancel ' />
    </form>
</div>
%end
%end

