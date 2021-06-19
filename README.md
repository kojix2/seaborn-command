# sns: seaborn as a command line tool

:ocean: [seaborn](https://github.com/mwaskom/seaborn) as a command line tool

<img src="https://user-images.githubusercontent.com/5798442/122654771-9d50ae80-d188-11eb-830e-18a4cf6ad29b.png" alt="seaborn" width="50%" height="50%">

## Installation

```
pip install git+https://github.com/kojix2/sns
```

## Usage

`seaborn` or `sns`

```
seaborn <command> [options]
```

Basic usage

```
cat iris.tsv | seaborn pairplot --hue species --show
```

Input csv file

```
cat iris.tsv | sns pairplot -d, --hue species --show
```

Save image to a file

```
cat iris.tsv | sns pairplot --hue species --format png > result.png
```

* common options
  * `-d` : delimiter (default tab)
  * `--show` : show the GUI window. No output to STDOUT.
  * `--format` : output format of the image (default svg)

## Contributing

* Pull requests are welcome!
