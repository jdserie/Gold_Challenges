# Python Gold Badge exercises

Three Eleven Fifty Academy exercises by Joshua Serie. They demonstrate terminal input, repository-style Python modules, a first-in-first-out claims queue, and calculations over records.

| Exercise | Run from the repository root |
| --- | --- |
| Café menu | `python Challenge_1_of_8/cafe.py` |
| Claims queue | `python Challenge_2_of_8/claim.py` |
| Outing costs | `python Challenge_3_of_8/outing.py` |

Use Python 3.10 or newer. The apps store records in memory for the current run.

## Verify

```sh
python -m unittest discover -s Challenge_1_of_8
python -m unittest discover -s Challenge_2_of_8
python -m unittest discover -s Challenge_3_of_8
```

The [original coursework](https://github.com/jdserie/Gold_Challenges/commit/4640538d7259bcec2b4689169d5301ad923fdb1c) is dated February 22, 2019. The AI-assisted portfolio refresh fixes the record lookup and input handling and makes the tests independent.
