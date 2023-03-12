from yattag.doc import Doc
import os
import json


def generateIndex(items):
    doc, tag, text, line = Doc().ttl()
    with tag('html'):
        doc.stag("link", rel="stylesheet", href="static/style.css")
        with tag('body'):
            with tag('div', id="index"):
                for link in items:
                    if "output" in link:
                        continue
                    path = os.path.basename(link["path"]).replace('.md', "")
                    line("a", link["title"], klass="index-link", href=path)
    return doc

with open('./docs.json', 'r') as file:
    content = json.load(file)
    print(generateIndex(content).getvalue())

