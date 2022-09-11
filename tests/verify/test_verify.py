import sys

sys.path.append("../../pdf_tools")

from pdf_tools.verify import app as verify
import pathlib

pdfs = f"{pathlib.Path(__file__).parent.parent.resolve()}/pdfs"


class Tests:
    def test_valid_pdf(self):
        file = f"{pdfs}/valid.pdf"
        args = [file]
        valid = verify.execute(args, False)
        assert valid == 0

    def test_invalid_pdf(self):
        path = pathlib.Path(__file__).parent.resolve()
        file = f"{pdfs}/invalid.pdf"
        args = [file]
        valid = verify.execute(args, False)
        assert valid == 1
