from codepenget.utils import get_code
import sys
import os
import shutil


def download():
    if len(sys.argv) == 1:
        print('Usage: codepenget <url_to_pen>')
        return None

    print('Downloading...')
    code = get_code(sys.argv[1])

    if os.path.isdir('component'):
        shutil.rmtree('component')
    
    os.mkdir('component')

    if 'css' in code:
        with open('component/component.css', 'w+') as cfile:
            cfile.write(code['css'])
        cfile.close()

    if 'js' in code:
        with open('component/component.js', 'w+') as cfile:
            cfile.write(code['js'])
        cfile.close()

    if 'html' in code:
        with open('component/component.html', 'w+') as cfile:
            cfile.write(code['html'])
        cfile.close()

    print('Done')
