from text_paste import get_list_available_languages
from text_paste import get_random_paste


def tools_get_list_available_languages():
    """ Create new list with the languages from the documentation and
    compare it with the keys from the dictionary_with_languages """

    dictionary_with_languages = get_list_available_languages()
    keys_with_languages = dictionary_with_languages.keys()
    BoolLanguages = []
    tuple_with_languages = ('text', 'html5', 'css', 'javascript',
                            'php', 'python', 'ruby', 'lua',
                            'bash', 'erlang', 'go', 'c',
                            'cpp', 'diff', 'latex', 'sql',
                            'xml', '0', '4cs', '6502acme',
                            '6502kickass', '6502tasm', 'jquery',
                            '68000devpac', 'abap', 'actionscript',
                            'actionscript3', 'ada', 'algol68', 'apache',
                            'applescript', 'apt_sources', 'arm', 'asm',
                            'asymptote', 'asp', 'autoconf', 'autohotkey',
                            'autoit', 'avisynth', 'awk', 'bascomavr',
                            'basic4gl', 'bf', 'bibtex', 'blitzbasic',
                            'bnf', 'boo', 'c_loadrunner', 'c_mac', 'caddcl',
                            'cadlisp', 'cfdg', 'cfm', 'chaiscript', 'cil',
                            'clojure', 'cmake', 'cobol', 'coffeescript',
                            'csharp', 'cuesheet', 'd', 'dcs', 'dcl',
                            'dcpu16', 'delphi', 'div', 'dos', 'dot',
                            'e', 'ecmascript', 'eiffel', 'email',
                            'epc', 'euphoria', 'f1', 'falcon',
                            'fo', 'fortran', 'freebasic', 'freeswitch',
                            'fsharp', 'gambas', 'gdb', 'genero', 'genie',
                            'gettext', 'glsl', 'gml', 'gnuplot', 'groovy',
                            'gwbasic', 'haskell', 'haxe', 'hicest',
                            'hq9plus', 'html4strict', 'icon', 'idl', 'ini',
                            'inno', 'intercal', 'io', 'j', 'java', 'java5',
                            'klonec', 'klonecpp', 'lb', 'ldif', 'lisp', 'llvm',
                            'locobasic', 'logcat', 'logtalk', 'lolcode',
                            'lotusformulas', 'lotusscript', 'lscript', 'lsl2',
                            'm68k', 'magiksf', 'make', 'mapbasic', 'matlab',
                            'mirc', 'mmix', 'modula2', 'modula3',
                            'mpasm', 'mxml', 'mysql', 'nagios', 'netrexx',
                            'newlisp', 'nsis', 'oberon2', 'objc', 'objeck',
                            'ocaml', 'octave', 'oobas', 'oorexx', 'oracle11',
                            'oracle8', 'oxygene', 'oz', 'parasail', 'parigp',
                            'pascal', 'pcre', 'per', 'perl', 'perl6', 'pf',
                            'pic16', 'pike', 'pixelbender', 'pli',
                            'plsql', 'postgresql', 'povray', 'powerbuilder',
                            'powershell', 'proftpd', 'progress',
                            'prolog', 'properties', 'providex',
                            'purebasic', 'pys60', 'q', 'qbasic', 'rails',
                            'rebol', 'reg', 'rexx', 'robots',
                            'rpmspec', 'rsplus', 'sas', 'scala',
                            'scheme', 'scilab', 'sdlbasic',
                            'smalltalk', 'smarty', 'spark', 'sparql',
                            'stonescript', 'systemverilog', 'tcl', 'teraterm',
                            'thinbasic', 'tsql', 'typoscript', 'unicon',
                            'uscript', 'upc', 'urbi', 'vala', 'vb',
                            'vbnet', 'vedit', 'verilog', 'vhdl', 'vim',
                            'visualfoxpro', 'visualprolog', 'whitespace',
                            'whois', 'winbatch', 'xbasic', 'xorg_conf', 'xpp',
                            'yaml', 'z80', 'zxbasic')
    for every_language in tuple_with_languages:
        if every_language in keys_with_languages:
            BoolLanguages.append(True)
        else:
            BoolLanguages.append(False)
    return all(BoolLanguages)


def tools_get_random_paste():
    dictionary_with_random_paste = get_random_paste()
    dictionary_with_random_paste_keys = dictionary_with_random_paste.keys()
    BoolRandomPaste = []
    list_with_values = ['lang', 'title', 'name', 'url']
    for every_value in list_with_values:
        if every_value in dictionary_with_random_paste:
            BoolRandomPaste.append(True)
        else:
            BoolRandomPaste.append(False)
    return all(BoolRandomPaste)
