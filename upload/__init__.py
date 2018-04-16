# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

import upload.fileupload
import upload.config
import upload.jinja
import upload.play
import upload.view
