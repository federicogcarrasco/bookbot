# BookBot

*BookBot* is a Python CLI tool that analyzes a text file and provides two pieces of information:

1. The total number of words in the text file.
2. The frequency of each letter (A-Z) in the text.

## Installation

To use *bookbot*, you need Python 3.x installed. You can check if Python is installed by running:

```bash
python3 --version
```

If you don't have Python 3 installed, download and install it from python.org

## Clone the repository

Clone this repository to your local machine:

``` bash
git clone https://github.com/federicogcarrasco/bookbot.git
```

## Usage

You can use the bookbot tool from the command line by passing a relative path to a text file as an argument.

``` bash
python3 bookbot.py <path_to_text_file>
```

## Example

If you have a file called frankenstein.txt in a /books directory, you would run:

``` bash
python3 bookbot.py ./books/frankenstein.txt
```

## Output

The output will display two sections:

1. The total number of words in the text.
2. The frequency of each letter in the text.

Example:

``` bash
--- Begin report of ./books/frankenstein.txt ---

77986 words found in the file.

The E was found 46043 times.
The T was found 30365 times.
The A was found 26743 times.
The O was found 25225 times.
The I was found 24613 times.
The N was found 24367 times.
The S was found 21155 times.
The R was found 20818 times.
The H was found 19725 times.
The D was found 16863 times.
The L was found 12739 times.
The M was found 10604 times.
The U was found 10407 times.
The C was found 9243 times.
The F was found 8731 times.
The Y was found 7914 times.
The W was found 7638 times.
The P was found 6121 times.
The G was found 5974 times.
The B was found 5026 times.
The V was found 3833 times.
The K was found 1755 times.
The X was found 677 times.
The J was found 504 times.
The Q was found 324 times.
The Z was found 243 times.

--- End report ---
```
