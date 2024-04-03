#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def get_integer(self):
        return self._page_count
    def set_integer(self, value):
        if type(value) is int:
            self._page_count = value
        else:
            print("page_count must be an integer")
    page_count = property(get_integer, set_integer)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

