import os.path

FILENAME = "nestle1904.csv"
FIELD_NAMES = ("ref", "text", "parse1", "parse2", "strongs", "lemma", "norm")

def nestle_rows():
    """
    yield a dict for each Nestle 1904 row.
    """
    with open(os.path.join(os.path.dirname(__file__), FILENAME)) as f:
        for line in f:
            yield dict(zip(FIELD_NAMES, line.strip().split("\t")))
