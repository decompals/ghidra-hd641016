#!/usr/bin/env sh

LOCATION=$(pwd)
pushd ../../../support

./sleigh -a "$LOCATION"
