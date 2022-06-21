#!/usr/bin/python3
import sys


def safe_function(fct, *args):
        try:
                    res = fct(*args)
                        except Exception as exp:
                                    print("Exception: {}".format(exp), file=sys.stderr)
                                            res = None
                                                return res
                                            © 2022 GitHub, Inc.
                                            Terms
                                            Privacy
                                            Sec
