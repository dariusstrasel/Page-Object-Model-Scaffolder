#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta


class BaseAction:
    """
    Represents the contract of a typical Action class.
    """

    __metaclass__ = ABCMeta

    def __init__(self, target_element, compatible_elements, csharp_variable_name):
        self._target_element = target_element
        self._compatible_elements = compatible_elements
        self._csharp_variable_name = csharp_variable_name

    @property
    def csharp_variable_name(self):
        return self._csharp_variable_name

    @csharp_variable_name.setter
    def csharp_variable_name(self, csharp_variable_name):
        self._csharp_variable_name = csharp_variable_name

    @property
    def target_element(self):
        return self._target_element

    @target_element.setter
    def target_element(self, target_element):
        self._target_element = target_element

    @property
    def compatible_elements(self):
        return self._compatible_elements

    @compatible_elements.setter
    def compatible_elements(self, elements):
        self._compatible_elements = elements
