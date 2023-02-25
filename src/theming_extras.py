from colors import DraculaTokenColors as dtc
from colors import FleetTokenColors as ftc
from colors import MaterialTokenColors as mtc
from colors import MonokaiTokenColors as mktc
from colors import VSCodeDefaultTokenColors as vtc
from colors import StyxTokenColors as stc
from colors import DebugTokenColors as dbtc

from syntax_highlighting_systems import StyxSyntaxHighlitingSystem as sshs

def styx_extra_colors():
    return {
        #  https://code.visualstudio.com/api/references/theme-color
        
        #  <<- Bracket colors ->>
        "editorBracketHighlight.foreground1": stc.periwinkle,
        "editorBracketHighlight.foreground2": stc.periwinkle,
        "editorBracketHighlight.foreground3": stc.periwinkle,
        "editorBracketHighlight.foreground4": stc.periwinkle,
        "editorBracketHighlight.foreground5": stc.periwinkle,
        "editorBracketHighlight.foreground6": stc.periwinkle,
        "editorBracketHighlight.unexpectedBracket.foreground": stc.red,
        "editorBracketPairGuide.activeBackground1": stc.periwinkle,
        "editorBracketPairGuide.activeBackground2": stc.periwinkle,
        "editorBracketPairGuide.activeBackground3": stc.periwinkle,
        "editorBracketPairGuide.activeBackground4": stc.periwinkle,
        "editorBracketPairGuide.activeBackground5": stc.periwinkle,
        "editorBracketPairGuide.activeBackground6": stc.periwinkle,
        "editorBracketPairGuide.background1": stc.periwinkle,
        "editorBracketPairGuide.background2": stc.periwinkle,
        "editorBracketPairGuide.background3": stc.periwinkle,
        "editorBracketPairGuide.background4": stc.periwinkle,
        "editorBracketPairGuide.background5": stc.periwinkle,
        "editorBracketPairGuide.background6": stc.periwinkle,
        
        #  <<- Symbol Icon colors ->>
        "symbolIcon.arrayForeground": sshs._type[0], # <<-
        "symbolIcon.booleanForeground": sshs._type[0], # <<-
        "symbolIcon.classForeground": sshs._class_declaration[0],
        "symbolIcon.colorForeground": sshs.color[0],
        "symbolIcon.constantForeground": sshs.constant[0],
        "symbolIcon.constructorForeground": sshs.function[0],
        "symbolIcon.enumeratorForeground": sshs._class_declaration[0], # <<-
        "symbolIcon.enumeratorMemberForeground": sshs.function[0], # <<-
        "symbolIcon.eventForeground": sshs._class[0], # <<-
        "symbolIcon.fieldForeground": sshs.parameter[0], # <<-
        "symbolIcon.fileForeground": sshs.comment[0],
        "symbolIcon.folderForeground": sshs.string[0],
        "symbolIcon.functionForeground": sshs.function[0],
        "symbolIcon.interfaceForeground": sshs.function[0],
        "symbolIcon.keyForeground": sshs.keyword[0], # <<-
        "symbolIcon.keywordForeground": sshs.keyword[0],
        "symbolIcon.methodForeground": sshs.function[0],
        "symbolIcon.moduleForeground": sshs.module[0],
        "symbolIcon.namespaceForeground": sshs._class[0], # <<-
        "symbolIcon.nullForeground": sshs.constant[0], # <<-
        "symbolIcon.numberForeground": sshs.function[0], # <<-
        "symbolIcon.objectForeground": sshs._class[0],
        "symbolIcon.operatorForeground": sshs.invalid[0],
        "symbolIcon.packageForeground": sshs.module[0], # <<-
        "symbolIcon.propertyForeground": sshs.property_css[0], # <<-
        "symbolIcon.referenceForeground": sshs.reference[0],
        "symbolIcon.snippetForeground": sshs.comment[0],
        "symbolIcon.stringForeground": sshs.string[0],
        "symbolIcon.structForeground": sshs._class[0],
        "symbolIcon.textForeground": sshs.comment[0],
        "symbolIcon.typeParameterForeground": sshs._type[0],
        "symbolIcon.unitForeground": sshs.keyword_unit_css[0],
        "symbolIcon.variableForeground": sshs.variable_declaration[0],
    }
    
    
