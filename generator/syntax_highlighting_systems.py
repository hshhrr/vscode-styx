from dataclasses import dataclass
from colors import DraculaTokenColors as dtc
from colors import VSCodeDefaultTokenColors as vtc


@dataclass(frozen=True, init=False)
class VSCodeSyntaxHighlitingSystem:
    comment: tuple = (vtc.gray, "italic")
    variable: tuple = (vtc.white, None)
    module: tuple = (vtc.white, None)
    invalid: tuple = (vtc.red, None)
    reference: tuple = (vtc.red, "italic")
    keyword: tuple = (vtc.purple, None)
    operator: tuple = (vtc.lightBlue, None)
    punctuation: tuple = (vtc.lightBlue, None)
    tag: tuple = (vtc.pink, None)
    function: tuple = (vtc.blue, None)
    decorator: tuple = (vtc.blue, None)
    decorator_definition_punctuation: tuple = (vtc.lightBlue, None)
    constant: tuple = (vtc.orange, None)
    string: tuple = (vtc.lime, None)
    string_wrapper_punctuation: tuple = (vtc.lightBlue, None)
    _class: tuple = (vtc.lime, None)
    _class_declaration: tuple = (vtc.yellow, None)
    parameter: tuple = (vtc.orange, None)
    _type: tuple = (vtc.lightBlueGray, None)


@dataclass(frozen=True, init=False)
class DebugSyntaxHighlitingSystem:
    comment: tuple = (dtc.gray, "italic")
    variable: tuple = (dtc.white, None)
    module: tuple = (dtc.white, None)
    invalid: tuple = (dtc.red, None)
    reference: tuple = (dtc.purple, None)
    keyword: tuple = (dtc.pink, None)
    operator: tuple = (dtc.pink, None)
    punctuation: tuple = (dtc.white, None)
    tag: tuple = (dtc.pink, None)
    function: tuple = (dtc.green, None)
    decorator: tuple = (dtc.green, None)
    decorator_definition_punctuation: tuple = (dtc.green, None)
    constant: tuple = (dtc.purple, None)
    string: tuple = (dtc.yellow, None)
    string_wrapper_punctuation: tuple = (dtc.yellow, None)
    _class: tuple = (dtc.cyan, None)
    _class_declaration: tuple = (dtc.cyan, None)
    parameter: tuple = (dtc.orange, None)
    _type: tuple = (dtc.cyan, None)
