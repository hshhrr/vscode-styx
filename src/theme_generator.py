import json
from theming import get_theme


def generate_theme(name: str, sh_system: str, brackets: str):
    theme = json.dumps(get_theme(name, sh_system, brackets), indent=4)
    path = "./themes/" + "-".join(name.split()).lower() + "-color-theme.json"
    
    with open(file=path, mode="w") as jsonfile:
        jsonfile.write(theme)
        

generate_theme("Styx", "styx", "styx")
generate_theme("Styx Plus", "styx", "styx_plus")
generate_theme("Styx Dracula", "dracula", "dracula")
generate_theme("Styx Fleet", "fleet", "fleet")
generate_theme("Styx Material", "material", "material")
generate_theme("Styx Monokai", "monokai", "monokai")
generate_theme("Styx VSCode", "vscode", "vscode")