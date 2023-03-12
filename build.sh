#!/bin/bash
# requires:
# python
# pandoc
# jq

function output_filename() {
  basename $1 | sed "s/\..*//g"
}

function buildDoc() {
  # TODO: the way $output is used is gonna be finicky
  # better to default it
  outfile=docs/$3`output_filename $1`.html
  mkdir -p `dirname $outfile`
  pandoc --mathjax \
    --template ./template/template.html \
    --metadata title="$2" \
    -o $outfile \
    -t "html" \
    "$1"
}

while read -r line; do
  path=`echo $line | jq -r ".path"`
  title=`echo $line | jq -r ".title"`
  output="`echo $line | jq -r ".output // empty"`"
  buildDoc "$path" "$title" "$output"
done < <(cat ./docs.json | jq -c ".[]")

# css mathjax etc
cp -r static docs/

# create an index file in the root
python ./makeIndex.py > docs/index.html
