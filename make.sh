#!/usr/bin/env sh

"$GHIDRA_INSTALL_DIR/support/sleigh" "data/languages/hd641016.slaspec"

pytest
