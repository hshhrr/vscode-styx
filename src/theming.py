import sys, inspect
from common import *
from theming_extras import *
from syntax_highlighting_systems import *


# Properties
props = lambda h : dict(zip(["foreground", "fontStyle"], [x for x in h if x is not None]))

# List of class names in syntax_highlighting_systems module
sh_systems = [(name, obj) for name, obj in inspect.getmembers(sys.modules["syntax_highlighting_systems"]) if inspect.isclass(obj)]

# List of function names for Bracket Coloring
bcf = [(name, obj) for name, obj in inspect.getmembers(sys.modules["theming_extras"]) if inspect.isfunction(obj)]


def get_syntax_highlighting_system(sh_system):
    common = "SyntaxHighlitingSystem"
    for s, obj in sh_systems:
        if common in s and s.split(common)[0].lower() == sh_system.lower():
            return obj
            
    return DebugSyntaxHighlitingSystem()


def get_bracket_colors(bc):
    # Brackets and others
    common = "_extra_colors"
    for s, func in bcf:
        if common in s and s.split(common)[0].lower() == bc.lower():
            return func()
            
    return debug_extra_colors()


def get_token_colors(sh_system: str) -> list:
    sh = get_syntax_highlighting_system(sh_system)
    
    return [
        {
            "name": "Comment",
            "scope": [
                "comment",
                "punctuation.definition.comment",
                "string.quoted.docstring.multi",
                "string.quoted.docstring.multi punctuation.definition.string",
                "source string.quoted.docstring.multi punctuation.definition.string",
                "constant.other.ellipsis",
            ],
            "settings": props(sh.comment)
        },
        {
            "name": "Variables",
            "scope": [
                # "variable.other.readwrite",
                "variable.other.member",
                "variable.other.property.js",
                "string constant.other.placeholder",
                "meta.function-call.arguments",
                "support.variable.property.js",
                "entity.name.variable",
            ],
            "settings": props(sh.variable)
        },
        {
            "name": "Source - Undefined",
            "scope": [
                "source.python"
            ],
            "settings": props(sh.module)
        },
        {
            "name": "Colors",
            "scope": [
                "constant.other.color",
            ],
            "settings": props(sh.color)
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
                # "keyword",
                "storage.control",
                "storage.type",
                "storage.modifier",
                "keyword.other",
            ],
            "settings": props(sh.keyword)
        },
        {
            "name": "CSS - Control Keyword",
            "scope": [
                "keyword.control.at-rule",
            ],
            "settings": props(sh.keyword_control_css)
        },
        {
            "name": "Punctuation - Definition Keyword, Constant",
            "scope": [
                "punctuation.definition.keyword",
                "punctuation.definition.constant",
            ],
            "settings": props(sh.punctuation_definition_keyword)
        },
        {
            "name": "Control Flow Keyword",
            "scope": [
                "keyword.control",
            ],
            "settings": props(sh.keyword_control)
        },
        {
            "name": "Operator, Misc",
            "scope": [
                # "constant.other.color",
                # "punctuation",
                "meta.tag",
                "punctuation.definition.tag",
                "punctuation.separator.inheritance.php",
                "punctuation.section.embedded",
                "punctuation.separator.pointer-access",
                "punctuation.separator.key-value",
                "keyword.other.template",
                "keyword.other.substitution",
                "keyword.operator",
                "keyword.operator.assignment",
                "source keyword.operator",
                "meta.symbol",
            ],
            "settings": props(sh.operator)
        },
        {
            "name": "Punctuation",
            "scope": [
                "punctuation",
                "punctuation.definition.tag.html",
                "punctuation.definition.tag.begin.html",
                "punctuation.definition.tag.end.html",
            ],
            "settings": props(sh.punctuation)
        },
        {
            "name": "Punctuation - Annotation Separator",
            "scope": [
                "punctuation.separator.annotation",
                "entity.other.attribute-name.pseudo-element.css punctuation.definition.entity.css"
            ],
            "settings": props(sh.punctuation_annotation)
        },
        {
            "name": "Punctuation - Entity Definition",
            "scope": [
                "punctuation.definition.entity",
            ],
            "settings": props(sh.punctuation_definition_entity)
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
                "source meta.function-call",
                "variable.function",
                "support.function",
                "keyword.other.special-method",
                "entity.name.method.js"
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
                "constant.other",
                "constant.escape",
                "constant.other.placeholder",
                "source constant.other.placeholder",
                "entity.other.keyframe-offset",
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
            "name": "String, Symbols, Markup Heading",
            "scope": [
                "string",
                "constant.other.symbol",
                "constant.other.key",
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
                "entity.other.inherited-class",
                "support.other.namespace.php",
                "markup.changed.git_gutter",
                "support.type.sys-types"
            ],
            "settings": props(sh._class)
        },
        {
            "name": "Entity Types",
            "scope": [
                "support.type",
                "keyword.type"
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
                "source.postcss support.type.property-name",
                "support.type.vendored.property-name"
            ],
            "settings": props(sh.property_css)
        },
        {
            "name": "CSS Unit",
            "scope": [
                "keyword.other.unit",
            ],
            "settings": props(sh.keyword_unit_css)
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
            "name": "meta.method.js",
            "scope": [
                "meta.class-method.js entity.name.function.js",
                "variable.function.constructor",
            ],
            "settings": props(sh.function)
        },
        {
            "name": "Attributes",
            "scope": [
                "entity.other.attribute-name",
            ],
            "settings": props(sh.attribute)
        },
        {
            "name": "HTML Attributes",
            "scope": [
                "text.html.basic entity.other.attribute-name.html",
                "text.html.basic entity.other.attribute-name"
            ],
            "settings": props(sh.attribute)
        },
        {
            "name": "CSS Classes",
            "scope": [
                "entity.other.attribute-name.class"
            ],
            "settings": props(sh._class_css)
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
			"scope": "markup.strikethrough",
			"settings": {
				"fontStyle": "strikethrough"
			}
		},
        {
            "name": "Decorator",
            "scope": [
                "tag.decorator.js entity.name.tag.js",
                "tag.decorator.js punctuation.definition.tag.js"
            ],
            "settings": props(sh.decorator)
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
            "settings": props(sh.bind_operator)
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
                "text.html.jinja",
                "punctuation.definition.list_item.markdown"
            ],
            "settings": props(sh.plain_text)
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
            "settings": props(sh.heading)
        },
        {
            "name": "Markup - Section",
            "scope": [
                "entity.name.section"
            ],
            "settings": props(sh.section)
        },
        {
            "name": "Markup - Italic",
            "scope": [
                "markup.italic"
            ],
            "settings": props(sh.italic)
        },
        {
            "name": "Markup - Bold",
            "scope": [
                "markup.bold",
                "markup.bold string"
            ],
            "settings": props(sh.bold_italic)
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
            "settings": props(sh.bold_italic)
        },
        {
            "name": "Markup - Underline",
            "scope": [
                "markup.underline"
            ],
            "settings": props(sh.link)
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
            "settings": props(sh.link_title)
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
            "name": "Markdown - Fenced Code Block",
            "scope": [
                "fenced_code.block.language.markdown",
            ],
            "settings": props(sh.code_block)
        },
        {
            "name": "Markdown - Fenced Code Block Punctuation",
            "scope": [
                "punctuation.definition.markdown",
            ],
            "settings": props(sh.code_block_definition_punctuation)
        },
        {
            "name": "Markdown - Raw Definition Punctuation",
            "scope": [
                "punctuation.definition.raw",
            ],
            "settings": props(sh.raw_definition_punctuation)
        },
        {
            "name": "Markdown - Raw String",
            "scope": [
                "markup.inline.raw.string",
            ],
            "settings": props(sh.raw_string)
        },
        {
            "name": "Markdown - Separator",
            "scope": [
                "meta.separator"
            ],
            "settings": props(sh.separator)
        },
        {
            "name": "Markup - Table",
            "scope": [
                "markup.table"
            ],
            "settings": props(sh.variable)
        }
    ]


