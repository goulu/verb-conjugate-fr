# -*- coding: utf-8 -*-

from mock import patch

import pytest

from verb_conjugate_fr.conjugation_template import (
    ConjugationTemplate, ConjugationTemplateError
)
from verb_conjugate_fr.conjugations_parser import (
    ConjugationsParser, ConjugationsParserError
)


def test_conjugations_parser():
    conj = ConjugationsParser()
    assert len(conj.templates) >= 132


@patch('lxml.etree._Element')
def test_TemplateInvalidXML(mock_template_elem):
    mock_template_elem.tag.return_value = "not-template"
    with pytest.raises(ConjugationTemplateError):
        template = ConjugationTemplate(mock_template_elem)
