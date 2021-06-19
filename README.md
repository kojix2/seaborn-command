# sns: seaborn as a command line tool

:ocean: [seaborn](https://github.com/mwaskom/seaborn) as a command line tool

## Installation

```
pip install git+https://github.com/kojix2/sns
```

## Usage

```
cat iris.tsv | seaborn pairplot --hue species --show
```

* Options
  * `-d` : delimiter
  * `-show` : show window

csv file

```
cat iris.tsv | sns pairplot -d, --hue species --show
```

save image

```
cat iris.tsv | sns pairplot --hue species --format png > result.png
```

## Contributing

* Pull requests are welcome!
