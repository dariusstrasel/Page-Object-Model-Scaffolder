from .BaseAction import BaseAction
from ..Element.Elements import *


class Click(BaseAction):
    """
    A common 'click' interaction.
    """

    COMPATIBLE_ELEMENTS = [A, Input]

    def __init__(self, target_element, COMPATIBLE_ELEMENTS):
        print("Creating {self.__name__} tag.")
        csharp_variable_name = self.create_csharp_variable_name()
        super().__init__(target_element, COMPATIBLE_ELEMENTS, csharp_variable_name)


    def create_csharp_variable_name(self):
        return "click_{self.target_element.name}"
