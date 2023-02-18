from dataclasses import dataclass
from colors import DraculaTokenColors as dtc
from colors import FleetTokenColors as ftc
from colors import MaterialTokenColors as mtc
from colors import MonokaiTokenColors as mktc
from colors import VSCodeDefaultTokenColors as vtc
from colors import StyxTokenColors as stc
from colors import DebugTokenColors as dbtc


@dataclass(frozen=True, init=False)
class MaterialSyntaxHighlitingSystem:
    # <<- Programming Languages and Common ->>
    comment: tuple = (mtc.gray, None)
    variable: tuple = (mtc.white, None)
    variable_declaration: tuple = (mtc.white, None)
    module: tuple = (mtc.white, None)
    invalid: tuple = (mtc.red, None)
    reference: tuple = (mtc.red, None)
    keyword: tuple = (mtc.purple, None)
    keyword_control: tuple = (mtc.cyan, None)
    operator: tuple = (mtc.cyan, None)
    bind_operator: tuple = (mtc.red, None)
    punctuation: tuple = (mtc.cyan, None)
    punctuation_annotation: tuple = (mtc.cyan, None)
    function: tuple = (mtc.blue, None)
    decorator: tuple = (mtc.blue, None)
    decorator_definition_punctuation: tuple = (mtc.cyan, None)
    constant: tuple = (mtc.orange, None)
    string: tuple = (mtc.green, None)
    string_wrapper_punctuation: tuple = (mtc.cyan, None)
    _class: tuple = (mtc.yellow, None)
    _class_declaration: tuple = (mtc.yellow, None)
    parameter: tuple = (mtc.white, "italic")
    _type: tuple = (mtc.yellow, None)
    
    # <<- Markup and Common ->>
    tag: tuple = (mtc.red, None)
    attribute: tuple = (mtc.purple, None)
    color: tuple = (mtc.white, None)
    keyword_control_css: tuple = (mtc.cyan, "italic")
    keyword_unit_css: tuple = (mtc.orange, None)
    punctuation_definition_keyword: tuple = (mtc.cyan, "italic")
    punctuation_definition_entity: tuple = (mtc.cyan, None)
    property_css: tuple = (mtc.paleblue, None)
    _class_css: tuple = (mtc.yellow, None)
    
    # <<- Markdown and Common ->>
    link: tuple = (mtc.red, "underline")
    link_title: tuple = (mtc.green, None)
    plain_text: tuple = (mtc.white, None)
    section: tuple = (mtc.yellow, None)
    heading: tuple = (mtc.cyan, None)
    code_block: tuple = (mtc.gray, None)
    code_block_definition_punctuation: tuple = (mtc.green, None)
    raw_definition_punctuation: tuple = (mtc.cyan, None)
    raw_string: tuple = (mtc.green, None)
    separator: tuple = (mtc.gray, "bold")
    bold_italic: tuple = (mtc.pink, "bold")
    italic: tuple = (mtc.pink, "italic")


@dataclass(frozen=True, init=False)
class VSCodeSyntaxHighlitingSystem:
    # <<- Programming Languages and Common ->>
    comment: tuple = (vtc.brown, None)
    variable: tuple = (vtc.lightBlue, None)
    variable_declaration: tuple = (vtc.lightBlue, None)
    module: tuple = (vtc.teal, None)
    invalid: tuple = (vtc.red, None)
    reference: tuple = (vtc.lightBlue, None)
    keyword: tuple = (vtc.blue, None)
    keyword_control: tuple = (vtc.magenta, None)
    operator: tuple = (vtc.white, None)
    bind_operator: tuple = (vtc.white, None)
    punctuation: tuple = (vtc.white, None)
    punctuation_annotation: tuple = (vtc.white, None)
    function: tuple = (vtc.lightYellow, None)
    decorator: tuple = (vtc.lightYellow, None)
    decorator_definition_punctuation: tuple = (vtc.lightYellow, None)
    constant: tuple = (vtc.lightGreen, None)
    string: tuple = (vtc.brown, None)
    string_wrapper_punctuation: tuple = (vtc.brown, None)
    _class: tuple = (vtc.teal, None)
    _class_declaration: tuple = (vtc.teal, None)
    parameter: tuple = (vtc.lightBlue, None)
    _type: tuple = (vtc.lightBlue, None)
    
    # <<- Markup and Common ->>
    tag: tuple = (vtc.blue, None)
    attribute: tuple = (vtc.lightBlue, None)
    color: tuple = (vtc.magenta, None)
    keyword_control_css: tuple = (vtc.magenta, None)
    keyword_unit_css: tuple = (vtc.lightGreen, None)
    punctuation_definition_keyword: tuple = (vtc.magenta, None)
    punctuation_definition_entity: tuple = (vtc.yellow, None)
    property_css: tuple = (vtc.lightBlue, None)
    _class_css: tuple = (vtc.yellow, None)
    
    # <<- Markdown and Common ->>
    link: tuple = (vtc.white, "underline")
    link_title: tuple = (vtc.brown, None)
    plain_text: tuple = (vtc.white, None)
    section: tuple = (vtc.blue, "bold")
    heading: tuple = (vtc.blue, "bold")
    code_block: tuple = (vtc.white, None)
    code_block_definition_punctuation: tuple = (vtc.white, None)
    raw_definition_punctuation: tuple = (vtc.white, None)
    raw_string: tuple = (vtc.white, None)
    separator: tuple = (vtc.white, "bold")
    bold_italic: tuple = (vtc.lightBlue, "bold")
    italic: tuple = (vtc.lightBlue, "italic")
    
    
