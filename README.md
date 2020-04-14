# mp3-dl-tagger

[![works badge](https://cdn.rawgit.com/nikku/works-on-my-machine/v0.2.0/badge.svg)](https://github.com/nikku/works-on-my-machine)

A Python script that downloads audio from a given youtube url (optional), lets user edit tags and changes filename according to tags.


# Dependencies
Note: Use pip to download the dependencies, it may not work the other way

* [youtube-dl](https://github.com/rg3/youtube-dl/)
* [mutagen](https://github.com/quodlibet/mutagen)
* [TkInter](https://wiki.python.org/moin/TkInter)

# Usage
```python main.py [youtube url]``` to download audio from Youtube and edit tags.

```python main.py``` to open local file and edit tags.

__This script needs to be run with Python3!__

You can also use ```alias ymp3="python [pathtoscript]"```, for example, ```alias ymp3="python ~/Documents/mp3-dl-tagger/main.py"```. And then ```ymp3 [youtubeurl]```. Thanks to [RaitaroH](https://github.com/RaitaroH) for the idea.

# Troubleshooting
## youtube-dl

Sometimes there is some trouble with youtube-dl. This is due to confusion between Python 2 and 3. If the method given in youtube-dl doesn't work, try:
```pip install youtube_dl```

If it doesn't work try:
```pip3 install youtube_dl```

## Windows

This script does not work on Windows. After installing all the modules and running it, tkinter file dialog does not work. If someone knows how to fix it, I appreciate it. Otherwise, it works on Linux!
