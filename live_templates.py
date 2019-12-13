from pathlib import Path
import html

import lxml.etree


def export(filename):
    """
    https://github.com/hoffmann/PyCharm-Python-Templates
    """
    tree = lxml.etree.parse(open(filename, encoding='utf=8'))
    print('<dl>')
    for template in tree.findall('.//template'):
        print('<dt>%s</dt>' % (html.escape(template.get('name'))))
        print('<dd>%s\n<pre class="prettyprint">%s\n</pre>\n</dd>\n' % (
            template.get('description'), template.get('value')))
    print('</dl>')


def print_live_templates(filename, show_value=False):
    """
    打印本库里面的 Live Templates
    """
    print('=' * 70)
    print(filename)
    tree = lxml.etree.parse(open(filename, encoding='utf=8'))
    for template in tree.findall('.//template'):
        print('-' * 70)
        print(f"Abbreviation: {template.get('name')}")
        print(f"Description: {template.get('description')}")
        if show_value:
            print(f"Template text: \n{template.get('value')}")


if __name__ == '__main__':

    for file in Path('settings/templates').iterdir():
        print_live_templates(file)
