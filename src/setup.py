# -*- encoding:utf-8 -*-

#!/usr/bin/env python

from distutils.core import setup

setup(
	name = 'tongwen-python',
	version = '1.0.0',
	description = 'New TongWenTang Python module',
	author = 'swatch',
	author_email = 'swatch.code@gmail.com',
	url = 'http://code.google.com/p/tongwen-python/',
	license = 'GPLv2',
	scripts = ['bin/tongwen_conv.py'],
	packages = ['pyTongwen'],
)