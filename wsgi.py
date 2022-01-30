from os.path import dirname, abspath, join
import sys

# Find code directory relative to our directory
THIS_DIR = dirname(__file__)
CODE_DIR = abspath(join(THIS_DIR, 'app'))
sys.path.append(CODE_DIR)
print(CODE_DIR)

from cii import app

if __name__ == '__main__':
    app.run()