@dataclass(frozen=True, init=False)
class FleetSyntaxHighlitingSystem:
    # <<- Programming Languages and Common ->>
    comment: tuple = (ftc.gray, "italic") # X
    variable_declaration: tuple = (ftc.purple, None)
    variable: tuple = (ftc.white, None) # X
    module: tuple = (ftc.white, None) # X
    invalid: tuple = (ftc.red, None) # X
    reference: tuple = (ftc.coral, None)
    keyword: tuple = (ftc.cyan, None)
    keyword_control: tuple = (ftc.cyan, None) # X
    operator: tuple = (ftc.pink, None) # X
    bind_operator: tuple = (ftc.red, "italic") # X
    punctuation: tuple = (ftc.white, None) # X
    punctuation_annotation: tuple = (ftc.pink, None) # X
    function: tuple = (ftc.lime, None)
    decorator: tuple = (ftc.lime, None)
    decorator_definition_punctuation: tuple = (ftc.white, None)
    constant: tuple = (ftc.yellow, None) # X
    string: tuple = (ftc.pink, None)
    string_wrapper_punctuation: tuple = (ftc.pink, None)
    _class: tuple = (ftc.white, None) # X
    _class_declaration: tuple = (ftc.blue, None) # X
    parameter: tuple = (ftc.orange, "italic") # X
    _type: tuple = (ftc.cyan, None) # X
    
    # <<- Markup and Common ->>
    tag: tuple = (ftc.cyan, None)
    attribute: tuple = (ftc.purple, "italic")
    color: tuple = (ftc.purple, None) # X
    keyword_control_css: tuple = (ftc.purple, None)
    keyword_unit_css: tuple = (ftc.yellow, None)
    punctuation_definition_entity: tuple = (ftc.lime, None) # X
    punctuation_definition_keyword: tuple = (ftc.purple, None)
    property_css: tuple = (ftc.cyan, None) # X
    _class_css: tuple = (ftc.lime, None) # X
    
    # <<- Markdown and Common ->>
    link: tuple = (ftc.cyan, "underline")
    link_title: tuple = (ftc.pink, None)
    plain_text: tuple = (ftc.white, None)
    section: tuple = (ftc.purple, None)
    heading: tuple = (ftc.purple, None)
    code_block: tuple = (ftc.green, None)
    code_block_definition_punctuation: tuple = (ftc.green, None)
    raw_definition_punctuation: tuple = (ftc.green, None)
    raw_string: tuple = (ftc.green, None)
    separator: tuple = (ftc.gray, "bold")
    bold_italic: tuple = (ftc.pink, "bold")
    italic: tuple = (ftc.pink, "italic")


