# -*- coding: utf-8 -*-

'''
定义Jinja过滤器
Jinja docs : http://dormousehole.readthedocs.io/en/latest/templating.html
'''

from upload import app
import humanize
import upload.config
from datetime import datetime


@app.template_filter('size_fmt')
# 文件大小human view
def size_fmt(size):
    return humanize.naturalsize(size)


@app.template_filter('time_fmt')
# 时间戳to本地时间
def time_desc(timestamp):
    mdate = datetime.fromtimestamp(timestamp)
    str = mdate.strftime('%Y-%m-%d %H:%M:%S')
    return str


@app.template_filter('data_fmt')
# 根据文件名后缀，返回文件类型。文件类型在config中定义
def data_fmt(filename):
    t = 'unknown'
    # items()方法以列表返回可遍历的(键, 值) 元组数组
    for type, exts in upload.config.datatypes.items():
        # split处理后返回列表，[-1]获取最后一个元素
        if filename.split('.')[-1] in exts:
            t = type
    return t


@app.template_filter('icon_fmt')
# 根据文件名后缀，返回icon类型。icon类型在config中定义
def icon_fmt(filename):
    i = 'fa-file-o'
    for icon, exts in upload.config.icontypes.items():
        if filename.split('.')[-1] in exts:
            i = icon
    return i


@app.template_filter('humanize')
# 时间戳to UTC时间
def time_humanize(timestamp):
    mdate = datetime.utcfromtimestamp(timestamp)
    return humanize.naturaltime(mdate)
