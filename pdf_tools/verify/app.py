from typing import List

import ghostscript
from subprocess import run, DEVNULL, PIPE


def execute(args: List[str], verbose: bool) -> bool:
    if len(args) < 1:
        raise Exception("Insufficient arguments provided")

    file = args[0]
    command = f"gs -o /dev/null -sDEVICE=nullpage -dBATCH -dNOPAUSE {file}"
    result = run(command, shell=True, stdout=PIPE, stderr=PIPE)

    if result.returncode == 0:
        print("Valid PDF")
        if verbose:
            print(result.args)
            print(result.stdout)
    else:
        print(f"Invalid PDF. Add -v flag for details")

    return result.returncode
