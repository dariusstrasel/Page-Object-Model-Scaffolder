#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: POM Scaffolding Tool
Description: Python powered web crawler that creates Page Object Models based on a webpage.

class Page:
- Name: the URL
- Elements: list of child elements

class Element:
- Name: {html_type}_{property key}__{property value}
- Type: HTML Element Type, i.e. <a>, <p>, <input>, etc

class AbstractElement(ABC):
- Name: {html_type}_{property key}__{property value}
- Type: HTML Element Type, i.e. <a>, <p>, <input>, etc

class Action:
- Target Element: The element it will target
- 

class BaseAction(ABC):

class BaseNode(ABC):

"""

from Element.Elements import *


def main():
    test = A.tag_name
    
    print(test)


if __name__ == '__main__':
    main()