@dataclass(frozen=True, init=False)
class DraculaSyntaxHighlitingSystem:
    # <<- Programming Languages and Common ->>
    comment: tuple = (dtc.gray, "italic")
    variable: tuple = (dtc.white, None)
    variable_declaration: tuple = (dtc.white, None) # X
    module: tuple = (dtc.white, None)
    invalid: tuple = (dtc.red, None)
    reference: tuple = (dtc.purple, None)
    keyword: tuple = (dtc.pink, None)
    keyword_control: tuple = (dtc.pink, "italic")
    operator: tuple = (dtc.pink, None)
    bind_operator: tuple = (dtc.red, "italic")
    punctuation: tuple = (dtc.white, None)
    punctuation_annotation: tuple = (dtc.pink, None)
    function: tuple = (dtc.green, None)
    decorator: tuple = (dtc.green, None)
    decorator_definition_punctuation: tuple = (dtc.green, None)
    constant: tuple = (dtc.purple, None)
    string: tuple = (dtc.yellow, None)
    string_wrapper_punctuation: tuple = (dtc.yellow, None)
    _class: tuple = (dtc.cyan, None)
    _class_declaration: tuple = (dtc.cyan, None)
    parameter: tuple = (dtc.orange, "italic")
    _type: tuple = (dtc.cyan, None)
    
    # <<- Markup and Common ->>
    tag: tuple = (dtc.pink, None)
    attribute: tuple = (dtc.green, "italic")
    color: tuple = (dtc.purple, None)
    keyword_control_css: tuple = (dtc.pink, None)
    keyword_unit_css: tuple = (dtc.pink, None)
    punctuation_definition_entity: tuple = (dtc.green, None)
    punctuation_definition_keyword: tuple = (dtc.pink, None)
    property_css: tuple = (dtc.cyan, None)
    _class_css: tuple = (dtc.green, None)
    
    # <<- Markdown and Common ->>
    link: tuple = (dtc.cyan, "underline")
    link_title: tuple = (dtc.pink, None)
    plain_text: tuple = (dtc.white, None)
    section: tuple = (dtc.purple, "bold")
    heading: tuple = (dtc.purple, "bold")
    code_block: tuple = (dtc.green, None)
    code_block_definition_punctuation: tuple = (dtc.green, None)
    raw_definition_punctuation: tuple = (dtc.green, None)
    raw_string: tuple = (dtc.green, None)
    separator: tuple = (dtc.gray, "bold")
    bold_italic: tuple = (dtc.pink, "bold")
    italic: tuple = (dtc.pink, "italic")
    
    
@dataclass(frozen=True, init=False)
class MonokaiSyntaxHighlitingSystem:
    # <<- Programming Languages and Common ->>
    comment: tuple = (mktc.gray, "italic")
    variable: tuple = (mktc.white, None)
    variable_declaration: tuple = (mktc.white, None) # X
    module: tuple = (mktc.white, None)
    invalid: tuple = (mktc.white, None)    #   No Red in Monokai
    reference: tuple = (mktc.lightGray, None)
    keyword: tuple = (mktc.blue, "italic")
    keyword_control: tuple = (mktc.pink, None)
    operator: tuple = (mktc.pink, None)
    bind_operator: tuple = (mktc.pink, "italic")
    punctuation: tuple = (mktc.white, None)
    punctuation_annotation: tuple = (mktc.white, None)
    function: tuple = (mktc.green, None)
    decorator: tuple = (mktc.green, None)
    decorator_definition_punctuation: tuple = (mktc.lightGray, None)
    constant: tuple = (mktc.purple, None)
    string: tuple = (mktc.yellow, None)
    string_wrapper_punctuation: tuple = (mktc.blue, None)
    _class: tuple = (mktc.purple, None)
    _class_declaration: tuple = (mktc.blue, None)
    parameter: tuple = (mktc.orange, "italic")
    _type: tuple = (mktc.blue, None)
    
    # <<- Markup and Common ->>
    tag: tuple = (mktc.pink, None)
    attribute: tuple = (mktc.blue, "italic")
    color: tuple = (mktc.purple, None)
    keyword_control_css: tuple = (mktc.pink, None)
    keyword_unit_css: tuple = (mktc.pink, None)
    punctuation_definition_keyword: tuple = (mktc.gray, None)
    punctuation_definition_entity: tuple = (mktc.green, None)
    property_css: tuple = (mktc.white, None)
    _class_css: tuple = (mktc.green, None)
    
    # <<- Markdown and Common ->>
    link: tuple = (mktc.green, "underline")
    link_title: tuple = (mktc.pink, None)
    plain_text: tuple = (mktc.white, None)
    section: tuple = (mktc.yellow, None)
    heading: tuple = (mktc.gray, None)
    code_block: tuple = (mktc.white, None)
    code_block_definition_punctuation: tuple = (mktc.white, None)
    raw_definition_punctuation: tuple = (mktc.white, None)
    raw_string: tuple = (mktc.white, None)
    separator: tuple = (mktc.gray, "bold")
    bold_italic: tuple = (mktc.pink, "bold")
    italic: tuple = (mktc.pink, "italic")
    