def get_semantic_token_colors(sh_system) -> dict:
    sh = get_syntax_highlighting_system(sh_system)
    
    return {
        "variable.declaration": {
            "foreground": sh.variable_declaration[0],
        },
        "variable.defaultLibrary": {
            "foreground": sh.variable[0],
        },
        # "property": {
        #     "foreground": sh.variable[0],
        # },
        # "property.declaration": {
        #     "foreground": sh.variable_declaration[0],
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
        # "module": {
        #     "foreground": sh.module[0],
        # },
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
        "class.typeHint.builtin": {
            "foreground": sh._type[0],
        },
        "function": {
            "foreground": sh.function[0],
        },
        "function.decorator": {
            "foreground": sh.decorator[0],
        },
        "method": {
            "foreground": sh.function[0],
        },
        "parameter": {
            "foreground": sh.parameter[0],
        },
        "builtinConstant": {
            "foreground": sh.constant[0],
        },
    }


def get_theme(name: str, sh_system: str, bc: str = "styx") -> dict:
    ui_colors = get_ui_colors()
    ui_colors.update(get_bracket_colors(bc))
    return {
        "name": name,
        "$schema": "vscode://schemas/color-theme",
        "semanticHighlighting": True,
        "colors": ui_colors,
        "semanticTokenColors": get_semantic_token_colors(sh_system),
        "tokenColors": get_token_colors(sh_system),
    }
