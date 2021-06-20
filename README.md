# seaborn-command

[![PyPI Version](https://img.shields.io/pypi/v/seaborn-command.svg)](https://pypi.org/project/seaborn-command/)
[![CI](https://github.com/kojix2/seaborn-command/actions/workflows/ci.yaml/badge.svg)](https://github.com/kojix2/seaborn-command/actions/workflows/ci.yaml)

:ocean: [seaborn](https://github.com/mwaskom/seaborn) as a command line tool

<img src="https://user-images.githubusercontent.com/5798442/122654771-9d50ae80-d188-11eb-830e-18a4cf6ad29b.png" alt="seaborn" width="50%" height="50%">

## Installation

```
pip install seaborn-command
```

## Usage

```
seaborn <command> [options]
```

Basic usage

```
cat iris.tsv | seaborn pairplot --hue species --show
```

Input csv file

```
cat iris.csv | seaborn pairplot -d, --hue species --show
```

Save image to a file

```
cat iris.tsv | seaborn pairplot --hue species --format png > result.png
```

* common options
  * `-d` : delimiter (default tab)
  * `--show` : show the GUI window. No output to STDOUT.
  * `--format` : output format of the image (default svg)

### Tips

Setting alias

```
alias sns="seaborn"
```

Display with ImageMagick

```
cat iris.tsv | seaborn pairplot --hue species --format png | display
```

Note: SVG images may not be displayed correctly.

## Contributing

* Try this command!
* Pull requests are welcome!

## LICENSE

MIT
