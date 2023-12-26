#!/usr/bin/env sh

LOCATION=$(pwd)
pushd "$GHIDRA_INSTALL_DIR/support"

./sleigh -a "$LOCATION"
