class Text():
    RED = "\033[1;31;1m"
    GREEN = '\033[1;32;1m'
    YELLOW = '\033[1;33;1m'
    UNDERLINE = '\033[4m'

    def apply(str, format):
        return(format + str + '\033[0m')
