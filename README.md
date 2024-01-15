# vereqsyn

[![PyPI - Version](https://img.shields.io/pypi/v/vereqsyn.svg)](https://pypi.org/project/vereqsyn)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vereqsyn.svg)](https://pypi.org/project/vereqsyn)

Bi-directional version.cfg <–> requirements.txt synchronization

-----

**Table of Contents**

- [Installation](#installation)
- [Constraints](#constraints)
- [License](#license)

## Installation

```console
pip install vereqsyn
```

## Constraints

* `version.cfg` is the source of truth. `requirements.txt` can get recreated.
* So `version.cfg` can contain comments, the ones in `requirements.txt` are
  lost when running recreate.

## License

`vereqsyn` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
