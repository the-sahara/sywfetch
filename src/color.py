color = {
    "black"         : "\033[30m",
    "blue"          : "\033[34m",
    "bold"          : "\033[1m",
    "bold_res"      : "\033[22m",
    "cyan"          : "\033[36m",
    "green"         : "\033[32m",
    "italics"       : "\033[3m",
    "italics_res"   : "\033[23m",
    "purple"        : "\033[35m",
    "red"           : "\033[31m",
    "res"           : "\033[0m",
    "underline"     : "\033[4m",
    "underline_res" : "\033[24m",
    "white"         : "\033[37m",
    "yellow"        : "\033[33m"
}

def fmt(text: str, _color: str | None = None, bold: bool = False, underline: bool = False, italics: bool = False) -> str:
    _str = ""

    if bold:
        _str += color['bold']
    if underline:
        _str += color['underline']
    if italics:
        _str += color['italics']
    
    if _color is not None:
        _str += color[_color]

    _str += text
    _str += color['res']

    return _str