#!/bin/sh

set -e

rm ../*.html || true
rm -r ../author || true
rm -r ../author || true
rm -r ../category || true
rm -r ../rss || true
rm -r ../theme || true

pelican --relative-urls --ignore-cache \
  --theme-path template/pelican-simplegrey \
  -o .. content