@dataclass(frozen=True, init=False)
class DebugSyntaxHighlitingSystem:
    # <<- Programming Languages and Common ->>
    comment: tuple = (dbtc.red, "italic") # X
    variable: tuple = (dbtc.red, None) # X
    variable_declaration: tuple = (dbtc.red, None) # X
    module: tuple = (dbtc.red, None) # X
    invalid: tuple = (dbtc.red, None) # X
    reference: tuple = (dbtc.red, None) # X
    keyword: tuple = (dbtc.red, "italic") # X
    keyword_control: tuple = (dbtc.red, "italic") # X
    operator: tuple = (dbtc.red, None) # X
    bind_operator: tuple = (dbtc.red, "italic") # X
    punctuation: tuple = (dbtc.red, None) # X
    punctuation_annotation: tuple = (dbtc.red, None) # X
    function: tuple = (dbtc.red, None) # X
    decorator: tuple = (dbtc.red, None) # X
    decorator_definition_punctuation: tuple = (dbtc.red, None) # X
    constant: tuple = (dbtc.red, None) # X
    string: tuple = (dbtc.red, None) # X
    string_wrapper_punctuation: tuple = (dbtc.red, None) # X
    _class: tuple = (dbtc.red, None) # X
    _class_declaration: tuple = (dbtc.red, None) # X
    parameter: tuple = (dbtc.red, "italic") # X
    _type: tuple = (dbtc.red, None) # X
    
    # <<- Markup and Common ->>
    tag: tuple = (dbtc.red, None) # X
    attribute: tuple = (dbtc.red, "italic") # X - function
    color: tuple = (dbtc.red, None) # X
    keyword_control_css: tuple = (dbtc.red, None) # X
    keyword_unit_css: tuple = (dbtc.red, None) # X - keyword
    punctuation_definition_keyword: tuple = (dbtc.red, None) # X - operator
    punctuation_definition_entity: tuple = (dbtc.red, None) # X - operator
    property_css: tuple = (dbtc.red, None) # X - _type
    _class_css: tuple = (dbtc.red, None) # X
    
    # <<- Markdown and Common ->>
    link: tuple = (dbtc.red, "underline") # X - keyword_control
    link_title: tuple = (dbtc.red, None) # X - keyword
    plain_text: tuple = (dbtc.red, None) # X
    section: tuple = (dbtc.red, "bold") # X - constant
    heading: tuple = (dbtc.red, "bold") # X - constant
    code_block: tuple = (dbtc.red, None) # X - function
    code_block_definition_punctuation: tuple = (dbtc.red, None) # X - function
    raw_definition_punctuation: tuple = (dbtc.red, None) # X - function
    raw_string: tuple = (dbtc.red, None) # X - function
    separator: tuple = (dbtc.red, "bold") # X - comment
    bold_italic: tuple = (dbtc.red, "bold") # X - keyword
    italic: tuple = (dbtc.red, "italic") # X - keyword
    
    
@dataclass(frozen=True, init=False)
class StyxSyntaxHighlitingSystem:
    # <<- Programming Languages and Common ->>
    comment: tuple = (stc.gray, "italic")
    variable: tuple = (stc.white, None)
    variable_declaration: tuple = (stc.white, None)
    module: tuple = (stc.white, None)
    invalid: tuple = (stc.red, None)
    reference: tuple = (stc.coral, None)
    keyword: tuple = (stc.purple, "italic")
    keyword_control: tuple = (stc.periwinkle, "italic")
    operator: tuple = (stc.periwinkle, None)
    bind_operator: tuple = (stc.periwinkle, "italic")
    punctuation: tuple = (stc.periwinkle, None)
    punctuation_annotation: tuple = (stc.periwinkle, None)
    function: tuple = (stc.green, None)
    decorator: tuple = (stc.teal, None)
    decorator_definition_punctuation: tuple = (stc.periwinkle, None)
    constant: tuple = (stc.amber, None)
    string: tuple = (stc.yellow, None)
    string_wrapper_punctuation: tuple = (stc.periwinkle, None)
    _class: tuple = (stc.cyan, None)
    _class_declaration: tuple = (stc.blue, None)
    parameter: tuple = (stc.pink, "italic")
    _type: tuple = (stc.cyan, "italic")
    
    # <<- Markup and Common ->>
    tag: tuple = (stc.purple, None)
    attribute: tuple = (stc.pink, "italic")
    color: tuple = (stc.amber, None)
    keyword_control_css: tuple = (stc.purple, None)
    keyword_unit_css: tuple = (stc.yellow, None)
    punctuation_definition_keyword: tuple = (stc.periwinkle, None)
    punctuation_definition_entity: tuple = (stc.periwinkle, None)
    property_css: tuple = (stc.lime, None)
    _class_css: tuple = (stc.blue, None)
    
    # <<- Markdown and Common ->>
    link: tuple = (stc.cyan, "underline")
    link_title: tuple = (stc.purple, None)
    plain_text: tuple = (stc.white, None)
    section: tuple = (stc.amber, None)
    heading: tuple = (stc.periwinkle, None)
    code_block: tuple = (stc.green, None)
    code_block_definition_punctuation: tuple = (stc.periwinkle, None)
    raw_definition_punctuation: tuple = (stc.periwinkle, None)
    raw_string: tuple = (stc.green, None)
    separator: tuple = (stc.gray, "bold")
    bold_italic: tuple = (stc.purple, "bold")
    italic: tuple = (stc.purple, "italic")
    