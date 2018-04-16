# -*- coding: utf-8 -*-

# 视图函数

from upload import app
from upload.fileupload import PathView
from flask import request
from upload.refresh import cdn_refresh

path_view = PathView.as_view('path_view')
app.add_url_rule('/', view_func=path_view)
# 使用path类型获取用户访问的URI
app.add_url_rule('/<path:p>', view_func=path_view)


@app.route('/refresh', methods=['POST'])
def refresh():
    cdnurl = request.values["cdnurl"]
    res = cdn_refresh(cdnurl)
    res = str(res)
    print(res)
    return res
