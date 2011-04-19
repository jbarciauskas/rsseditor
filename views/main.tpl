<html>
<head>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js">
    </script>
    <script type="text/javascript" src="/static/js/jquery.inline-edit.js">
    </script>
    <script>
    $(document).ready(function() {
        $("#loadFeedForm").submit(function(event) {
            event.preventDefault();
            var jqxhr = $
                            .post("loadFeed", $("#loadFeedForm").serialize())
                            .success(function(data) {
                                renderResponse(data);
                            });
        });
    });
    function renderResponse(response) {
        $( "#currentFeed" ).html(response);
        $('.editable-block').inlineEdit({
            success: renderResponse,
            hover: 'hover'});
    }
    </script>
    <style type="text/css">
        .indent {
            margin-left:1em;
        }
        .editable-block .form {
            display: none;
        }

        .editable-block .hover {
            background-color: #FFFFA5;
            cursor: pointer;
        }
    </style>
</head>
<body>
<form id="loadFeedForm">
<input type="text" size="50" name="feedUrl" value="http://news.ycombinator.com/rss"/>
<input type="submit" value="Load feed"/>
</form>
<div id="currentFeed"></div>
</body>
</html>
