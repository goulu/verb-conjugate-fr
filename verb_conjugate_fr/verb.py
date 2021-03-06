# -*- coding: utf-8 -*-

from lxml import etree


class VerbsParserError(SyntaxError):
    pass


class Verb:
    def __init__(self, v_elem):
        if v_elem.tag != 'v':
            raise VerbsParserError("parse_verb: not a 'v' elem")
        try:
            self.infinitive = u'' + v_elem.find('i').text
            self.template = u'' + v_elem.find('t').text
            self.translation_en = u'' + v_elem.find('en').text
        except AttributeError as e:
            raise VerbsParserError(
                "Error parsing {}: {}".format(
                    etree.tostring(v_elem),
                    str(e)))
