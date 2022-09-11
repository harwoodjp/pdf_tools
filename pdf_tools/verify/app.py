from typing import List

import ghostscript # type: ignore
from subprocess import CompletedProcess, run, DEVNULL, PIPE


def execute(args: List[str], verbose: bool) -> int:
    if len(args) < 1:
        raise Exception("Insufficient arguments provided")

    file: str = args[0]
    command: str = f"gs -o /dev/null -sDEVICE=nullpage -dBATCH -dNOPAUSE {file}"
    result: CompletedProcess = run(command, shell=True, stdout=PIPE, stderr=PIPE)

    if result.returncode == 0:
        print("Valid PDF")
        if verbose:
            print(result.args)
            print(result.stdout)
    else:
        print(f"Invalid PDF. Add -v flag for details")

    return result.returncode
