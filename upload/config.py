# -*- coding: utf-8 -*-

# 配置文件模块

file_path = "/data/cdn/filetmp"

# 定义参数
ignored = [
    '.bzr',
    '$RECYCLE.BIN',
    '.DAV',
    '.DS_Store',
    '.git',
    '.hg',
    '.htaccess',
    '.htpasswd',
    '.Spotlight-V100',
    '.svn',
    '__MACOSX',
    'ehthumbs.db',
    'robots.txt',
    'Thumbs.db',
    'thumbs.tps'
]
datatypes = {
    'audio': 'm4a,mp3,oga,ogg,webma,wav',
    'archive': '7z,zip,rar,gz,tar',
    'image': 'gif,ico,jpe,jpeg,jpg,png,svg,webp',
    'pdf': 'pdf',
    'quicktime': '3g2,3gp,3gp2,3gpp,mov,qt',
    'source': 'atom,bat,bash,c,cmd,coffee,css,hml,js,json,java,less,markdown,md,php,pl,py,rb,rss,sass,scpt,swift,scss,sh,xml,yml,plist',
    'text': 'txt',
    'video': 'mp4,m4v,ogv,webm',
    'website': 'htm,html,mhtm,mhtml,xhtm,xhtml'
}
icontypes = {
    'fa-music': 'm4a,mp3,oga,ogg,webma,wav',
    'fa-archive': '7z,zip,rar,gz,tar',
    'fa-picture-o': 'gif,ico,jpe,jpeg,jpg,png,svg,webp',
    'fa-file-text': 'pdf',
    'fa-film': '3g2,3gp,3gp2,3gpp,mov,qt',
    'fa-code': 'atom,plist,bat,bash,c,cmd,coffee,css,hml,js,json,java,less,markdown,md,php,pl,py,rb,rss,sass,scpt,swift,scss,sh,xml,yml',
    'fa-file-text-o': 'txt',
    'fa-film': 'mp4,m4v,ogv,webm',
    'fa-globe': 'htm,html,mhtm,mhtml,xhtm,xhtml'
}