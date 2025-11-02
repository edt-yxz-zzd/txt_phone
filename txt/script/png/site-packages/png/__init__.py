try:
    exec("from .png import *", globals(), locals())
    #  Following methods are not parts of API and imports only for unittest
    exec("from .png import _main", globals(), locals())
    exec("from .png import strtobytes", globals(), locals())
    exec("from .png import array", globals(), locals())
except SyntaxError:
    # On Python < 2.5 relative import cause syntax error
    from png import *
    #  Following methods are not parts of API and imports only for unittest
    from png import _main
    from png import strtobytes
    from png import array
