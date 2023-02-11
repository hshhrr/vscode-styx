import json
from syntax_highlighting_systems import DebugSyntaxHighlitingSystem
from syntax_highlighting_systems import VSCodeSyntaxHighlitingSystem
from common import get_ui_colors


props = lambda h : dict(zip(["foreground", "fontStyle"], [x for x in h if x is not None]))

def get_token_colors() -> list:
    sh = DebugSyntaxHighlitingSystem()
    
    return [
        {
            "name": "Comment",
            "scope": [
                "comment",
                "punctuation.definition.comment",
                "string.quoted.docstring.multi",
                "string.quoted.docstring.multi punctuation.definition.string",
                "source string.quoted.docstring.multi punctuation.definition.string",
            ],
            "settings": props(sh.comment)
        },
        {
            "name": "Variables",
            "scope": [
                "variable.other.readwrite",
                "variable.other.member",
                "variable.other.property.js",
                   "string constant.other.placeholder"
            ],
            "settings": props(sh.variable)
        },
        {
            "name": "Colors",
            "scope": [
                "constant.other.color"
            ],
            "settings": props(sh.variable)
        },
        {
            "name": "Invalid",
            "scope": [
                "invalid",
                "invalid.illegal"
            ],
            "settings": props(sh.invalid)
        },
        {
            "name": "Keyword, Storage",
            "scope": [
                "keyword",
                "storage.type",
                "storage.modifier"
            ],
            "settings": props(sh.keyword)
        },
        {
            "name": "Operator, Misc",
            "scope": [
                "keyword.control",
                "constant.other.color",
                # "punctuation",
                "meta.tag",
                "punctuation.definition.tag",
                "punctuation.separator.inheritance.php",
                "punctuation.definition.tag.html",
                "punctuation.definition.tag.begin.html",
                "punctuation.definition.tag.end.html",
                "punctuation.section.embedded",
                "punctuation.separator.annotation",
                "punctuation.separator.pointer-access",
                "keyword.other.template",
                "keyword.other.substitution"
            ],
            "settings": props(sh.operator)
        },
        {
            "name": "Punctuation",
            "scope": [
                "punctuation",
            ],
            "settings": props(sh.punctuation)
        },
        {
            "name": "Tag",
            "scope": [
                "entity.name.tag",
                "meta.tag.sgml",
                "markup.deleted.git_gutter"
            ],
            "settings": props(sh.tag)
        },
        {
            "name": "Function, Special Method",
            "scope": [
                "entity.name.function",
                "meta.function entity.name.function",
                "source meta.function entity.name.function",
                "meta.function-call",
                "variable.function",
                "support.function",
                "keyword.other.special-method"
            ],
            "settings": props(sh.function)
        },
        {
            "name": "Block Level Variables",
            "scope": [
                "meta.block variable.other"
            ],
            "settings": props(sh.tag)
        },
        {
            "name": "Other Variable, String Link",
            "scope": [
                "support.other.variable",
                "string.other.link"
            ],
            "settings": props(sh.tag)
        },
        {
            "name": "Number, Constant, Tag Attribute, Embedded",
            "scope": [
                "constant.numeric",
                "constant.language",
                "support.constant",
                "constant.character",
                "constant.escape",
                "keyword.other.unit",
                "constant.other.placeholder",
                "source constant.other.placeholder",
                # "keyword.other"
            ],
            "settings": props(sh.constant)
        },
        {
            "name": "Parameter",
            "scope": [
                "variable.parameter",
            ],
            "settings": props(sh.parameter)
        },
        {
            "name": "String, Symbols, Inherited Class, Markup Heading",
            "scope": [
                "string",
                "constant.other.symbol",
                "constant.other.key",
                "entity.other.inherited-class",
                "markup.heading",
                "markup.inserted.git_gutter",
                "meta.group.braces.curly constant.other.object.key.js string.unquoted.label.js"
            ],
            "settings": props(sh.string)
        },
        {
            "name": "String Wrapper Punctuation",
            "scope": [
                "punctuation.definition.string",
            ],
            "settings": props(sh.string_wrapper_punctuation)
        },
        {
            "name": "Class, Support",
            "scope": [
                "entity.name",
                "support.type",
                "support.class",
                "support.other.namespace.use.php",
                "meta.use.php",
                "support.other.namespace.php",
                "markup.changed.git_gutter",
                "support.type.sys-types"
            ],
            "settings": props(sh._class)
        },
        {
            "name": "Entity Types",
            "scope": [
                "support.type"
            ],
            "settings": props(sh._type)
        },
        {
            "name": "CSS Class and Support",
            "scope": [
                "source.css support.type.property-name",
                "source.sass support.type.property-name",
                "source.scss support.type.property-name",
                "source.less support.type.property-name",
                "source.stylus support.type.property-name",
                "source.postcss support.type.property-name"
            ],
            "settings": props(sh._type)
        },
        {
            "name": "Sub-methods",
            "scope": [
                "entity.name.module.js",
                "variable.import.parameter.js",
                "variable.other.class.js"
            ],
            "settings": props(sh.invalid)
        },
        {
            "name": "Language methods",
            "scope": [
                "variable.language"
            ],
            "settings": props(sh.reference)
        },
        {
            "name": "entity.name.method.js",
            "scope": [
                "entity.name.method.js"
            ],
            "settings": {
                "fontStyle": "italic",
                "foreground": sh.function[0]
            }
        },
        {
            "name": "meta.method.js",
            "scope": [
                "meta.class-method.js entity.name.function.js",
                "variable.function.constructor"
            ],
            "settings": props(sh.function)
        },
        {
            "name": "Attributes",
            "scope": [
                "entity.other.attribute-name"
            ],
            "settings": props(sh.keyword)
        },
        {
            "name": "HTML Attributes",
            "scope": [
                "text.html.basic entity.other.attribute-name.html",
                "text.html.basic entity.other.attribute-name"
            ],
            "settings": {
                "fontStyle": "italic",
                "foreground": sh._class[0]
            }
        },
        {
            "name": "CSS Classes",
            "scope": [
                "entity.other.attribute-name.class"
            ],
            "settings": props(sh._class)
        },
        {
            "name": "CSS ID's",
            "scope": [
                "source.sass keyword.control"
            ],
            "settings": props(sh.function)
        },
        {
            "name": "Inserted",
            "scope": [
                "markup.inserted"
            ],
            "settings": props(sh.string)
        },
        {
            "name": "Deleted",
            "scope": [
                "markup.deleted"
            ],
            "settings": props(sh.invalid)
        },
        {
            "name": "Changed",
            "scope": [
                "markup.changed"
            ],
            "settings": props(sh.keyword)
        },
        {
            "name": "Regular Expressions",
            "scope": [
                "string.regexp"
            ],
            "settings": props(sh.operator)
        },
        {
            "name": "Escape Characters",
            "scope": [
                "constant.character.escape"
            ],
            "settings": props(sh.operator)
        },
        {
            "name": "URL",
            "scope": [
                "*url*",
                "*link*",
                "*uri*"
            ],
            "settings": {
                "fontStyle": "underline"
            }
        },
        {
            "name": "Decorator",
            "scope": [
                "tag.decorator.js entity.name.tag.js",
                "tag.decorator.js punctuation.definition.tag.js"
            ],
            "settings": {
                "fontStyle": "italic",
                "foreground": sh.function[0]
            }
        },
        {
            "name": "Decorator Definition Punctuation",
            "scope": [
                "punctuation.definition.decorator",
            ],
            "settings": props(sh.decorator_definition_punctuation)
        },
        {
            "name": "ES7 Bind Operator",
            "scope": [
                "source.js constant.other.object.key.js string.unquoted.label.js"
            ],
            "settings": {
                "fontStyle": "italic",
                "foreground": sh.invalid[0]
            }
        },
        {
            "name": "JSON Key",
            "scope": [
                "source.json meta.structure.dictionary.json support.type.property-name.json"
            ],
            "settings": props(sh.keyword)
        },
        {
            "name": "Markdown - Plain",
            "scope": [
                "text.html.markdown",
                "punctuation.definition.list_item.markdown"
            ],
            "settings": props(sh.variable)
        },
        {
            "name": "Markdown - Markup Raw Inline",
            "scope": [
                "text.html.markdown markup.inline.raw.markdown"
            ],
            "settings": props(sh.keyword)
        },
        {
            "name": "Markdown - Markup Raw Inline Punctuation",
            "scope": [
                "text.html.markdown markup.inline.raw.markdown punctuation.definition.raw.markdown"
            ],
            "settings": props(sh.comment)
        },
        {
            "name": "Markdown - Heading",
            "scope": [
                "markdown.heading",
                "markup.heading | markup.heading entity.name",
                "markup.heading.markdown punctuation.definition.heading.markdown"
            ],
            "settings": props(sh.string)
        },
        {
            "name": "Markup - Italic",
            "scope": [
                "markup.italic"
            ],
            "settings": {
                "fontStyle": "italic",
                "foreground": sh.tag[0]
            }
        },
        {
            "name": "Markup - Bold",
            "scope": [
                "markup.bold",
                "markup.bold string"
            ],
            "settings": {
                "fontStyle": "bold",
                "foreground": sh.tag[0]
            }
        },
        {
            "name": "Markup - Bold-Italic",
            "scope": [
                "markup.bold markup.italic",
                "markup.italic markup.bold",
                "markup.quote markup.bold",
                "markup.bold markup.italic string",
                "markup.italic markup.bold string",
                "markup.quote markup.bold string"
            ],
            "settings": {
                "fontStyle": "bold",
                "foreground": sh.tag[0]
            }
        },
        {
            "name": "Markup - Underline",
            "scope": [
                "markup.underline"
            ],
            "settings": {
                "fontStyle": "underline",
                "foreground": sh.constant[0]
            }
        },
        {
            "name": "Markdown - Blockquote",
            "scope": [
                "markup.quote punctuation.definition.blockquote.markdown"
            ],
            "settings": props(sh.comment)
        },
        {
            "name": "Markup - Quote",
            "scope": [
                "markup.quote"
            ],
            "settings": {
                "fontStyle": "italic"
            }
        },
        {
            "name": "Markdown - Link",
            "scope": [
                "string.other.link.title.markdown"
            ],
            "settings": props(sh.function)
        },
        {
            "name": "Markdown - Link Description",
            "scope": [
                "string.other.link.description.title.markdown"
            ],
            "settings": props(sh.keyword)
        },
        {
            "name": "Markdown - Link Anchor",
            "scope": [
                "constant.other.reference.link.markdown"
            ],
            "settings": props(sh._class)
        },
        {
            "name": "Markup - Raw Block",
            "scope": [
                "markup.raw.block"
            ],
            "settings": props(sh.keyword)
        },
        {
            "name": "Markdown - Raw Block Fenced",
            "scope": [
                "markup.raw.block.fenced.markdown"
            ],
            "settings": props(sh.comment)
        },
        {
            "name": "Markdown - Fenced Bode Block",
            "scope": [
                "punctuation.definition.fenced.markdown"
            ],
            "settings": props(sh.comment)
        },
        {
            "name": "Markdown - Fenced Bode Block Variable",
            "scope": [
                "markup.raw.block.fenced.markdown",
                "variable.language.fenced.markdown",
                "punctuation.section.class.end"
            ],
            "settings": props(sh.variable)
        },
        {
            "name": "Markdown - Fenced Language",
            "scope": [
                "variable.language.fenced.markdown"
            ],
            "settings": props(sh.comment)
        },
        {
            "name": "Markdown - Separator",
            "scope": [
                "meta.separator"
            ],
            "settings": {
                "fontStyle": "bold",
                "foreground": sh.comment[0]
            }
        },
        {
            "name": "Markup - Table",
            "scope": [
                "markup.table"
            ],
            "settings": props(sh.variable)
        }
    ]


