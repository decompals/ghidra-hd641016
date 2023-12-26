#!/usr/bin/env python3
import pathlib

import pytest
from pypcode import Arch, Context, PcodePrettyPrinter


@pytest.fixture(scope="module")
def context():
    lang = Arch(
        "hd641016:BE:32:default",
        str(pathlib.Path(__file__).parent / "data" / "languages" / "hd641016.ldefs"),
    )
    return Context(lang.languages[0])


def test_mov_q(context: Context):
    disasm = context.disassemble(b"\x2e\x91", 0x116E)
    assert len(disasm.instructions) == 1
    assert disasm.instructions[0].mnem == "MOV.L"
    assert disasm.instructions[0].body == "R9, R1"
