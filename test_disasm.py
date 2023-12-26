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


def test_mov_b(context: Context):
    disasm = context.disassemble(b"\x0c\x50\x51", 0xDB4)
    assert len(disasm.instructions) == 1
    assert disasm.instructions[0].mnem == "MOV.B"
    assert disasm.instructions[0].body == "@R0+, @R1+"


def test_ldm(context: Context):
    disasm = context.disassemble(b"\x76\x5F\x00\x03", 0xDB9)
    assert len(disasm.instructions) == 1
    assert disasm.instructions[0].mnem == "LDM.L"
    assert disasm.instructions[0].body == "@R15+, [R0 R1]"


def test_rts(context: Context):
    disasm = context.disassemble(b"\xbb", 0x117B)
    assert len(disasm.instructions) == 1
    assert disasm.instructions[0].mnem == "RTS"
    assert disasm.instructions[0].body == ""


def test_orc(context: Context):
    disasm = context.disassemble(b"\xf9\x20\x71\x01", 0x1177)
    assert len(disasm.instructions) == 1
    assert disasm.instructions[0].mnem == "ORC"
    assert disasm.instructions[0].body == "0x1.B, CCR"
