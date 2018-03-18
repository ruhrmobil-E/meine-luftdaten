# encoding: utf-8

"""
Copyright (c) 2017, Ernesto Ruge
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import os
from .common.constants import INSTANCE_FOLDER_PATH


class DefaultConfig(object):
    PROJECT_NAME = ""
    PROJECT_URL = ''
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_VERSION = '0.1.0'
    LOG_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir, 'logs'))

    DEBUG = False
    TESTING = False

    ADMINS = ['']
    MAILS_FROM = ''

    SECRET_KEY = ''
    SECURITY_PASSWORD_SALT = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = ''

    MAIL_SERVER = ''
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

    EXTERNAL_DATABASE_HOST = ''
    EXTERNAL_DATABASE_USER = ''
    EXTERNAL_DATABASE_PASSWORD = ''
    EXTERNAL_DATABASE_DATABASE = ''

    MAPBOX_TOKEN = ''
    PIWIK_HOST = ''
    PIWIK_ID = ''


class LocalConfig(DefaultConfig):
    pass


class StagingConfig(DefaultConfig):
    pass


class ProdConfig(DefaultConfig):
    pass


def get_config(MODE):
    SWITCH = {
        'LOCAL': LocalConfig,
        'STAGING': StagingConfig,
        'PRODUCTION': ProdConfig
    }
    return SWITCH[MODE]
