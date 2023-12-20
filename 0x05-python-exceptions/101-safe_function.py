#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        v = fct(*args)
        return v
    except Exception as z:
        print("Exception: {}".format(z), file=sys.stderr)
        return None
