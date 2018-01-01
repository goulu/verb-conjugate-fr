# verb-conjugate-fr
Python French verb conjugation / Conjugaison des verbes français en Python

* Unit tested
* [Travis CI](https://www.travis-ci.org/bretttolbert/verb-conjugate-fr) ![Travis CI build status](https://travis-ci.org/bretttolbert/verb-conjugate-fr.svg?branch=master) 
* Currently under development, some tenses not yet implemented
* Has a command line interface

Build with setup.py or use tox to build (both py27 and p36) and run unit tests and linters.

API demo:
```
In [1]: from verb_conjugate_fr.conjugator import Conjugator

In [2]: conj = Conjugator()
Loaded 7000 verbs
Loaded 132 conjugation templates

In [3]: conj.conjugate('manger')
Conjugaison du verbe "manger":
Conjugation template: man:ger
Out[3]: 
{'moods': {'indicative': {'future': ['je mangerai',
    'tu mangeras',
    'il mangera',
    'nous mangerons',
    'vous mangerez',
    'ils mangeront'],
   'imperfect': ['je mangeais',
    'tu mangeais',
    'il mangeait',
    'nous mangions',
    'vous mangiez',
    'ils mangeaient'],
   'present': ['je mange',
    'tu manges',
    'il mange',
    'nous mangeons',
    'vous mangez',
    'ils mangent'],
   'simple-past': ['je mangeai',
    'tu mangeas',
    'il mangea',
    'nous mangeâmes',
    'vous mangeâtes',
    'ils mangèrent']}}}

```

CLI demo:

```
$ sudo apt-get install python-dev
$ tox
...
$ source .py3/bin/activate
(.py3) brett@ubuntu:~/Git/verb-conjugate-fr$ confr manger
Loaded 7000 verbs
Loaded 132 conjugation templates
Conjugaison du verbe manger
Template: man:ger

present
je mange
tu manges
il mange
nous mangeons
vous mangez
ils mangent


imperfect
je mangeais
tu mangeais
il mangeait
nous mangions
vous mangiez
ils mangeaient


future
je mangerai
tu mangeras
il mangera
nous mangerons
vous mangerez
ils mangeront


simple-past
je mangeai
tu mangeas
il mangea
nous mangeâmes
vous mangeâtes
ils mangèrent


Entrez un mot français pour conjuguer
Enter a French verb to conjugate
foo
Aucune mot trouvé
Verb not found
No matches
Entrez un mot français pour conjuguer
Enter a French verb to conjugate
cro
Aucune mot trouvé
Verb not found
Matches:
croasser
crocher
crocheter
crochir
croire
croiser
croquer
crosser
crotter
crouler
croupir
croustiller
croître
croûter
Entrez un mot français pour conjuguer
Enter a French verb to conjugate
```