def get_semantic_token_colors() -> dict:
    sh = DebugSyntaxHighlitingSystem()
    
    return {
        "variable.declaration": {
            "foreground": sh.variable[0],
        },
        # "property.declaration": {
        #     "foreground": sh.variable[0],
        # },
        "property.decorator": {
            "foreground": sh.decorator[0],
        },
        "selfParameter": {
            "foreground": sh.reference[0],
        },
        "selfParameter.declaration": {
            "foreground": sh.reference[0],
        },
        "module": {
            "foreground": sh.module[0],
        },
        "class": {
            "foreground": sh._class[0],
        },
        "class.declaration": {
            "foreground": sh._class_declaration[0],
        },
        "class.decorator": {
            "foreground": sh.decorator[0],
        },
        "class.decorator.builtin": {
            "foreground": sh.decorator[0],
        },
        "function": {
            "foreground": sh.function[0],
        },
        "method": {
            "foreground": sh.function[0],
        },
        "parameter": {
            "foreground": sh.parameter[0],
        },
        # "builtinConstant": {
        #     "foreground": sh.purple[0],
        # },
        # "variable.defaultLibrary": {
        #     "foreground": sh.purple[0],
        # },
    }


def get_theme(name:str) -> dict:
    return {
        "name": name,
        "$schema": "vscode://schemas/color-theme",
        "semanticHighlighting": True,
        "colors": get_ui_colors(),
        "semanticTokenColors": get_semantic_token_colors(),
        "tokenColors": get_token_colors(),
    }

theme = json.dumps(get_theme("Styx"), indent=4)
path = r"C:/Users/hasan/OneDrive/Desktop/vscode-theme/styx/themes/Styx-color-theme.json"

with open(file=path, mode="w") as jsonfile:
    jsonfile.write(theme)