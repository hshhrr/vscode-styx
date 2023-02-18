from dataclasses import dataclass
import color_mode_conversion as cmc


altered_value_saturation = lambda x, s, v: (x[0], s, v)

def get_shade(color, s, v):
    x = cmc.hex2rgb(color)
    x = cmc.rgb2hsv(x)
    x = altered_value_saturation(x, s, v)
    x = cmc.hsv2rgb(x)
    x = cmc.rgb2hex(x)
    
    return x


@dataclass(frozen=True, init=False)
class BaseColors:
    #   Background
    bg0: str = "#000000"                #   Material - Black
    bg1: str = "#101010"
    bg2: str = "#202020"
    
    #   Foreground
    fg0: str = "#CFD8DC"                #   Material - Blue Gray 100
    fg1: str = "#78909C"                #   Material - Blue Gray 400
    fg2: str = "#2E364D"
    
    #   Primary Accent
    pa0: str = "#64FFDA"                #   Material - Teal A200
    pa1: str = get_shade(pa0, 80, 40)
    pa2: str = get_shade(pa0, 80, 20)
    
    #   Secondary Accent
    sa0: str = "#40C4FF"                #   Material - Light Blue A200
    sa1: str = get_shade(sa0, 80, 40)
    sa2: str = get_shade(sa0, 80, 20)
    
    #   Warning Accent
    wa0: str = "#FFFF00"                #   Material - Yellow A200
    wa1: str = get_shade(wa0, 80, 40)
    wa2: str = get_shade(wa0, 80, 20)
    
    #   Debug Accent
    da0: str = "#B388FF"                #   Material - Deep Purple A100
    da1: str = get_shade(da0, 60, 30)
    da2: str = get_shade(da0, 60, 10)
    
    #   Error Accent
    ea0: str = "#FF5252"                #   Material - Red A200
    ea1: str = get_shade(ea0, 80, 40)
    ea2: str = get_shade(ea0, 80, 20)
    
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
    gray: str = "#757575"               #   Material - Gray 600
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
    #   https://monokai.pro/
    white: str = "#ECEFF1"              #   Material - Blue Gray 50
    gray: str = "#908E8F"               #   Monokai - Gray
    lightGray: str = "#CCCACA"
    blue: str = "#78DCE8"               #   Monokai - Blue
    green: str = "#A9DC76"              #   Monokai - Green
    orange: str = "#FC9867"             #   Monokai - Orange
    pink: str = "#FF6188"               #   Monokai - Pink
    purple: str = "#AB9DF2"             #   Monokai - Purple
    # red: str = "#FF5555"              #   Dracula - Red
    yellow: str = "#FFD866"             #   Monokai - Yellow
    

@dataclass(frozen=True, init=False)
class FleetTokenColors:
    white: str = "#ECEFF1"              #   Material - Blue Gray 50
    gray: str = "#767676"               #   Fleet - Gray 80
    lightGray: str = "#A0A0A0"          #   Fleet - Gray 100
    blue: str = "#87c3ff"               #   Fleet - Blue
    cyan: str = "#82D2CE"               #   Fleet - Cyan
    green: str = "#70CCA0"
    lime: str = "#A8CC7C"               #   Fleet - Lime
    orange: str = "#E09B70"             #   Fleet - Orange
    pink: str = "#E394DC"               #   Fleet - Pink
    purple: str = "#AF9CFF"             #   Fleet - Violet
    red: str = "#FF5555"
    coral: str = "#CC7C8A"              #   Fleet - Coral
    yellow: str = "#E6D58A"
    

# @dataclass(frozen=True, init=False)
# class VSCodeDefaultTokenColors:
#     gray: str = "#546E7A"               #   VSC Default
#     white: str = "#EEFFFF"              #   VSC Default
#     red: str = "#FF5370"                #   VSC Default
#     purple: str = "#C792EA"             #   VSC Default
#     lightBlue: str = "#89DDFF"          #   VSC Default
#     pink: str = "#f07178"               #   VSC Default
#     blue: str = "#82AAFF"               #   VSC Default
#     orange: str = "#F78C6C"             #   VSC Default
#     lime: str = "#C3E88D"               #   VSC Default
#     yellow: str = "#FFCB6B"             #   VSC Default
#     lightBlueGray: str = "#B2CCD6"      #   VSC Default


@dataclass(frozen=True, init=False)
class VSCodeDefaultTokenColors:
    #   https://github.com/microsoft/vscode/tree/main/extensions/theme-defaults
    white: str = "#C8C8C8"              #   VSC Default
    gray: str = "#808080"               #   VSC Default - Unused
    lightGray: str = "#D4D4D4"          #   VSC Default - Unused
    green: str = "#6A9955"              #   VSC Default - Unused
    lightGreen: str = "#B5CEA8"         #   VSC Default
    darkBlue: str = "#000080"           #   VSC Default - Unused
    blue: str = "#6796E6"               #   VSC Default
    lightBlue: str = "#9CDCFE"          #   VSC Default
    cyan: str = "#4FC1FF"               #   VSC Default - Unused
    lightCyan: str = "#569CD6"          #   VSC Default - Unused
    red: str = "#f44747"                #   VSC Default
    lightRed: str = "#D16969"           #   VSC Default - Unused
    yellow: str = "#D7BA7D"             #   VSC Default
    lightYellow: str = "#DCDCAA"        #   VSC Default
    purple: str = "#646695"             #   VSC Default - Unused
    teal: str = "#4EC9B0"               #   VSC Default
    magenta: str = "#C586C0"            #   VSC Default
    brown: str = "#CE9178"              #   VSC Default
    


@dataclass(frozen=True, init=False)
class StyxTokenColors:
    white: str = "#F2FBFF"              #   HSV -> 200°, 5%, 100%
    gray: str = "#5C6B99"               #   Dracula - Gray
    green: str = "#45E6B0"              #   HSV -> 160°, 70%, 90%
    teal: str = "#8AE6C0"               #   HSV -> 155°, 40%, 90%
    cyan: str = "#91F2F2"               #   HSV -> 180°, 40%, 95%
    blue: str = "#61CEF2"               #   HSV -> 195°, 60%, 95%
    coral: str = "#E67386"              #   HSV -> 350°, 50%, 90%
    pink: str = "#FFB3D9"               #   HSV -> 330°, 30%, 100%
    purple: str = "#AA80FF"             #   HSV -> 260°, 50%, 100%
    periwinkle: str = "#B6B6F2"         #   HSV -> 240°, 25%, 95%
    red: str = "#F25555"                #   HSV -> 0°, 65%, 95%
    amber: str = "#FFA64D"              #   HSV -> 30°, 70%, 100%
    yellow: str = "#FFE9A6"             #   HSV -> 45°, 35%, 100%
    lime: str = "#B8E6A1"               #   HSV -> 100°, 30%, 90%
    
    
@dataclass(frozen=True, init=False)
class DebugTokenColors:
    red: str = "#FF5555"
