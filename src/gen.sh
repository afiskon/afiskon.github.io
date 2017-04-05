#!/bin/sh

set -e

pelican --relative-urls --ignore-cache -o .. content
