# py-nestle1904

Like py-sblgnt does for the MorphGNT SBLGNT, **py-nestle1904** provides a pip-installable package that combines the Nestle 1904 text with morphology and lemmatisation and a Python API for accessing it.

This way, Python tools built on the Nestle 1904 can include **py-nestle1904** as a requirement to be installed globally or into a virtualenv and no other set up is necessary.

Note that, even though this repo and package contain the Nestle 1904 database, the [Nestle 1904 repo](https://github.com/biblicalhumanities/Nestle1904) remains the authoritative source of the data and all data corrections should be reported there.

All credit for the data belongs to those people acknowledged there.


## How to Use

Firstly, install with

```
pip install py-nestle1904
```

Then in your code...

```
from pynestle1904 import nestle_rows

for row in nestle_rows():
    ...
```

Each `row` will be a dictionary with the keys:

```
"ref", "text", "parse1", "parse2", "strongs", "lemma", "norm"
```

See the [Nestle 1904 repo](https://github.com/biblicalhumanities/Nestle1904) for details of these fields.

## License

The text and data is in the Public Domain.

The code here is made available under an MIT License.
