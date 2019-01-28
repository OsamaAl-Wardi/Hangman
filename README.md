# Hangman
A python3 scripted Hangman that uses an API to acquire its words.

![screenshot from 2019-01-28 14-34-08](https://user-images.githubusercontent.com/34874686/51839726-5721f880-230a-11e9-93ec-cc3608cd6077.png)

## Requirements
- You will need pip3 installed.
```console
user@Osama:~$ sudo apt-get install python3-pip
```
- You will need the random-word modules installed. This can be done in two ways:

```console
user@Osama:~$ easy_install random-word
```
Or

```console
user@Osama:~$ pip install random-word
```
## Basic Usage
```python
from random_word import RandomWords
r = RandomWords()

# Return a single random word
r.get_random_word()
# Return list of Random words
r.get_random_words()
# Return Word of the day
r.word_of_the_day()
```
for more please visit [random-word PyPI](https://pypi.org/project/random-word/).

## What I learned?
- This was just a small game I built in my free time. My intention was to learn how to use the random-word module.
- I was inroduced to the basics natural language processing, semantic similarities and corpus meanings.
## Future Projects
- I believe that creating a maschine learining algorithm and training it solve Hangman would be very interesting. As the data set can be very massive.
## Contact me
You can contact me on [Linkedin](https://www.linkedin.com/in/osamaalwardi/)
