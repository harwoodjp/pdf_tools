from typing import List
from verify import app as verify
from split import app as split
import sys

args: List[str] = sys.argv[1:]
module: str = args[0]
options: List[str] = args[1:]
verbose: bool = True if "-v" in options else False

if module == "verify":
    exit(verify.execute(options, verbose))
elif module == "split":
    exit(split.execute(options, verbose))
else:
    raise Exception("Invalid module specified")
