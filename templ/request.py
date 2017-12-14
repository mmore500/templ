# -*- coding: utf-8 -*-


"""templ.request: dict wrapper that requests user input on missing values."""

from .warn import warn

class CustomFormatStr(str):
    def __format__(self, fmt):
        if fmt and fmt[0] == 'u':
            s = self.upper()
            fmt = fmt[1:]
        elif fmt and fmt[0] == 'l':
            s = self.lower()
            fmt = fmt[1:]
        elif fmt and fmt[0] == 'c':
            s = self.title()
            fmt = fmt[1:]
        else:
            s = str(self)

        return s.__format__(fmt)


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

        # try to convert from str to numeric...
        try:
            # if decimal point included, try to float
            if '.' in res:
                res = float(res)
            # otherwise, try to int
            else:
                res = int(res)
        # if string is not numeric, conversion fails and no change made to res
        except ValueError:
            # cast to type CustomFormatStr so that custom formatting
            # can be applied to string components in the templates
            res = CustomFormatStr(res)


        # store answer for future use and return answer
        self[key] = res
        return self[key]
