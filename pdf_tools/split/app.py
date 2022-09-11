from typing import List

import ghostscript # type: ignore
from subprocess import CompletedProcess, run, DEVNULL, PIPE


def execute(args: List[str], verbose: bool) -> int:
    if len(args) < 3:
        raise Exception(
            "Insufficient arguments provided: need [input.pdf] [output_dir] [png|pdf]"
        )

    file_path: str = args[0]
    output_dir: str = args[1]
    output_format: str = args[2]

    if output_format not in ["pdf", "png"]:
        raise Exception("Unrecognized output format")

    output_dir = output_dir[0:-1] if output_dir[-1] == "/" else output_dir
    file: str = file_path.split("/")[-1]
    file_has_extension: bool = file[len(file) - 4 : :] == ".pdf"
    output_file_prefix: str = file[0 : len(file) - 4] if file_has_extension else file

    command: str = ""
    if output_format == "png":
        command = f"gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r300 -dDownScaleFactor=3 -sOutputFile={output_dir}/{output_file_prefix}_%d.png {file_path}"
    else:
        command = f"gs -o {output_dir}/{output_file_prefix}_%d.pdf -sDEVICE=pdfwrite {file_path}"

    result: CompletedProcess = run(command, shell=True, stdout=PIPE, stderr=PIPE)

    if result.returncode == 0:
        print("PDF split succeeded")
        if verbose:
            print(result.args)
            print(result.stdout)
    else:
        print(f"PDF split failed. Add -v flag for details")
        if verbose:
            print(result.args)
            print(result.stdout)

    return result.returncode
