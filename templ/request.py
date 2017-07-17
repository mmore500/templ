# -*- coding: utf-8 -*-


"""templ.request: dict wrapper that requests user input on missing values."""

from .warn import warn

class Request(dict):

    def __missing__(self, key):
        # prompt for user input
        warn(key + " '> '")

        # get user input, catching end of file error
        try:
            res = input()
        except EOFError:
            warn("\n")
            res = 'null'

        # store answer for future use and return answer
        self[key] = res
        return self[key]
