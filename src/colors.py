from dataclasses import dataclass
import color_mode_conversion as cmc


altered_value_saturation = lambda x, s, v: (x[0], s, v)
hsv2hex = lambda h, s, v: cmc.rgb2hex(cmc.hsv2rgb((h, s, v)))

def get_shade(color, s, v):
    x = cmc.hex2rgb(color)
    x = cmc.rgb2hsv(x)
    x = altered_value_saturation(x, s, v)
    x = cmc.hsv2rgb(x)
    x = cmc.rgb2hex(x)
    
    return x


@dataclass(frozen=True, init=False)
class BaseColors:
    # Background
    bg0: str = hsv2hex(225, 20, 0)
    bg1: str = hsv2hex(225, 20, 5)
    bg2: str = get_shade(bg1, 20, 10)
    
    # Foreground
    fg0: str = hsv2hex(225, 5, 90)
    fg1: str = get_shade(fg0, 10, 60)
    fg2: str = get_shade(fg0, 30, 30)
    
    # Primary Accent
    pa0: str = hsv2hex(165, 40, 95)
    pa1: str = get_shade(pa0, 80, 40)
    pa2: str = get_shade(pa0, 80, 20)
    
    # Secondary Accent
    sa0: str = hsv2hex(210, 40, 100)
    sa1: str = get_shade(sa0, 80, 40)
    sa2: str = get_shade(sa0, 80, 20)
    
    # Warning Accent
    wa0: str = hsv2hex(55, 45, 100)
    wa1: str = get_shade(wa0, 80, 35)
    wa2: str = get_shade(wa0, 80, 15)
    
    # Debug Accent
    da0: str = hsv2hex(240, 40, 100)
    da1: str = get_shade(da0, 60, 40)
    da2: str = get_shade(da0, 60, 20)
    
    # Error Accent
    ea0: str = hsv2hex(0, 55, 100)
    ea1: str = get_shade(ea0, 80, 35)
    ea2: str = get_shade(ea0, 80, 15)
    
    # Terminal
    ansiBlack: str = bg0                        #   Material - Black
    ansiBrightBlack: str = "#757575"            #   Material - Gray 600
    ansiRed: str = "#E81123"                    #   Fluent - Red
    ansiBrightRed: str = "#FF5252"              #   Material - Red A200
    ansiGreen: str = "#00C853"                  #   Material - Green A700
    ansiBrightGreen: str = "#69F0AE"            #   Material - Green A200
    ansiYellow: str = "#FFD600"                 #   Material - Yellow A700
    ansiBrightYellow: str = "#FFFF00"           #   Material - Yellow A200
    ansiBlue: str = "#0091EA"                   #   Material - Light Blue A700
    ansiBrightBlue: str = "#40C4FF"             #   Material - Light Blue A200
    ansiMagenta: str = "#651FFF"                #   Material - Deep Purple A400
    ansiBrightMagenta: str = "#B388FF"          #   Material - Deep Purple A100
    ansiCyan: str = "#00E5FF"                   #   Material - Cyan A400
    ansiBrightCyan: str = "#84FFFF"             #   Material - Cyan A100
    ansiWhite: str = "#CFD8DC"                  #   Material - Blue Gray 100
    ansiBrightWhite: str = "#FFFFFF"            #   Material - White
    
    # Debug
    red: str = "#FF0000"


@dataclass(frozen=True, init=False)
class DraculaTokenColors:
    # https://github.com/dracula/visual-studio-code
    white: str = "#ECEFF1"                      #   Material - Blue Gray 50
    gray: str = "#6272A4"                       #   Dracula - Gray
    cyan: str = "#8BE9FD"                       #   Dracula - Cyan
    green: str = "#69F0AE"                      #   Material - Green A200
    orange: str = "#FFB74D"                     #   Material - Orange 300
    pink: str = "#FF80AB"                       #   Material - Pink A100
    purple: str = "#B388FF"                     #   Material - Purple A100
    red: str = "#FF5555"                        #   Dracula - Red
    yellow: str = "#FFF59D"                     #   Material - Yellow 200
    
    
