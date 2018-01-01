# -*- coding: utf-8 -*-

from lxml import etree

from verb_conjugate_fr.person_ending import PersonEnding
from verb_conjugate_fr.tense_template import TenseTemplate


def test_tense_and_person():
    tense_elem = etree.fromstring(
        u"""<present>
        <p><i>ie</i><i>ye</i></p>
        <p><i>ies</i><i>yes</i></p>
        <p><i>ie</i><i>ye</i></p>
        <p><i>yons</i></p>
        <p><i>yez</i></p>
        <p><i>ient</i><i>yent</i></p>
        </present>""")
    tense_name = 'present'
    tense = TenseTemplate(tense_name, tense_elem)
    assert tense.name == tense_name
    assert tense.persons[0].get_ending() == "ie"
    assert tense.persons[0].get_alternate_ending() == "ye"
    assert tense.persons[3].get_ending() == "yons"
    assert tense.persons[3].get_alternate_ending() is None
    assert tense.get_person_ending_by_pronoun('je').get_ending() == 'ie'
    assert tense.get_person_ending_by_pronoun('tu').get_ending() == 'ies'
    assert tense.get_person_ending_by_pronoun('elle').get_ending() == 'ie'
    assert tense.get_person_ending_by_pronoun('nous').get_ending() == 'yons'
    assert tense.get_person_ending_by_pronoun('vous').get_ending() == 'yez'
    assert tense.get_person_ending_by_pronoun('ils').get_ending() == 'ient'
    assert tense.get_person_ending_by_pronoun('on') \
        == tense.get_person_ending_by_pronoun('il') \
        == tense.get_person_ending_by_pronoun('elle')
    third_person_sing_ending = tense.get_person_ending_by_pronoun('on')
    assert third_person_sing_ending.get_ending() == 'ie'
    assert third_person_sing_ending.get_alternate_ending() == 'ye'
