from verify import app as verify
from split import app as split
import sys

args = sys.argv[1:]
module = args[0]
options = args[1:]
verbose = True if "-v" in options else False

if module == "verify":
    exit(verify.execute(options, verbose))
elif module == "split":
    exit(split.execute(options, verbose))
else:
    raise Exception("Invalid module specified")
