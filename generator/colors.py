from dataclasses import dataclass


@dataclass(frozen=True, init=False)
class BaseColors:
    #   Background
    bg0: str = "#000000"                #   Material - Black
    bg1: str = "#101010"
    bg2: str = "#212121"                #   Material - Gray 900
    
    #   Foreground
    fg0: str = "#ECEFF1"                #   Material - Blue Gray 50
    fg1: str = "#B0BEC5"                #   Material - Blue Gray 200
    fg2: str = "#455A64"                #   Material - Blue Gray 700
    
    #   Accent
    accent0: str = "#1DE9B6"            #   Material - Teal A400
    accent1: str = "#64B5F6"            #   Material - Blue 300
    
    #   Terminal
    ansiBlack: str = bg0                #   Material - Black
    ansiBrightBlack: str = "#757575"    #   Material - Gray 600
    ansiRed: str = "#E81123"            #   Fluent - Red
    ansiBrightRed: str = "#FF5252"      #   Material - Red A200
    ansiGreen: str = "#00C853"          #   Material - Green A700
    ansiBrightGreen: str = "#69F0AE"    #   Material - Green A200
    ansiYellow: str = "#FFD600"         #   Material - Yellow A700
    ansiBrightYellow: str = "#FFFF00"   #   Material - Yellow A200
    ansiBlue: str = "#0091EA"           #   Material - Light Blue A700
    ansiBrightBlue: str = "#40C4FF"     #   Material - Light Blue A200
    ansiMagenta: str = "#651FFF"        #   Material - Deep Purple A400
    ansiBrightMagenta: str = "#B388FF"  #   Material - Deep Purple A100
    ansiCyan: str = "#00E5FF"           #   Material - Cyan A400
    ansiBrightCyan: str = "#84FFFF"     #   Material - Cyan A100
    ansiWhite: str = "#CFD8DC"          #   Material - Blue Gray 100
    ansiBrightWhite: str = "#FFFFFF"    #   Material - White
    
    #   Debug
    red: str = "#FF0000"


@dataclass(frozen=True, init=False)
class DraculaTokenColors:
    #   https://github.com/dracula/visual-studio-code
    white: str = "#ECEFF1"              #   Material - Blue Gray 50
    gray: str = "#6272A4"               #   Dracula - Gray
    cyan: str = "#8BE9FD"               #   Dracula - Cyan
    green: str = "#69F0AE"              #   Material - Green A200
    orange: str = "#FFB74D"             #   Material - Orange 300
    pink: str = "#FF80AB"               #   Material - Pink A100
    purple: str = "#B388FF"             #   Material - Purple A100
    red: str = "#FF5555"                #   Dracula - Red
    yellow: str = "#FFF59D"             #   Material - Yellow 200
    
    
@dataclass(frozen=True, init=False)
class MaterialTokenColors:
    white: str = "#ECEFF1"              #   Material - Blue Gray 50
    black: str = "#000000"
    red: str = "#f07178"
    orange: str = "#F78C6C"
    yellow: str = "#FFCB6B"
    green: str = "#C3E88D"
    cyan: str = "#89DDFF"
    blue: str = "#82AAFF"
    paleblue: str = "#B2CCD6"
    purple: str = "#C792EA"
    brown: str = "#916b53"
    pink: str = "#ff9cac"
    violet: str = "#bb80b3"
    gray: str = "#4A4A4A"
    

@dataclass(frozen=True, init=False)
class MonokaiTokenColors:
    #   https://monokai.pro/
    foreground: str = "#ECEFF1"         #   Material - Blue Gray 50
    gray: str = "#908E8F"               #   Monokai - Gray
    blue: str = "#78DCE8"               #   Monokai - Blue
    green: str = "#A9DC76"              #   Monokai - Green
    orange: str = "#FC9867"             #   Monokai - Orange
    pink: str = "#FF6188"               #   Monokai - Pink
    purple: str = "#AB9DF2"             #   Monokai - Purple
    # red: str = "#FF5555"              #   Dracula - Red
    yellow: str = "#FFD866"             #   Monokai - Yellow
    

@dataclass(frozen=True, init=False)
class FleetTokenColors:
    # foreground: str = "#D1D1D1"       #   Fleet - Gray 120
    foreground: str = "#ECEFF1"         #   Material - Blue Gray 50
    gray: str = "#898989"               #   Fleet - Gray 90
    cyan: str = "#82D2CE"               #   Fleet - Cyan
    green: str = "#50FA7B"
    lime: str = "#A8CC7C"               #   Fleet - Lime
    orange: str = "#FFB86C"
    pink: str = "#E394DC"               #   Fleet - Pink
    purple: str = "#AF9CFF"             #   Fleet - Violet
    red: str = "#FF5555"
    coral: str = "#CC7C8A"              #   Fleet - Coral
    yellow: str = "#e1971b"             #   Fleet - Yellow 60
    

@dataclass(frozen=True, init=False)
class VSCodeDefaultTokenColors:
    gray: str = "#546E7A"               #   VSC Default
    white: str = "#EEFFFF"              #   VSC Default
    red: str = "#FF5370"                #   VSC Default
    purple: str = "#C792EA"             #   VSC Default
    lightBlue: str = "#89DDFF"          #   VSC Default
    pink: str = "#f07178"               #   VSC Default
    blue: str = "#82AAFF"               #   VSC Default
    orange: str = "#F78C6C"             #   VSC Default
    lime: str = "#C3E88D"               #   VSC Default
    yellow: str = "#FFCB6B"             #   VSC Default
    lightBlueGray: str = "#B2CCD6"      #   VSC Default


@dataclass(frozen=True, init=False)
class TokenColors:
    foreground: str = "#ECEFF1"         #   Material - Blue Gray 50
    gray: str = "#6272A4"
    cyan: str = "#8BE9FD"
    green: str = "#50FA7B"
    orange: str = "#FFB86C"
    pink: str = "#FF79C6"
    purple: str = "#BD93F9"
    red: str = "#FF5555"
    yellow: str = "#F1FA8C"
