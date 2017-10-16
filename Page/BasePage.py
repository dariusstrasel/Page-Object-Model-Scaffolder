#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta


class BasePage:
    """
    Represents the contract of a typical Page class.
    """

    __metaclass__ = ABCMeta

    def __init__(self, url, elements=None, child_pages=None, source_html=None):
        self._url = url
        self._elements = elements
        self._child_pages = child_pages
        self._source_html = source_html

    @property
    def child_pages(self):
        return self._child_pages

    @child_pages.setter
    def child_pages(self, new_child_pages):
        self._child_pages = new_child_pages

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self, elements):
        if type(elements) == 'list':
            print("Its a list.")

        self._elements = elements

    @property
    def source_html(self):
        return self._source_html
    
    @source_html.setter
    def source_html(self, new_html):
        self._source_html = new_html
