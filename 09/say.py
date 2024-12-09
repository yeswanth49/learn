from sayings import hello
from sayings import good_bye

import sys

if len(sys.argv) ==3:
    hello(sys.argv[1])
    good_bye(sys.argv[2])
