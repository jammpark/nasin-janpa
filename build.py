# (c) 2022 Robert Winslow. Originally posted at https://github.com/RobertWinslow/Simple-SVG-to-Font-with-Fontforge
# Feel free to use this little script however you like. I claim no ownership over any fonts you create with it.
# All I ask is that you provide attribution by preserving this copyright notice in this script and its derivatives.
# (If you need something formal, this script is released under a CC BY-SA 4.0 license.)

import fontforge
import os

OUTPUTFILENAME = 'nasin-janpa.ttf'

font = fontforge.font()
font.familyname = "nasin janpa"
font.fullname = "nasin janpa"
font.copyright = "Copyright (c) 2025 jan Janpa"
font.version = "1.0"

SVGHEIGHT = 72
GLYPHHEIGHT = 1000
FULLWIDTH_SPACE = 850
PORTIONABOVEBASELINE = 0.8
CARTOUCHE_HEIGHT = (-349, -243, 841, 948)

SCALEFACTOR = GLYPHHEIGHT / SVGHEIGHT

EMPTY_GLYPHS = {
    ord("a"): "a",
    ord("e"): "e",
    ord("n"): "n",
    ord("o"): "o",
    ord("["): "bracketleft",
    ord("]"): "bracketright",
    ord("("): "parenthesisleft",
    ord(")"): "parenthesisright",
    ord("."): "period",
    ord(":"): "colon",
    ord("-"): "hyphen",
}

ALPHABETS = {
    ord("i"): "i",
    ord("j"): "j",
    ord("k"): "k",
    ord("l"): "l",
    ord("m"): "m",
    ord("p"): "p",
    ord("s"): "s",
    ord("t"): "t",
    ord("u"): "u",
    ord("w"): "w",
}