def styx_plus_extra_colors():
    return {
        #  https://code.visualstudio.com/api/references/theme-color
        
        #  <<- Bracket colors ->>
        "editorBracketHighlight.foreground1": stc.periwinkle,
        "editorBracketHighlight.foreground2": stc.blue,
        "editorBracketHighlight.foreground3": stc.cyan,
        "editorBracketHighlight.foreground4": stc.teal,
        "editorBracketHighlight.foreground5": stc.lime,
        "editorBracketHighlight.foreground6": stc.yellow,
        "editorBracketHighlight.unexpectedBracket.foreground": stc.red,
        "editorBracketPairGuide.activeBackground1": stc.periwinkle,
        "editorBracketPairGuide.activeBackground2": stc.blue,
        "editorBracketPairGuide.activeBackground3": stc.cyan,
        "editorBracketPairGuide.activeBackground4": stc.teal,
        "editorBracketPairGuide.activeBackground5": stc.lime,
        "editorBracketPairGuide.activeBackground6": stc.yellow,
        "editorBracketPairGuide.background1": stc.periwinkle,
        "editorBracketPairGuide.background2": stc.blue,
        "editorBracketPairGuide.background3": stc.cyan,
        "editorBracketPairGuide.background4": stc.teal,
        "editorBracketPairGuide.background5": stc.lime,
        "editorBracketPairGuide.background6": stc.yellow,
        
        #  <<- Symbol Icon colors ->>
        "symbolIcon.arrayForeground": sshs._type[0], # <<-
        "symbolIcon.booleanForeground": sshs._type[0], # <<-
        "symbolIcon.classForeground": sshs._class_declaration[0],
        "symbolIcon.colorForeground": sshs.color[0],
        "symbolIcon.constantForeground": sshs.constant[0],
        "symbolIcon.constructorForeground": sshs.function[0],
        "symbolIcon.enumeratorForeground": sshs._class_declaration[0], # <<-
        "symbolIcon.enumeratorMemberForeground": sshs.function[0], # <<-
        "symbolIcon.eventForeground": sshs._class[0], # <<-
        "symbolIcon.fieldForeground": sshs.parameter[0], # <<-
        "symbolIcon.fileForeground": sshs.comment[0],
        "symbolIcon.folderForeground": sshs.string[0],
        "symbolIcon.functionForeground": sshs.function[0],
        "symbolIcon.interfaceForeground": sshs.function[0],
        "symbolIcon.keyForeground": sshs.keyword[0], # <<-
        "symbolIcon.keywordForeground": sshs.keyword[0],
        "symbolIcon.methodForeground": sshs.function[0],
        "symbolIcon.moduleForeground": sshs.module[0],
        "symbolIcon.namespaceForeground": sshs._class[0], # <<-
        "symbolIcon.nullForeground": sshs.constant[0], # <<-
        "symbolIcon.numberForeground": sshs.function[0], # <<-
        "symbolIcon.objectForeground": sshs._class[0],
        "symbolIcon.operatorForeground": sshs.invalid[0],
        "symbolIcon.packageForeground": sshs.module[0], # <<-
        "symbolIcon.propertyForeground": sshs.property_css[0], # <<-
        "symbolIcon.referenceForeground": sshs.reference[0],
        "symbolIcon.snippetForeground": sshs.comment[0],
        "symbolIcon.stringForeground": sshs.string[0],
        "symbolIcon.structForeground": sshs._class[0],
        "symbolIcon.textForeground": sshs.comment[0],
        "symbolIcon.typeParameterForeground": sshs._type[0],
        "symbolIcon.unitForeground": sshs.keyword_unit_css[0],
        "symbolIcon.variableForeground": sshs.variable_declaration[0],
    }
    
    
