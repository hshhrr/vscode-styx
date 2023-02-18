RGB_SCALE = 255
CMY_SCALE = 100

rgb_norm = lambda x: x / RGB_SCALE
rgb_scaled = lambda x: x * RGB_SCALE

cmy_norm = lambda x: x / CMY_SCALE
cmy_scaled = lambda x: x * CMY_SCALE

rounded_val = lambda x: int(round(x, 0))

# Conversion between RGB to Hexadecimal color values
hex2rgb = lambda color: [int(x, 16) for x in map("".join, zip(*[iter(color.strip("#"))]*2))]
rgb2hex = lambda color: "#" + "".join(['%02X' % x for x in color])

# Conversion between RGB to CMYK color values
def rgb2cmyk_raw(color: tuple) -> tuple:
    k = 1 - rgb_norm(max(color))
    c, m, y = [(1 - rgb_norm(x) - k) / (1 - k) for x in color]
    return tuple(cmy_scaled(x) for x in [c, m, y, k])

rgb2cmyk = lambda color: tuple(rounded_val(x) for x in rgb2cmyk_raw(color))

cmyk2rgb_raw = lambda color: tuple(rgb_scaled((1 - cmy_norm(x)) * (1 - cmy_norm(color[-1]))) for x in color[:-1])
cmyk2rgb = lambda color: tuple(rounded_val(x) for x in cmyk2rgb_raw(color))


# https://en.wikipedia.org/wiki/HSL_and_HSV

# Chroma
chroma = lambda color: (max(color) - min(color)) / RGB_SCALE

# Value / Brightness
value = lambda color: max(color) / RGB_SCALE

# Lightness
lightness = lambda color: 0.5 * (max(color) + min(color)) / RGB_SCALE

# Saturation
saturation4v = lambda c, v: c / v if v != 0 else 0
saturation4l = lambda c, l: c / (1 - (abs((2*l) - 1))) if 1 > l > 0 else 0

# Hue
def hue(color: tuple) -> float:
    r, g, b = [rgb_norm(x) for x in color]
    c = chroma(color)
    
    if c == 0:
        h = 0
    else:
        if max(r, b, g) == r:
            h = ((g - b) / c) % 6
        elif max(r, g, b) == g:
            h = 2.0 + ((b - r) / c)
        else:
            h = 4.0 + ((r - g) / c)
        
    return h * 60

# Conversion between RGB to HSV color values
rgb2hsv_raw = lambda color: (
    hue(color),
    cmy_scaled(saturation4v(chroma(color),value(color))),
    cmy_scaled(value(color))
)
rgb2hsv = lambda color: tuple(rounded_val(x) for x in rgb2hsv_raw(color))

def hsv2rgb_raw(color: tuple) -> tuple:
    h, s, v = color[0], cmy_norm(color[1]), cmy_norm(color[2])
    k = lambda n: (n + (h / 60)) % 6
    f = lambda n: v - (v * s * max(0, min(k(n), 4 - k(n), 1)))
    r, g, b = f(5), f(3), f(1)
    
    return (rgb_scaled(x) for x in [r, g, b])

hsv2rgb = lambda color: tuple(rounded_val(x) for x in hsv2rgb_raw(color))

# Conversion between RGB to HSL color values
rgb2hsl_raw = lambda color: (
    hue(color),
    cmy_scaled(saturation4l(chroma(color), lightness(color))),
    cmy_scaled(lightness(color))
)
rgb2hsl = lambda color: tuple(rounded_val(x) for x in rgb2hsl_raw(color))

def hsl2rgb_raw(color: tuple) -> tuple:
    h, s, l = color[0], cmy_norm(color[1]), cmy_norm(color[2])
    k = lambda n: (n + (h / 30)) % 12
    a = s * min(l, (1 - l))
    f = lambda n: l - (a * max(-1, min(k(n) - 3, 9 - k(n), 1)))
    r, g, b = f(0), f(8), f(4)
    
    return (rgb_scaled(x) for x in [r, g, b])

hsl2rgb = lambda color: tuple(rounded_val(x) for x in hsl2rgb_raw(color))