NIMI_UCSUR = {
    0xF1900: ("a", tuple(list("a"))),
    0xF1901: ("akesi", tuple(list("akesi"))),
    0xF1902: ("ala", tuple(list("ala"))),
    0xF1903: ("alasa", tuple(list("alasa"))),
    0xF1904: ("ale", tuple(list("ale"))),
    0xF1905: ("anpa", tuple(list("anpa"))),
    0xF1906: ("ante", tuple(list("ante"))),
    0xF1907: ("anu", tuple(list("anu"))),
    0xF1908: ("awen", tuple(list("awen"))),
    0xF1909: ("e", tuple(list("e"))),
    0xF190A: ("en", tuple(list("en"))),
    0xF190B: ("esun", tuple(list("esun"))),
    0xF190C: ("ijo", tuple(list("ijo"))),
    0xF190D: ("ike", tuple(list("ike"))),
    0xF190E: ("ilo", tuple(list("ilo"))),
    0xF190F: ("insa", tuple(list("insa"))),
    
    0xF1910: ("jaki", tuple(list("jaki"))),
    0xF1911: ("jan", tuple(list("jan"))),
    0xF1912: ("jelo", tuple(list("jelo"))),
    0xF1913: ("jo", tuple(list("jo"))),
    0xF1914: ("kala", tuple(list("kala"))),
    0xF1915: ("kalama", tuple(list("kalama"))),
    0xF1916: ("kama", tuple(list("kama"))),
    0xF1917: ("kasi", tuple(list("kasi"))),
    0xF1918: ("ken", tuple(list("ken"))),
    0xF1919: ("kepeken", tuple(list("kepeken"))),
    0xF191A: ("kili", tuple(list("kili"))),
    0xF191B: ("kiwen", tuple(list("kiwen"))),
    0xF191C: ("ko", tuple(list("ko"))),
    0xF191D: ("kon", tuple(list("kon"))),
    0xF191E: ("kule", tuple(list("kule"))),
    0xF191F: ("kulupu", tuple(list("kulupu"))),
    
    0xF1920: ("kute", tuple(list("kute"))),
    0xF1921: ("la", tuple(list("la"))),
    0xF1922: ("lape", tuple(list("lape"))),
    0xF1923: ("laso", tuple(list("laso"))),
    0xF1924: ("lawa", tuple(list("lawa"))),
    0xF1925: ("len", tuple(list("len"))),
    0xF1926: ("lete", tuple(list("lete"))),
    0xF1927: ("li", tuple(list("li"))),
    0xF1928: ("lili", tuple(list("lili"))),
    0xF1929: ("linja", tuple(list("linja"))),
    0xF192A: ("lipu", tuple(list("lipu"))),
    0xF192B: ("loje", tuple(list("loje"))),
    0xF192C: ("lon", tuple(list("lon"))),
    0xF192D: ("luka", tuple(list("luka"))),
    0xF192E: ("lukin", tuple(list("lukin"))),
    0xF192F: ("lupa", tuple(list("lupa"))),
    
    0xF1930: ("ma", tuple(list("ma"))),
    0xF1931: ("mama", tuple(list("mama"))),
    0xF1932: ("mani", tuple(list("mani"))),
    0xF1933: ("meli", tuple(list("meli"))),
    0xF1934: ("mi", tuple(list("mi"))),
    0xF1935: ("mije", tuple(list("mije"))),
    0xF1936: ("moku", tuple(list("moku"))),
    0xF1937: ("moli", tuple(list("moli"))),
    0xF1938: ("monsi", tuple(list("monsi"))),
    0xF1939: ("mu", tuple(list("mu"))),
    0xF193A: ("mun", tuple(list("mun"))),
    0xF193B: ("musi", tuple(list("musi"))),
    0xF193C: ("mute", tuple(list("mute"))),
    0xF193D: ("nanpa", tuple(list("nanpa"))),
    0xF193E: ("nasa", tuple(list("nasa"))),
    0xF193F: ("nasin", tuple(list("nasin"))),
    
    0xF1940: ("nena", tuple(list("nena"))),
    0xF1941: ("ni", tuple(list("ni"))),
    0xF1942: ("nimi", tuple(list("nimi"))),
    0xF1943: ("noka", tuple(list("noka"))),
    0xF1944: ("o", tuple(list("o"))),
    0xF1945: ("olin", tuple(list("olin"))),
    0xF1946: ("ona", tuple(list("ona"))),
    0xF1947: ("open", tuple(list("open"))),
    0xF1948: ("pakala", tuple(list("pakala"))),
    0xF1949: ("pali", tuple(list("pali"))),
    0xF194A: ("palisa", tuple(list("palisa"))),
    0xF194B: ("pan", tuple(list("pan"))),
    0xF194C: ("pana", tuple(list("pana"))),
    0xF194D: ("pi", tuple(list("pi"))),
    0xF194E: ("pilin", tuple(list("pilin"))),
    0xF194F: ("pimeja", tuple(list("pimeja"))),
    
    0xF1950: ("pini", tuple(list("pini"))),
    0xF1951: ("pipi", tuple(list("pipi"))),
    0xF1952: ("poka", tuple(list("poka"))),
    0xF1953: ("poki", tuple(list("poki"))),
    0xF1954: ("pona", tuple(list("pona"))),
    0xF1955: ("pu", tuple(list("pu"))),
    0xF1956: ("sama", tuple(list("sama"))),
    0xF1957: ("seli", tuple(list("seli"))),
    0xF1958: ("selo", tuple(list("selo"))),
    0xF1959: ("seme", tuple(list("seme"))),
    0xF195A: ("sewi", tuple(list("sewi"))),
    0xF195B: ("sijelo", tuple(list("sijelo"))),
    0xF195C: ("sike", tuple(list("sike"))),
    0xF195D: ("sin", tuple(list("sin"))),
    0xF195E: ("sina", tuple(list("sina"))),
    0xF195F: ("sinpin", tuple(list("sinpin"))),
    
    0xF1960: ("sitelen", tuple(list("sitelen"))),
    0xF1961: ("sona", tuple(list("sona"))),
    0xF1962: ("soweli", tuple(list("soweli"))),
    0xF1963: ("suli", tuple(list("suli"))),
    0xF1964: ("suno", tuple(list("suno"))),
    0xF1965: ("supa", tuple(list("supa"))),
    0xF1966: ("suwi", tuple(list("suwi"))),
    0xF1967: ("tan", tuple(list("tan"))),
    0xF1968: ("taso", tuple(list("taso"))),
    0xF1969: ("tawa", tuple(list("tawa"))),
    0xF196A: ("telo", tuple(list("telo"))),
    0xF196B: ("tenpo", tuple(list("tenpo"))),
    0xF196C: ("toki", tuple(list("toki"))),
    0xF196D: ("tomo", tuple(list("tomo"))),
    0xF196E: ("tu", tuple(list("tu"))),
    0xF196F: ("unpa", tuple(list("unpa"))),
    
    0xF1970: ("uta", tuple(list("uta"))),
    0xF1971: ("utala", tuple(list("utala"))),
    0xF1972: ("walo", tuple(list("walo"))),
    0xF1973: ("wan", tuple(list("wan"))),
    0xF1974: ("waso", tuple(list("waso"))),
    0xF1975: ("wawa", tuple(list("wawa"))),
    0xF1976: ("weka", tuple(list("weka"))),
    0xF1977: ("wile", tuple(list("wile"))),
    0xF1978: ("namako", tuple(list("namako"))),
    0xF1979: ("kin", tuple(list("kin"))),
    0xF197A: ("oko", tuple(list("oko"))),
    0xF197B: ("kipisi", tuple(list("kipisi"))),
    0xF197C: ("leko", tuple(list("leko"))),
    0xF197D: ("monsuta", tuple(list("monsuta"))),
    0xF197E: ("tonsi", tuple(list("tonsi"))),
    0xF197F: ("jasima", tuple(list("jasima"))),
    
    0xF1980: ("kijetesantakalu", tuple(list("kijetesantakalu"))),
    0xF1981: ("soko", tuple(list("soko"))),
    0xF1982: ("meso", tuple(list("meso"))),
    0xF1983: ("epiku", tuple(list("epiku"))),
    0xF1984: ("kokosila", tuple(list("kokosila"))),
    0xF1985: ("lanpan", tuple(list("lanpan"))),
    0xF1986: ("n", tuple(list("n"))),
    0xF1987: ("misikeke", tuple(list("misikeke"))),
    0xF1988: ("ku", tuple(list("ku"))),

    0xF19A0: ("pake", tuple(list("pake"))),
    0xF19A1: ("apeja", tuple(list("apeja"))),
    0xF19A2: ("majuna", tuple(list("majuna"))),
    0xF19A3: ("powe", tuple(list("powe"))),
    
    0xF199C: ("middledot", tuple(["period"])),
    0xF199D: ("colon", tuple(["colon"])),
}

