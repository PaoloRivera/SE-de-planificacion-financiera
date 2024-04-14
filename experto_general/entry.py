from typing import List
from experto_general.property import Property


class Entry:

    def __init__(self, name: str):
        self.properties: List[Property] = []
        self.name = name.strip()
        self.description = ""

    def get_or_add_prop(self, name: str) -> Property:
        for prop in self.properties:
            if prop.is_equal(name):
                return prop

        prop = Property(name)
        self.properties.append(prop)
        return prop

    def is_equal(self, name: str) -> bool:
        return self.name.lower() == name.lower().strip()

    def __str__(self):
        res = f'Entry "{self.name}":'
        if len(self.description) > 0:
            res += f"\n\t{self.description}"
        for prop in self.properties:
            res += f"\n\t- {prop.name}"
        return res
