# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 14:33
# @Author  : lenny
# @desc    :
# coding=utf-8

import requests
from i18n import _


class HttpUtil:

    def __init__(self, url, timeout=10, header=None, proxies=None):
        self.url = url
        self.timeout = timeout
        self.header = self.build_req_headers(header)
        self.proxies = proxies or {}

    def http_get(self, **kwargs):
        return requests.get(self.url, timeout=self.timeout, headers=self.header, proxies=self.proxies, **kwargs)

    def http_post(self, **kwargs):
        return requests.post(self.url, timeout=self.timeout, headers=self.header, proxies=self.proxies, **kwargs)

    def http_patch(self, **kwargs):
        return requests.patch(self.url, timeout=self.timeout, headers=self.header, proxies=self.proxies, **kwargs)

    def http_delete(self, **kwargs):
        return requests.delete(self.url, timeout=self.timeout, headers=self.header, proxies=self.proxies, **kwargs)

    def http_head(self, **kwargs):
        return requests.head(self.url, timeout=self.timeout, headers=self.header, proxies=self.proxies, **kwargs)

    @staticmethod
    def build_req_headers(params_headers):
        headers = {}
        available_lang = _.default_language
        if available_lang:
            headers["Accept-Language"] = available_lang
        if params_headers:
            headers.update(params_headers)
        return headers
