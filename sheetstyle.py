comments_css = \
    '<!DOCTYPE html>' \
    '<html lang="en">' \
    '<head>' \
    '<style>' \
    '* {' \
    '    box-sizing: border-box;' \
    '}' \
    'body {' \
    '    margin: 0;' \
    '}' \
    '.column {' \
    '    float: left;' \
    '    padding: 10px;' \
    '}' \
    '.column.side {' \
    '    width: 70px;' \
    '}' \
    '.column.middle {' \
    '    width: 90%;' \
    '    border-style: solid;' \
    '    border-width: 0 0 1px 0;' \
    '    border-color: rgb(228, 228, 228);' \
    '}' \
    'h4{' \
    '    background: none;' \
    '    font-size: 13px;' \
    '    height: auto;' \
    '    margin: 0;' \
    '    padding: 0;' \
    '    color: #494949;' \
    '    margin-bottom: 5px;' \
    '}' \
    '.comment{' \
    '    overflow: hidden;' \
    '    line-height: 1.5;' \
    '    color: #494949;' \
    '    *zoom: 1;' \
    '    word-wrap: break-word;' \
    '}' \
    '.name{' \
    '    color:#37a;' \
    '    font-size:16px;' \
    '}' \
    '.comment-time {' \
    '    color: #aaa;' \
    '    font-size:13px;' \
    '}' \
    '.zan{' \
    '    color:#37a;' \
    '    font-size:15px;' \
    '    float:right;' \
    '}' \
    '.row:after {' \
    '    content: "";' \
    '    display: table;' \
    '    clear: both;' \
    '}' \
    '</style>' \
    '</head>' \
    '<body>' \

comments_html = \
    '<div class="row">' \
    '    <div class="column side">' \
    '        <img src="{}">' \
    '    </div>' \
    '    <div class="column middle">' \
    '        <span class="name">{}</span>' \
    '        <span class="comment-time">{}</span>' \
    '        <span class="zan">{}赞</span>' \
    '        <p class="comment">' \
    '            {}' \
    '        </p>' \
    '    </div>' \
    '</div>' \

load_msg_style = 'QPushButton {' \
                                '    border-radius: 3px;' \
                                '    color: white;'\
                                '    padding: 1px 5px;'\
                                '    text-align: left;'\
                                '    text-decoration: underline;'\
                                '    font-size: 15px;'\
                                '    margin: 1px 1px;'\
                                '    color: black;'\
                                '    border: 0px solid #37a;'\
                                '}'\
                                'QPushButton:hover {'\
                                '    background-color: #37a;'\
                                '    color: white;'\
                                '    cursor: pointer;'\
                                '}'\
                                'QPushButton:pressed {'\
                                '   background-color: #06AD56;'\
                                '}'

book_type_style = 'QPushButton {' \
                                        '    border-radius: 3px;'\
                                        '    color: white;'\
                                        '    padding: 5px 5px;'\
                                        '    text-align: center;'\
                                        '    text-decoration: none;'\
                                        '    font-size: 15px;'\
                                        '    margin: 1px 1px;'\
                                        '    background-color: white;'\
                                        '    color: black;'\
                                        '    border: 1px solid #37a;'	\
                                        '}'\
                                        'QPushButton:hover {'\
                                        '    background-color: #37a;'\
                                        '    color: white;'\
                                        '}'\
                                        'QPushButton:pressed {'\
                                        '   background-color: #06AD56;'\
                                        '}'
