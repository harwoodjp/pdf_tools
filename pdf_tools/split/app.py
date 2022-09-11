from typing import List

import ghostscript
from subprocess import run, DEVNULL, PIPE


def execute(args: List[str], verbose: bool) -> int:
    if len(args) < 3:
        raise Exception(
            "Insufficient arguments provided: need [input.pdf] [output_dir] [png|pdf]"
        )

    file_path = args[0]
    output_dir = args[1]
    output_format = args[2]

    if output_format not in ["pdf", "png"]:
        raise Exception("Unrecognized output format")

    output_dir = output_dir[0:-1] if output_dir[-1] == "/" else output_dir
    file = file_path.split("/")[-1]
    file_has_extension = file[len(file) - 4 : :] == ".pdf"
    output_file_prefix = file[0 : len(file) - 4] if file_has_extension else file

    command = ""
    if output_format == "png":
        command = f"gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r300 -dDownScaleFactor=3 -sOutputFile={output_dir}/{output_file_prefix}_%d.png {file_path}"
    else:
        command = f"gs -o {output_dir}/{output_file_prefix}_%d.pdf -sDEVICE=pdfwrite {file_path}"

    result = run(command, shell=True, stdout=PIPE, stderr=PIPE)

    if result.returncode == 0:
        print("PDF split succeeded")
        if verbose:
            print(result.args)
            print(result.stdout)
    else:
        print(f"PDF split failed. Add -v flag for details")

    return result.returncode
