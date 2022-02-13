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
cat iris.tsv | seaborn pairplot --hue species
```

Input csv file

```
cat iris.csv | seaborn pairplot -H -d, --hue species
```

Save svg image to a file

```
cat iris.tsv | seaborn pairplot --hue species > result.svg
```

Show png image with ImageMagick

```
cat iris.tsv | seaborn pairplot --hue species --format png | display
```

* common options
  * `-d` : delimiter (default tab)
  * `-t` : transpose
  * `--format` : output format of the image (default svg)

### Tips

Setting alias

```
alias sns="seaborn"
```

[viu](https://github.com/atanunq/viu) command. 

```
cat iris.tsv | seaborn pairplot --hue species --format png | viu -
```

Note:
* SVG images may not be displayed correctly. 
* viu + [kitty](https://github.com/kovidgoyal/kitty) terminal will work even if you are accessing it via ssh.

## Contributing

* Try this command!
* Pull requests are welcome!

```
Do you need commit rights to my repository?
Do you want to get admin rights and take over the project?
If so, please feel free to contact @kojix2.
```

## License

MIT
