#!/usr/bin/env python

import docker
import pierone.api
import sys
import tokens

pierone_url            = "https://pierone.stups.zalan.do"
credentials_dir        = "/meta/credentials"
oauth_access_token_url = "https://token.services.auth.zalando.com/oauth2/access_token?realm=/services"

tokens.configure(url=oauth_access_token_url, dir=credentials_dir)
tokens.manage("pierone", ["uid"])

pierone.api.docker_login_with_token(pierone_url, tokens.get("pierone"))

client = docker.from_env(version='1.24')
client.images.pull("pierone.stups.zalan.do/{}/{}:{}".format(*sys.argv[1:4]))
