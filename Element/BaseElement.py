#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta


class BaseElement:
    """
    Represents the contract of a typical Element class.
    """

    __metaclass__ = ABCMeta

    def __init__(self, element_name, attributes):
        print("BaseElement created.")
        self._element_name = element_name
        self._attributes = attributes

    @property
    def element_name(self):
        return self._element_name

    @element_name.setter
    def element_name(self, new_name):
        self._element_name = new_name

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, attribute_list):
        if type(attribute_list) == 'list':
            print("Its a list.")

        self._attributes = attribute_list