NIMI_PI_LAWA_LINJA = [
    "kepeken",
    "lon",
    "pi",
    "sama",
    "tan",
    "tawa"
]

def nimi_jan(x: str):
    words = x.split(' ')
    return (words[0], tuple(list(words[0])), tuple(f"toki_{word}" for word in words[1:]))

NIMI_SIN = [ (x[:-4], tuple(list(x[:-4]))) for x in os.listdir("nimi_sin") ]
NIMI_JAN = [ nimi_jan(x.strip()) for x in open("nimi_jan.txt").readlines() ]

def importAndCleanOutlines(outlinefile, glyph):
    glyph.importOutlines(outlinefile, simplify=True, correctdir=False, accuracy=0.25, scale=False)
    glyph.removeOverlap()
    foregroundlayer = glyph.foreground
    for contour in foregroundlayer:
        for point in contour:
            point.transform((1, 0, 0, 1, 0, -800))
            point.transform((SCALEFACTOR, 0, 0, SCALEFACTOR, 0, 0))
            point.transform((1, 0, 0, 1, 0, PORTIONABOVEBASELINE * GLYPHHEIGHT))
    glyph.setLayer(foregroundlayer, 'Fore')

font.addLookup('CartoucheVariantsLookup', 'gsub_single', None, (("cv01",(('DFLT',("dflt",)),('latn',("dflt",)),)),))
font.addLookup('LongGlyphVariantsLookup', 'gsub_single', None, (("cv01",(('DFLT',("dflt",)),('latn',("dflt",)),)),))
font.addLookup('CartoucheCaltLookup', 'gsub_contextchain', None, (("calt",(('DFLT',("dflt",)),('latn',("dflt",)),)),))
font.addLookup('LongGlyphCaltLookup', 'gsub_contextchain', None, (("calt",(('DFLT',("dflt",)),('latn',("dflt",)),)),))
font.addLookup('NimiJanLookup', 'gsub_multiple', None, (("ccmp",(('DFLT',("dflt",)),('latn',("dflt",)),)),))
font.addLookup('LongGlyphLigatureLookup', 'gsub_ligature', None, (("liga",(('DFLT',("dflt",)),('latn',("dflt",)),)),))
font.addLookup('SitelenPonaLookup', 'gsub_ligature', None, (("liga",(('DFLT',("dflt",)),('latn',("dflt",)),)),))

font.addLookupSubtable("CartoucheVariantsLookup", "CartoucheVariantsLookupSubtable")
font.addLookupSubtable("LongGlyphVariantsLookup", "LongGlyphVariantsLookupSubtable")
font.addLookupSubtable("SitelenPonaLookup", "SitelenPonaLookupSubtable")
font.addLookupSubtable("LongGlyphLigatureLookup", "LongGlyphLigatureLookupSubtable")
font.addLookupSubtable("NimiJanLookup", "NimiJanLookupSubtable")

for i in EMPTY_GLYPHS:
    spaceChar = font.createChar(i, EMPTY_GLYPHS[i])

for i in ALPHABETS:
    char = font.createChar(i, f'{ALPHABETS[i]}')
    importAndCleanOutlines(f'nimi_suli/{ALPHABETS[i]}.svg', char)

