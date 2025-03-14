![Version](https://img.shields.io/github/v/release/DCMLab/bach_solo?display_name=tag)
[![DOI](https://zenodo.org/badge/335588828.svg)](https://doi.org/10.5281/zenodo.14996765)
![GitHub repo size](https://img.shields.io/github/repo-size/DCMLab/bach_solo)
![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-9cf)


This is a README file for a data repository originating from the [DCML corpus initiative](https://github.com/DCMLab/dcml_corpora)
and serves as welcome page for both 

* the GitHub repo [https://github.com/DCMLab/bach_solo](https://github.com/DCMLab/bach_solo) and the corresponding
* documentation page [https://dcmlab.github.io/bach_solo](https://dcmlab.github.io/bach_solo)

For information on how to obtain and use the dataset, please refer to [this documentation page](https://dcmlab.github.io/bach_solo/introduction).

# J.S. Bach – Solo Pieces (A corpus of annotated scores)

All of the works in this repository are essential standard repertoire for their respective instruments. With the
possible exception of BWV 1013, all were composed during Bach's prolific period as Kapellmeister in Köthen. Despite
their ubiquity, their composition is shrouded in a kind of prophetic mystery; the Sonatas and Partitas for Solo Violin
were only published in 1802, the Partita for Solo Flute was completely unknown until the twentieth century, and the
Suites for Solo Cello were virtually unplayable on the instruments of the time. These works are outstanding for the
sheer melodic and figurative variety they introduce to their ostensibly 'fixed' Baroque dance forms and our analyses
will be able to substantiate broad new stylistic interpretations of this music.

## Getting the data

* download repository as a [ZIP file](https://github.com/DCMLab/bach_solo/archive/main.zip)
* download a [Frictionless Datapackage](https://specs.frictionlessdata.io/data-package/) that includes concatenations
  of the TSV files in the four folders (`measures`, `notes`, `chords`, and `harmonies`) and a JSON descriptor:
  * [bach_solo.zip](https://github.com/DCMLab/bach_solo/releases/latest/download/bach_solo.zip)
  * [bach_solo.datapackage.json](https://github.com/DCMLab/bach_solo/releases/latest/download/bach_solo.datapackage.json)
* clone the repo: `git clone https://github.com/DCMLab/bach_solo.git` 


## Data Formats

Each piece in this corpus is represented by five files with identical name prefixes, each in its own folder. 
For example, the first movement of the Violin Sonata No.1 in G minor has the following files:

* `MS3/BWV1001_01_Adagio.mscx`: Uncompressed MuseScore 3.6.2 file including the music and annotation labels.
* `notes/BWV1001_01_Adagio.notes.tsv`: A table of all note heads contained in the score and their relevant features (not each of them represents an onset, some are tied together)
* `measures/BWV1001_01_Adagio.measures.tsv`: A table with relevant information about the measures in the score.
* `chords/BWV1001_01_Adagio.chords.tsv`: A table containing layer-wise unique onset positions with the musical markup (such as dynamics, articulation, lyrics, figured bass, etc.).
* `harmonies/BWV1001_01_Adagio.harmonies.tsv`: A table of the included harmony labels (including cadences and phrases) with their positions in the score.

Each TSV file comes with its own JSON descriptor that describes the meanings and datatypes of the columns ("fields") it contains,
follows the [Frictionless specification](https://specs.frictionlessdata.io/tabular-data-resource/),
and can be used to validate and correctly load the described file. 

### Opening Scores

After navigating to your local copy, you can open the scores in the folder `MS3` with the free and open source score
editor [MuseScore](https://musescore.org). Please note that the scores have been edited, annotated and tested with
[MuseScore 3.6.2](https://github.com/musescore/MuseScore/releases/tag/v3.6.2). 
MuseScore 4 has since been released which renders them correctly but cannot store them back in the same format.

### Opening TSV files in a spreadsheet

Tab-separated value (TSV) files are like Comma-separated value (CSV) files and can be opened with most modern text
editors. However, for correctly displaying the columns, you might want to use a spreadsheet or an addon for your
favourite text editor. When you use a spreadsheet such as Excel, it might annoy you by interpreting fractions as
dates. This can be circumvented by using `Data --> From Text/CSV` or the free alternative
[LibreOffice Calc](https://www.libreoffice.org/download/download/). Other than that, TSV data can be loaded with
every modern programming language.

### Loading TSV files in Python

Since the TSV files contain null values, lists, fractions, and numbers that are to be treated as strings, you may want
to use this code to load any TSV files related to this repository (provided you're doing it in Python). After a quick
`pip install -U ms3` (requires Python 3.10 or later) you'll be able to load any TSV like this:

```python
import ms3

labels = ms3.load_tsv("harmonies/BWV1001_01_Adagio.harmonies.tsv")
notes = ms3.load_tsv("notes/BWV1001_01_Adagio.notes.tsv")
```


## Version history

See the [GitHub releases](https://github.com/DCMLab/bach_solo/releases).

## Questions, Suggestions, Corrections, Bug Reports

Please [create an issue](https://github.com/DCMLab/bach_solo/issues) and/or feel free to fork and submit pull requests.

## Cite as

> Johannes Hentschel, Yannis Rammos, Markus Neuwirth, & Martin Rohrmeier. (2025). J.S. Bach – Solo Pieces (A corpus of annotated scores) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.14996765

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)).

![cc-by-nc-sa-image](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

## File naming convention

```regex
BWV(?<bwv>\d{4})_
(?<no>\d{2}a?)_
(?<movement>\S+)?
```

## Overview
|        file_name         |measures|labels|standard| annotators |
|--------------------------|-------:|-----:|--------|------------|
|BWV1001_01_Adagio         |      22|    95|2.3.0   |Adrian Nagel|
|BWV1001_02_Fuga           |      94|   324|2.3.0   |Adrian Nagel|
|BWV1001_03_Siciliano      |      20|   113|2.3.0   |Adrian Nagel|
|BWV1001_04_Presto         |     136|   213|2.3.0   |Adrian Nagel|
|BWV1002_01_Allemanda      |      24|    97|2.3.0   |Adrian Nagel|
|BWV1002_02_Double         |      24|    87|2.3.0   |Adrian Nagel|
|BWV1002_03_Corrente       |      80|   109|2.3.0   |Adrian Nagel|
|BWV1002_04_Double         |      80|   121|2.3.0   |Adrian Nagel|
|BWV1002_05_Sarabande      |      32|    68|2.3.0   |Adrian Nagel|
|BWV1002_06_Double         |      32|    56|2.3.0   |Adrian Nagel|
|BWV1002_07_TempoDiBorea   |      68|   101|2.3.0   |Adrian Nagel|
|BWV1002_08_Double         |      68|   104|2.3.0   |Adrian Nagel|
|BWV1003_01_Grave          |      23|    91|2.3.0   |Adrian Nagel|
|BWV1003_02_Fuga           |     289|   479|2.3.0   |Adrian Nagel|
|BWV1003_03_Andante        |      26|    79|2.3.0   |Adrian Nagel|
|BWV1003_04_Allegro        |      58|   206|2.3.0   |Adrian Nagel|
|BWV1004_01_Allemande      |      32|    92|2.3.0   |Adrian Nagel|
|BWV1004_02_Courante       |      54|    73|2.3.0   |Adrian Nagel|
|BWV1005_02_Fuga           |     354|   748|2.3.0   |Adrian Nagel|
|BWV1006_04_Menuett        |      66|   124|2.3.0   |Adrian Nagel|
|BWV1006_05_Bourée         |      36|    57|2.3.0   |Adrian Nagel|
|BWV1006_06_Gigue          |      32|    52|2.3.0   |Adrian Nagel|
|BWV1007_01_Prelude        |      42|    54|2.3.0   |Adrian Nagel|
|BWV1007_02_Allemande      |      32|    75|2.3.0   |Adrian Nagel|
|BWV1007_03_Courante       |      42|    66|2.3.0   |Adrian Nagel|
|BWV1007_04_Sarabande      |      16|    43|2.3.0   |Adrian Nagel|
|BWV1007_05_MenuetI        |      24|    35|2.3.0   |Adrian Nagel|
|BWV1007_06_MenuetII       |      24|    33|2.3.0   |Adrian Nagel|
|BWV1007_07_Gique          |      34|    59|2.3.0   |Adrian Nagel|
|BWV1008_01_Prelude        |      63|    91|2.3.0   |Adrian Nagel|
|BWV1008_02_Allemande      |      24|    70|2.3.0   |Adrian Nagel|
|BWV1008_03_Courante       |      32|    50|2.3.0   |Adrian Nagel|
|BWV1008_04_Sarabande      |      28|    52|2.3.0   |Adrian Nagel|
|BWV1008_05_MenuetI        |      24|    44|2.3.0   |Adrian Nagel|
|BWV1008_06_MenuetII       |      24|    31|2.3.0   |Adrian Nagel|
|BWV1008_07_Gique          |      76|    91|2.3.0   |Adrian Nagel|
|BWV1009_01_Prelude        |      88|   113|2.3.0   |Adrian Nagel|
|BWV1009_02_Allemande      |      24|   106|2.3.0   |Adrian Nagel|
|BWV1009_03_Courante       |      84|    83|2.3.0   |Adrian Nagel|
|BWV1009_04_Sarabande      |      24|    55|2.3.0   |Adrian Nagel|
|BWV1009_05_BourréeI       |      28|    64|2.3.0   |Adrian Nagel|
|BWV1009_06_BourréeII      |      24|    36|2.3.0   |Adrian Nagel|
|BWV1009_07_Gique          |     108|   110|2.3.0   |Adrian Nagel|
|BWV1010_01_Prelude        |      91|    75|2.3.0   |Adrian Nagel|
|BWV1010_02_Allemande      |      40|    97|2.3.0   |Adrian Nagel|
|BWV1010_03_Courante       |      64|   106|2.3.0   |Adrian Nagel|
|BWV1010_04_Sarabande      |      32|    65|2.3.0   |Adrian Nagel|
|BWV1010_05_BourreeI       |      48|    78|2.3.0   |Adrian Nagel|
|BWV1010_06_BourreeII      |      12|    28|2.3.0   |Adrian Nagel|
|BWV1010_07_Gique          |      42|    80|2.3.0   |Adrian Nagel|
|BWV1011_01_Prelude        |     223|   327|2.3.0   |Adrian Nagel|
|BWV1011_02_Allemande      |      36|    70|2.3.0   |Adrian Nagel|
|BWV1011_03_Courante       |      24|    68|2.3.0   |Adrian Nagel|
|BWV1011_04_Sarabande      |      20|    27|2.3.0   |Adrian Nagel|
|BWV1011_05_GavotteI       |      36|    80|2.3.0   |Adrian Nagel|
|BWV1011_06_GavotteII      |      22|    65|2.3.0   |Adrian Nagel|
|BWV1011_07_Gique          |      72|    73|2.3.0   |Adrian Nagel|
|BWV1012_01_Prelude        |     104|   189|2.3.0   |Adrian Nagel|
|BWV1012_02_Allemande      |      20|    80|2.3.0   |Adrian Nagel|
|BWV1012_03_Courante       |      72|    90|2.3.0   |Adrian Nagel|
|BWV1012_04_Sarabande      |      32|    61|2.3.0   |Adrian Nagel|
|BWV1012_05_GavotteI       |      28|    58|2.3.0   |Adrian Nagel|
|BWV1012_06_GavotteII      |      24|    64|2.3.0   |Adrian Nagel|
|BWV1012_07_Gique          |      68|   112|2.3.0   |Adrian Nagel|
|BWV1013_01_Allemande      |      46|   163|2.3.0   |Adrian Nagel|
|BWV1013_02_Corrente       |      62|   120|2.3.0   |Adrian Nagel|
|BWV1013_03_Sarabande      |      46|    57|2.3.0   |Adrian Nagel|
|BWV1013_04_BourreeAnglaise|      70|    98|2.3.0   |Adrian Nagel|


*Overview table automatically updated using [ms3](https://ms3.readthedocs.io/).*