@dataclass(frozen=True, init=False)
class MaterialTokenColors:
    white: str = "#ECEFF1"                      #   Material - Blue Gray 50
    gray: str = "#757575"                       #   Material - Gray 600
    red: str = "#F07178"
    orange: str = "#F78C6C"
    yellow: str = "#FFCB6B"
    green: str = "#C3E88D"
    cyan: str = "#89DDFF"
    blue: str = "#82AAFF"
    paleblue: str = "#B2CCD6"
    purple: str = "#C792EA"
    brown: str = "#916B53" # x
    pink: str = "#FF9CAC"
    violet: str = "#BB80B3"
    

@dataclass(frozen=True, init=False)
class MonokaiTokenColors:
    # https://monokai.pro/
    white: str = "#ECEFF1"                      #   Material - Blue Gray 50
    gray: str = "#908E8F"                       #   Monokai - Gray
    lightGray: str = "#CCCACA"
    blue: str = "#78DCE8"                       #   Monokai - Blue
    green: str = "#A9DC76"                      #   Monokai - Green
    orange: str = "#FC9867"                     #   Monokai - Orange
    pink: str = "#FF6188"                       #   Monokai - Pink
    purple: str = "#AB9DF2"                     #   Monokai - Purple
    red: str = "#FF5555"                        #   Dracula - Red
    yellow: str = "#FFD866"                     #   Monokai - Yellow
    

@dataclass(frozen=True, init=False)
class FleetTokenColors:
    white: str = "#ECEFF1"                      #   Material - Blue Gray 50
    gray: str = "#767676"                       #   Fleet - Gray 80
    lightGray: str = "#A0A0A0"                  #   Fleet - Gray 100
    blue: str = "#87C3FF"                       #   Fleet - Blue
    cyan: str = "#82D2CE"                       #   Fleet - Cyan
    green: str = "#70CCA0"
    lime: str = "#A8CC7C"                       #   Fleet - Lime
    orange: str = "#E09B70"                     #   Fleet - Orange
    pink: str = "#E394DC"                       #   Fleet - Pink
    purple: str = "#AF9CFF"                     #   Fleet - Violet
    red: str = "#FF5555"
    coral: str = "#CC7C8A"                      #   Fleet - Coral
    yellow: str = "#E6D58A"


@dataclass(frozen=True, init=False)
class VSCodeDefaultTokenColors:
    # https://github.com/microsoft/vscode/tree/main/extensions/theme-defaults
    white: str = "#C8C8C8"                      #   VSC Default
    gray: str = "#808080"                       #   VSC Default - Unused
    lightGray: str = "#D4D4D4"                  #   VSC Default - Unused
    green: str = "#6A9955"                      #   VSC Default - Unused
    lightGreen: str = "#B5CEA8"                 #   VSC Default
    darkBlue: str = "#000080"                   #   VSC Default - Unused
    blue: str = "#6796E6"                       #   VSC Default
    lightBlue: str = "#9CDCFE"                  #   VSC Default
    cyan: str = "#4FC1FF"                       #   VSC Default - Unused
    lightCyan: str = "#569CD6"                  #   VSC Default - Unused
    red: str = "#f44747"                        #   VSC Default
    lightRed: str = "#D16969"                   #   VSC Default - Unused
    yellow: str = "#D7BA7D"                     #   VSC Default
    lightYellow: str = "#DCDCAA"                #   VSC Default
    purple: str = "#646695"                     #   VSC Default - Unused
    teal: str = "#4EC9B0"                       #   VSC Default
    magenta: str = "#C586C0"                    #   VSC Default
    brown: str = "#CE9178"                      #   VSC Default
    


@dataclass(frozen=True, init=False)
class StyxTokenColors:
    white: str = hsv2hex(225, 5, 100)
    gray: str = hsv2hex(225, 40, 60)            #   Dracula - Gray
    
    red: str = hsv2hex(0, 65, 95)
    amber: str = hsv2hex(35, 70, 100)
    yellow: str = hsv2hex(45, 35, 100)
    lime: str = hsv2hex(100, 30, 90)
    teal: str = hsv2hex(155, 40, 90)
    green: str = hsv2hex(160, 70, 90)
    cyan: str = hsv2hex(180, 40, 95)
    blue: str = hsv2hex(195, 65, 100)
    periwinkle: str = hsv2hex(240, 25, 100)
    purple: str = hsv2hex(260, 50, 100)
    pink: str = hsv2hex(330, 30, 100)
    coral: str = hsv2hex(345, 50, 90)
    
    
@dataclass(frozen=True, init=False)
class DebugTokenColors:
    red: str = "#FF5555"