for i in NIMI_UCSUR:
    char = font.createChar(i, f'toki_{NIMI_UCSUR[i][0]}')
    char.addPosSub("SitelenPonaLookupSubtable", NIMI_UCSUR[i][1])
    importAndCleanOutlines(f'nimi_suli/{NIMI_UCSUR[i][0]}.svg', char)

for (i, j) in NIMI_SIN:
    char = font.createChar(-1, f'toki_{i}')
    char.addPosSub("SitelenPonaLookupSubtable", j)
    importAndCleanOutlines(f'nimi_sin/{i}.svg', char)

open_cartouche_char = font.createChar(0xF1990, f'toki_opencartouche')
open_cartouche_char.addPosSub("SitelenPonaLookupSubtable", tuple(["bracketleft"]))
importAndCleanOutlines(f'nimi_suli/opencartouche.svg', open_cartouche_char)

close_cartouche_char = font.createChar(0xF1991, f'toki_closecartouche')
close_cartouche_char.addPosSub("SitelenPonaLookupSubtable", tuple(["bracketright"]))
importAndCleanOutlines(f'nimi_suli/closecartouche.svg', close_cartouche_char)

open_long_glyph_char = font.createChar(0xF1997, f'toki_openlongglyph')
open_long_glyph_char.addPosSub("SitelenPonaLookupSubtable", tuple(["parenthesisleft"]))
importAndCleanOutlines(f'nimi_suli/openlongglyph.svg', open_long_glyph_char)

close_long_glyph_char = font.createChar(0xF1998, f'toki_closelongglyph')
close_long_glyph_char.addPosSub("SitelenPonaLookupSubtable", tuple(["parenthesisright"]))
importAndCleanOutlines(f'nimi_suli/closelongglyph.svg', close_long_glyph_char)

for i in NIMI_PI_LAWA_LINJA:
    char = font.createChar(-1, f'toki_{i}_lawa')
    char.addPosSub("LongGlyphLigatureLookupSubtable", tuple([f"toki_{i}", "toki_openlongglyph"]))
    importAndCleanOutlines(f'nimi_suli/{i}_lawa.svg', char)

for (i, j, k) in NIMI_JAN:
    char = font.createChar(-1, f'toki_{i}')
    char.addPosSub("SitelenPonaLookupSubtable", j)
    char.addPosSub("NimiJanLookupSubtable", k)

font.selection.all()
font.autoWidth(150)
open_cartouche_char.right_side_bearing = 0
close_cartouche_char.left_side_bearing = 0
open_long_glyph_char.right_side_bearing = 0
close_long_glyph_char.left_side_bearing = 0

spaceChar = font.createChar(-1, 'space.cart')
spaceChar.width = 0
spaceChar = font.createChar(-1, 'space.cont')
spaceChar.width = 0
spaceChar = font.createChar(0x20, 'space')
spaceChar.width = 0
spaceChar.addPosSub("CartoucheVariantsLookupSubtable", 'space.cart')
spaceChar.addPosSub("LongGlyphVariantsLookupSubtable", 'space.cont')

for i in NIMI_PI_LAWA_LINJA:
    font[f'toki_{i}_lawa'].right_side_bearing = 0

fullSpaceChar = font.createChar(0x3000, 'ideographicspace')
fullSpaceChar.width = FULLWIDTH_SPACE
fullSpaceChar.addPosSub("SitelenPonaLookupSubtable", tuple(["space", "space"]))

for i in EMPTY_GLYPHS:
    font[i].width = 0

for i, j, k in NIMI_JAN:
    font[f'toki_{i}'].width = 0

for i in EMPTY_GLYPHS:
    spaceChar = font.createChar(i, EMPTY_GLYPHS[i])

for i in NIMI_UCSUR:
    char = font.createChar(-1, f'toki_{NIMI_UCSUR[i][0]}.cart')
    glyph_width = font[f'toki_{NIMI_UCSUR[i][0]}'].width

    pen = char.glyphPen()
    pen.addComponent(f'toki_{NIMI_UCSUR[i][0]}')
    pen.moveTo((0, CARTOUCHE_HEIGHT[0]))
    pen.lineTo((0, CARTOUCHE_HEIGHT[1]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[1]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[0]))
    pen.closePath()
    pen.moveTo((0, CARTOUCHE_HEIGHT[2]))
    pen.lineTo((0, CARTOUCHE_HEIGHT[3]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[3]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[2]))
    pen.closePath()
    pen = None

    char.width = glyph_width
    font[f'toki_{NIMI_UCSUR[i][0]}'].addPosSub("CartoucheVariantsLookupSubtable", f'toki_{NIMI_UCSUR[i][0]}.cart')