def dracula_extra_colors():
    return {
        #  https://code.visualstudio.com/api/references/theme-color
        
        #  <<- Bracket colors ->>
        "editorBracketHighlight.foreground1": dtc.white,
        "editorBracketHighlight.foreground2": dtc.pink,
        "editorBracketHighlight.foreground3": dtc.cyan,
        "editorBracketHighlight.foreground4": dtc.green,
        "editorBracketHighlight.foreground5": dtc.purple,
        "editorBracketHighlight.foreground6": dtc.yellow,
        "editorBracketHighlight.unexpectedBracket.foreground": dtc.red,
        "editorBracketPairGuide.activeBackground1": dtc.white,
        "editorBracketPairGuide.activeBackground2": dtc.pink,
        "editorBracketPairGuide.activeBackground3": dtc.cyan,
        "editorBracketPairGuide.activeBackground4": dtc.green,
        "editorBracketPairGuide.activeBackground5": dtc.purple,
        "editorBracketPairGuide.activeBackground6": dtc.yellow,
        "editorBracketPairGuide.background1": dtc.white,
        "editorBracketPairGuide.background2": dtc.pink,
        "editorBracketPairGuide.background3": dtc.cyan,
        "editorBracketPairGuide.background4": dtc.green,
        "editorBracketPairGuide.background5": dtc.purple,
        "editorBracketPairGuide.background6": dtc.yellow,
    }
    

def material_extra_colors():
    return {
        #  https://code.visualstudio.com/api/references/theme-color
        
        #  <<- Bracket colors ->>
        "editorBracketHighlight.foreground1": mtc.yellow,
        "editorBracketHighlight.foreground2": mtc.violet,
        "editorBracketHighlight.foreground3": mtc.blue,
        "editorBracketHighlight.foreground4": mtc.yellow,
        "editorBracketHighlight.foreground5": mtc.violet,
        "editorBracketHighlight.foreground6": mtc.blue,
        "editorBracketHighlight.unexpectedBracket.foreground": mtc.red,
        "editorBracketPairGuide.activeBackground1": mtc.yellow,
        "editorBracketPairGuide.activeBackground2": mtc.violet,
        "editorBracketPairGuide.activeBackground3": mtc.blue,
        "editorBracketPairGuide.activeBackground4": mtc.yellow,
        "editorBracketPairGuide.activeBackground5": mtc.violet,
        "editorBracketPairGuide.activeBackground6": mtc.blue,
        "editorBracketPairGuide.background1": mtc.yellow,
        "editorBracketPairGuide.background2": mtc.violet,
        "editorBracketPairGuide.background3": mtc.blue,
        "editorBracketPairGuide.background4": mtc.yellow,
        "editorBracketPairGuide.background5": mtc.violet,
        "editorBracketPairGuide.background6": mtc.blue,
    }


def monokai_extra_colors():
    return {
        #  https://code.visualstudio.com/api/references/theme-color
        
        #  <<- Bracket colors ->>
        "editorBracketHighlight.foreground1": mktc.pink,
        "editorBracketHighlight.foreground2": mktc.orange,
        "editorBracketHighlight.foreground3": mktc.yellow,
        "editorBracketHighlight.foreground4": mktc.green,
        "editorBracketHighlight.foreground5": mktc.blue,
        "editorBracketHighlight.foreground6": mktc.purple,
        "editorBracketHighlight.unexpectedBracket.foreground": mktc.red, # Dracula - Red
        "editorBracketPairGuide.activeBackground1": mktc.pink,
        "editorBracketPairGuide.activeBackground2": mktc.orange,
        "editorBracketPairGuide.activeBackground3": mktc.yellow,
        "editorBracketPairGuide.activeBackground4": mktc.green,
        "editorBracketPairGuide.activeBackground5": mktc.blue,
        "editorBracketPairGuide.activeBackground6": mktc.purple,
        "editorBracketPairGuide.background1": mktc.pink,
        "editorBracketPairGuide.background2": mktc.orange,
        "editorBracketPairGuide.background3": mktc.yellow,
        "editorBracketPairGuide.background4": mktc.green,
        "editorBracketPairGuide.background5": mktc.blue,
        "editorBracketPairGuide.background6": mktc.purple,
    }


