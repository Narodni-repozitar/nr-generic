# nr-common

[![Build Status](https://travis-ci.org/Narodni-repozitar/nr-common.svg?branch=master)](https://travis-ci.org/Narodni-repozitar/nr-common)
[![Coverage Status](https://coveralls.io/repos/github/Narodni-repozitar/nr-common/badge.svg)](https://coveralls.io/github/Narodni-repozitar/nr-common)

Disclaimer: The library is part of the Czech National Repository, and therefore the README is written in Czech.
General libraries extending [Invenio](https://github.com/inveniosoftware) are concentrated under the [Oarepo
 namespace](https://github.com/oarepo).
 
 ## Instalace
 
 Nejedná se o samostatně funkční knihovnu, proto potřebuje běžící Invenio a závislosti Oarepo.
 Knihovna se instaluje klasicky přes pip
 
```bash
pip install techlib-nr-common
```

Pro testování a/nebo samostané fungování knihovny je nutné instalovat tests z extras.

```bash
pip install -e .[tests]
```

## Účel

Knihovna obsahuje REST api pro obecný metadatový model definovaný v nr-generic.