from prompt_toolkit.styles import Style

target = ""

"""@______________________________________________________________________________________________@"""
                                        #Themes and colors


class red_blue:
    class color_sheme:
        red = "#ff0000"
        green = "#00ff00"
        blue = "#1a4ff0"
        light_blue = "#17e0ff"
        orange = "#ff7e05"
        yellow = "#ffff05"
        purple = ""
        white = "#ffffff"
        black = "#00000"
        # Over
        banner = blue
        text = white
        error = red
        warn = orange
        info = light_blue
        notice = yellow
    style = Style.from_dict({
        # User input (default text).
        '':          color_sheme.text,

        # Prompt.
        'username': color_sheme.red,
        'symbol':   '#eeeeee',
        'host':     '#1a4ff0',
        'symbol2': color_sheme.white,
        'target': color_sheme.white,
    })

class red_green:
    class color_sheme:
        red = "#ff0000"
        green = "#00ff00"
        blue = "#1a4ff0"
        light_blue = "#17e0ff"
        orange = "#ff7e05"
        yellow = "#ffff05"
        purple = ""
        white = "#ffffff"
        black = "#00000"
        # Over
        banner = green
        text = white
        error = red
        warn = orange
        info = light_blue
        notice = yellow
    style = Style.from_dict({
        # User input (default text).
        '': color_sheme.text,

        # Prompt.
        'username': color_sheme.red,
        'symbol': color_sheme.white,
        'host': color_sheme.green,
        'symbol2': color_sheme.white,
        'target': color_sheme.white,
    })

class green:
    class color_sheme:
        red = "#ff0000"
        green = "#00ff00"
        blue = "#1a4ff0"
        light_blue = "#17e0ff"
        orange = "#ff7e05"
        yellow = "#ffff05"
        light_grey = "#eaeaea"
        white = "#ffffff"
        black = "#00000"
        # Over
        banner = green
        text = light_grey
        error = red
        warn = orange
        info = light_blue
        notice = yellow
    style = Style.from_dict({
        # User input (default text).
        '': color_sheme.text,

        # Prompt.
        'username': color_sheme.green,
        'symbol': color_sheme.white,
        'symbol2': color_sheme.white,
        'target': color_sheme.white,
        'host': color_sheme.green,

    })

class red:
    class color_sheme:
        red = "#ff0000"
        green = "#00ff00"
        blue = "#1a4ff0"
        light_blue = "#17e0ff"
        orange = "#ff7e05"
        yellow = "#ffff05"
        purple = ""
        white = "#ffffff"
        black = "#00000"
        # Over
        banner = red
        text = white
        error = red
        warn = orange
        info = light_blue
        notice = yellow
    style = Style.from_dict({
        # User input (default text).
        '': color_sheme.text,

        # Prompt.
        'username': color_sheme.red,
        'symbol': color_sheme.white,
        'host': color_sheme.red,
        'symbol2': color_sheme.white,
        'target': color_sheme.white,
    })


class blue:
    class color_sheme:
        red = "#ff0000"
        green = "#00ff00"
        blue = "#1a4ff0"
        light_blue = "#17e0ff"
        orange = "#ff7e05"
        yellow = "#ffff05"
        purple = ""
        white = "#ffffff"
        black = "#00000"
        # Over
        banner = blue
        text = white
        error = red
        warn = orange
        info = light_blue
        notice = yellow
    style = Style.from_dict({
        # User input (default text).
        '': color_sheme.text,

        # Prompt.
        'username': '#34c6eb',
        'symbol': color_sheme.blue,
        'host': '#34c6eb',
        'symbol2': color_sheme.white,
        'target': color_sheme.white,
    })


class white_blue:
    class color_sheme:
        red = "#ff0000"
        green = "#00ff00"
        blue = "#1a4ff0"
        light_blue = "#17e0ff"
        orange = "#ff7e05"
        yellow = "#ffff05"
        purple = ""
        white = "#ffffff"
        black = "#00000"
        #Over
        banner = light_blue
        text = white
        error = red
        warn = orange
        info = blue
        notice = yellow
    style = Style.from_dict({
        # User input (default text).
        '': color_sheme.text,

        # Prompt.
        'username': '#34c6eb',
        'symbol': color_sheme.white,
        'host': '#34c6eb',
        'symbol2': color_sheme.white,
        'target': color_sheme.white,
    })

class blue:
    class color_sheme:
        red = "#ff0000"
        green = "#00ff00"
        blue = "#1a4ff0"
        light_blue = "#17e0ff"
        orange = "#ff7e05"
        yellow = "#ffff05"
        purple = ""
        white = "#ffffff"
        black = "#00000"
        #Over
        banner = blue
        text = white
        error = red
        warn = orange
        info = blue
        notice = yellow
    style = Style.from_dict({
        # User input (default text).
        '': color_sheme.white,

        # Prompt.
        'username': '#34c6eb',
        'symbol': color_sheme.blue,
        'host': '#34c6eb',
        'symbol2': color_sheme.white,
        'target': color_sheme.white,
    })

class Promts:
    simple = [
        ('class:username', 'Terminator'),
        ('class:symbol', '@'),
        ('class:host', 'T-70'),
        ('class:symbol', ': '),
    ]
    kali_like = [
        ('class:symbol', '┌──['),
        ('class:username', 'Terminator'),
        ('class:symbol2', '@'),
        ('class:host', 'T-70'),
        ('class:symbol', ']'),
        ("class:target", target + "\n"),
        ('class:symbol', '└── '),
    ]


"""@______________________________________________________________________________________________@"""
                                    #Selected themes and colors
theme = red
colors = theme.color_sheme
style = theme.style
promt = Promts.kali_like

"""@______________________________________________________________________________________________@"""
                                        #Some output functions

def colored(hex_color, message):
    r, g, b = [int(hex_color[i:i + 2], 16) for i in range(1, len(hex_color), 2)]
    print("\x1b[38;2;{r};{g};{b}m{message}\x1b[0m".format(**vars()))

def info(massage, colors = colors):
    color = colors.info
    message = " [+] " + massage
    colored(color, message)

def warn(massage, colors = colors):
    color = colors.warn
    message = " [!] " + massage
    colored(color, message)

def notice(massage, colors = colors):
    color = colors.notice
    message = " " + massage
    colored(color, message)

def error(massage, notice_message, colors = colors):
    color = colors.error
    message = " ERR! " + massage
    colored(color, message)
    notice(notice_message)