def fleet_extra_colors():
    return {
        #  https://code.visualstudio.com/api/references/theme-color
        
        #  <<- Bracket colors ->>
        "editorBracketHighlight.foreground1": ftc.white,
        "editorBracketHighlight.foreground2": ftc.white,
        "editorBracketHighlight.foreground3": ftc.white,
        "editorBracketHighlight.foreground4": ftc.white,
        "editorBracketHighlight.foreground5": ftc.white,
        "editorBracketHighlight.foreground6": ftc.white,
        "editorBracketHighlight.unexpectedBracket.foreground": ftc.red,
        "editorBracketPairGuide.activeBackground1": ftc.white,
        "editorBracketPairGuide.activeBackground2": ftc.white,
        "editorBracketPairGuide.activeBackground3": ftc.white,
        "editorBracketPairGuide.activeBackground4": ftc.white,
        "editorBracketPairGuide.activeBackground5": ftc.white,
        "editorBracketPairGuide.activeBackground6": ftc.white,
        "editorBracketPairGuide.background1": ftc.white,
        "editorBracketPairGuide.background2": ftc.white,
        "editorBracketPairGuide.background3": ftc.white,
        "editorBracketPairGuide.background4": ftc.white,
        "editorBracketPairGuide.background5": ftc.white,
        "editorBracketPairGuide.background6": ftc.white,
        
        #  <<- Symbol Icon colors ->>
        "symbolIcon.arrayForeground": ftc.white, # <<-
        "symbolIcon.booleanForeground": ftc.white, # <<-
        "symbolIcon.classForeground": ftc.white,
        "symbolIcon.colorForeground": ftc.white,
        "symbolIcon.constantForeground": ftc.white,
        "symbolIcon.constructorForeground": ftc.white,
        "symbolIcon.enumeratorForeground": ftc.white, # <<-
        "symbolIcon.enumeratorMemberForeground": ftc.white, # <<-
        "symbolIcon.eventForeground": ftc.white, # <<-
        "symbolIcon.fieldForeground": ftc.white, # <<-
        "symbolIcon.fileForeground": ftc.white,
        "symbolIcon.folderForeground": ftc.white,
        "symbolIcon.functionForeground": ftc.white,
        "symbolIcon.interfaceForeground": ftc.white,
        "symbolIcon.keyForeground": ftc.white, # <<-
        "symbolIcon.keywordForeground": ftc.white,
        "symbolIcon.methodForeground": ftc.white,
        "symbolIcon.moduleForeground": ftc.white,
        "symbolIcon.namespaceForeground": ftc.white, # <<-
        "symbolIcon.nullForeground": ftc.white, # <<-
        "symbolIcon.numberForeground": ftc.white, # <<-
        "symbolIcon.objectForeground": ftc.white,
        "symbolIcon.operatorForeground": ftc.white,
        "symbolIcon.packageForeground": ftc.white, # <<-
        "symbolIcon.propertyForeground": ftc.white, # <<-
        "symbolIcon.referenceForeground": ftc.white,
        "symbolIcon.snippetForeground": ftc.white,
        "symbolIcon.stringForeground": ftc.white,
        "symbolIcon.structForeground": ftc.white,
        "symbolIcon.textForeground": ftc.white,
        "symbolIcon.typeParameterForeground": ftc.white,
        "symbolIcon.unitForeground": ftc.white,
        "symbolIcon.variableForeground": ftc.white,
    }


def vscode_extra_colors():
    return {
        #  https://code.visualstudio.com/api/references/theme-color
        
        #  <<- Bracket colors ->>
        "editorBracketHighlight.foreground1": vtc.yellow,
        "editorBracketHighlight.foreground2": vtc.purple,
        "editorBracketHighlight.foreground3": vtc.blue,
        "editorBracketHighlight.foreground4": vtc.yellow,
        "editorBracketHighlight.foreground5": vtc.purple,
        "editorBracketHighlight.foreground6": vtc.blue,
        "editorBracketHighlight.unexpectedBracket.foreground": vtc.red,
        "editorBracketPairGuide.activeBackground1": vtc.yellow,
        "editorBracketPairGuide.activeBackground2": vtc.purple,
        "editorBracketPairGuide.activeBackground3": vtc.blue,
        "editorBracketPairGuide.activeBackground4": vtc.yellow,
        "editorBracketPairGuide.activeBackground5": vtc.purple,
        "editorBracketPairGuide.activeBackground6": vtc.blue,
        "editorBracketPairGuide.background1": vtc.yellow,
        "editorBracketPairGuide.background2": vtc.purple,
        "editorBracketPairGuide.background3": vtc.blue,
        "editorBracketPairGuide.background4": vtc.yellow,
        "editorBracketPairGuide.background5": vtc.purple,
        "editorBracketPairGuide.background6": vtc.blue,
    }


