# -*- coding: utf-8 -*-

# 文件上传模块

import os
import stat
import json
import upload.config
from upload.play import get_range, partial_response
from flask import make_response, request, render_template, send_file
from flask.views import MethodView
from werkzeug import secure_filename

root = os.path.abspath(upload.config.file_path)


# 判断是文件还是目录
def get_type(mode):
    if stat.S_ISDIR(mode) or stat.S_ISLNK(mode):
        type = 'dir'
    else:
        type = 'file'
    return type


# PathView是flask.views.MethodView的子类
# 实现基于调度的方法，每个HTTP方法映射到同名函数，比如get、post
class PathView(MethodView):
    # 参数p表示访问路径
    def get(self, p=''):
        path = os.path.join(root, p)
        # print(path)
        # 路径是目录的处理
        if os.path.isdir(path):
            contents = []
            total = {'size': 0, 'dir': 0, 'file': 0}
            for filename in os.listdir(path):
                if filename in upload.config.ignored:
                    continue
                # os.path.join 多路径组合返回
                # os.stat 显示文件信息，包括有st_mtime(最后修改时间)、st_mode(inode保护模式)
                filepath = os.path.join(path, filename)
                stat_res = os.stat(filepath)
                # 判断是dir or file
                ft = get_type(stat_res.st_mode)
                sz = stat_res.st_size
                # 定义info元组
                info = {}
                info['name'] = filename  # 文件名
                info['mtime'] = stat_res.st_mtime  # 最后修改时间
                info['type'] = ft
                total[ft] += 1
                info['size'] = sz
                total['size'] += sz
                contents.append(info)
            # print(contents)
            page = render_template('index.html', path=p,
                                   contents=contents, total=total)
            res = make_response(page, 200)
        # 路径是文件的处理
        elif os.path.isfile(path):
            # Range header主要用在音视频播放中
            if 'Range' in request.headers:
                start, end = get_range(request)
                res = partial_response(path, start, end)
            else:
                res = send_file(path)
                res.headers.add('Content-Disposition', 'attachment')
        else:
            res = make_response('Not found', 404)
        return res

    def post(self, p=''):
        path = os.path.join(root, p)
        typedata = request.values["type"]
        value = request.values["value"]
        # 定义info元组
        info = {}
        # 只有目录才能上传文件
        if os.path.isdir(path):
            if typedata == "mkdir":
                mkdir_path = path + value
                os.makedirs(mkdir_path)
            else:
                files = request.files.getlist('files[]')
                for file in files:
                    try:
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(path, filename))
                    except Exception as e:
                        info['status'] = 'error'
                        info['msg'] = str(e)
                    else:
                        info['status'] = 'success'
                        info['msg'] = 'File Saved'
        else:
            info['status'] = 'error'
            info['msg'] = 'Invalid Operation'
        res = make_response(json.JSONEncoder().encode(info), 200)
        # res.headers.add('Content-type', 'application/json')
        res.headers['Content-type'] = 'application/json'
        return res
