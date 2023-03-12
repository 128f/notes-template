### Notes

I've been keeping a folder full of `notes`, markdown files containing snippets of code and math. I wanted to use `pandoc` to convert them into simple html files.

This repo has a number of components you should know about

* `docs.json` - a json document containing information about which files to render into html
* `build.sh` - a shell script that calls pandoc for each item in `docs.json`
* `makeIndex.py` - create an `index.py` file using `yattag`, this is called from build.sh
* `serve.py` - run a local webserver serving the output directory

Included is a basic `docs.json` file and a set of example notes.

[See the result here](https://cr0ax.github.io/notes-template/)