def debug_extra_colors():
    return {
        #  https://code.visualstudio.com/api/references/theme-color
        
        #  <<- Bracket colors ->>
        # "editorBracketHighlight.foreground1": dbtc.red,
        # "editorBracketHighlight.foreground2": dbtc.red,
        # "editorBracketHighlight.foreground3": dbtc.red,
        # "editorBracketHighlight.foreground4": dbtc.red,
        # "editorBracketHighlight.foreground5": dbtc.red,
        # "editorBracketHighlight.foreground6": dbtc.red,
        # "editorBracketHighlight.unexpectedBracket.foreground": dbtc.red,
        # "editorBracketPairGuide.activeBackground1": dbtc.red,
        # "editorBracketPairGuide.activeBackground2": dbtc.red,
        # "editorBracketPairGuide.activeBackground3": dbtc.red,
        # "editorBracketPairGuide.activeBackground4": dbtc.red,
        # "editorBracketPairGuide.activeBackground5": dbtc.red,
        # "editorBracketPairGuide.activeBackground6": dbtc.red,
        # "editorBracketPairGuide.background1": dbtc.red,
        # "editorBracketPairGuide.background2": dbtc.red,
        # "editorBracketPairGuide.background3": dbtc.red,
        # "editorBracketPairGuide.background4": dbtc.red,
        # "editorBracketPairGuide.background5": dbtc.red,
        # "editorBracketPairGuide.background6": dbtc.red,
        
        #  <<- Symbol Icon colors ->>
        # "symbolIcon.arrayForeground": dbtc.red,
        # "symbolIcon.booleanForeground": dbtc.red,
        # "symbolIcon.classForeground": dbtc.red,
        # "symbolIcon.colorForeground": dbtc.red,
        # "symbolIcon.constantForeground": dbtc.red,
        # "symbolIcon.constructorForeground": dbtc.red,
        # "symbolIcon.enumeratorForeground": dbtc.red,
        # "symbolIcon.enumeratorMemberForeground": dbtc.red,
        # "symbolIcon.eventForeground": dbtc.red,
        # "symbolIcon.fieldForeground": dbtc.red,
        # "symbolIcon.fileForeground": dbtc.red,
        # "symbolIcon.folderForeground": dbtc.red,
        # "symbolIcon.functionForeground": dbtc.red,
        # "symbolIcon.interfaceForeground": dbtc.red,
        # "symbolIcon.keyForeground": dbtc.red,
        # "symbolIcon.keywordForeground": dbtc.red,
        # "symbolIcon.methodForeground": dbtc.red,
        # "symbolIcon.moduleForeground": dbtc.red,
        # "symbolIcon.namespaceForeground": dbtc.red,
        # "symbolIcon.nullForeground": dbtc.red,
        # "symbolIcon.numberForeground": dbtc.red,
        # "symbolIcon.objectForeground": dbtc.red,
        # "symbolIcon.operatorForeground": dbtc.red,
        # "symbolIcon.packageForeground": dbtc.red,
        # "symbolIcon.propertyForeground": dbtc.red,
        # "symbolIcon.referenceForeground": dbtc.red,
        # "symbolIcon.snippetForeground": dbtc.red,
        # "symbolIcon.stringForeground": dbtc.red,
        # "symbolIcon.structForeground": dbtc.red,
        # "symbolIcon.textForeground": dbtc.red,
        # "symbolIcon.typeParameterForeground": dbtc.red,
        # "symbolIcon.unitForeground": dbtc.red,
        # "symbolIcon.variableForeground": dbtc.red,
    }