for (i, j) in NIMI_SIN:
    char = font.createChar(-1, f'toki_{i}.cart')
    glyph_width = font[f'toki_{i}'].width

    pen = char.glyphPen()
    pen.addComponent(f'toki_{i}')
    pen.moveTo((0, CARTOUCHE_HEIGHT[0]))
    pen.lineTo((0, CARTOUCHE_HEIGHT[1]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[1]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[0]))
    pen.closePath()
    pen.moveTo((0, CARTOUCHE_HEIGHT[2]))
    pen.lineTo((0, CARTOUCHE_HEIGHT[3]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[3]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[2]))
    pen.closePath()
    pen = None

    char.width = glyph_width
    font[f'toki_{i}'].addPosSub("CartoucheVariantsLookupSubtable", f'toki_{i}.cart')

for i in NIMI_UCSUR:
    char = font.createChar(-1, f'toki_{NIMI_UCSUR[i][0]}.cont')
    glyph_width = font[f'toki_{NIMI_UCSUR[i][0]}'].width

    pen = char.glyphPen()
    pen.addComponent(f'toki_{NIMI_UCSUR[i][0]}')
    pen.moveTo((0, CARTOUCHE_HEIGHT[0]))
    pen.lineTo((0, CARTOUCHE_HEIGHT[1]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[1]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[0]))
    pen.closePath()
    pen = None

    char.width = glyph_width
    font[f'toki_{NIMI_UCSUR[i][0]}'].addPosSub("LongGlyphVariantsLookupSubtable", f'toki_{NIMI_UCSUR[i][0]}.cont')

for (i, j) in NIMI_SIN:
    char = font.createChar(-1, f'toki_{i}.cont')
    glyph_width = font[f'toki_{i}'].width

    pen = char.glyphPen()
    pen.addComponent(f'toki_{i}')
    pen.moveTo((0, CARTOUCHE_HEIGHT[0]))
    pen.lineTo((0, CARTOUCHE_HEIGHT[1]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[1]))
    pen.lineTo((glyph_width, CARTOUCHE_HEIGHT[0]))
    pen.closePath()
    pen = None

    char.width = glyph_width
    font[f'toki_{i}'].addPosSub("LongGlyphVariantsLookupSubtable", f'toki_{i}.cont')

calt_cart_continue_glyphs = []
calt_cart_start_glyphs = []

for i in NIMI_UCSUR:
    calt_cart_continue_glyphs.append(f'toki_{NIMI_UCSUR[i][0]}.cart')
    calt_cart_start_glyphs.append(f'toki_{NIMI_UCSUR[i][0]}')

for (i, j) in NIMI_SIN:
    calt_cart_continue_glyphs.append(f'toki_{i}.cart')
    calt_cart_start_glyphs.append(f'toki_{i}')

calt_cart_continue_glyphs.append(f'space.cart')
calt_cart_start_glyphs.append(f'space')

calt_cart_continue_glyphs.append(f'toki_opencartouche')
calt_cart_start_glyphs.append(f'toki_closecartouche')

calt_cont_continue_glyphs = []
calt_cont_start_glyphs = []

for i in NIMI_UCSUR:
    calt_cont_continue_glyphs.append(f'toki_{NIMI_UCSUR[i][0]}.cont')
    calt_cont_start_glyphs.append(f'toki_{NIMI_UCSUR[i][0]}')

for (i, j) in NIMI_SIN:
    calt_cont_continue_glyphs.append(f'toki_{i}.cont')
    calt_cont_start_glyphs.append(f'toki_{i}')

calt_cont_continue_glyphs.append(f'space.cont')
calt_cont_start_glyphs.append(f'space')

calt_cont_continue_glyphs.append(f'toki_openlongglyph')
calt_cont_start_glyphs.append(f'toki_closelongglyph')

for i in NIMI_PI_LAWA_LINJA:
    calt_cont_continue_glyphs.append(f'toki_{i}_lawa')

font.addContextualSubtable("CartoucheCaltLookup", "CartoucheCaltLookupSubtable", "coverage", f"[{' '.join(calt_cart_continue_glyphs)}] | [{' '.join(calt_cart_start_glyphs)}] @<CartoucheVariantsLookup>")
font.addContextualSubtable("LongGlyphCaltLookup", "LongGlyphCaltLookupSubtable", "coverage", f"[{' '.join(calt_cont_continue_glyphs)}] | [{' '.join(calt_cont_start_glyphs)}] @<LongGlyphVariantsLookup>")

font.generate(OUTPUTFILENAME)