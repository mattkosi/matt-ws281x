#!/bin/bash

if (( $# != 1 )); then
  echo "Enter exactly one file as an argument" >&2
  exit 2
fi

if ! [ -f $(pwd)/$1 ]; then
  echo "You must give a valid file" >&1
  exit 1
fi

sudo python3 $(pwd)/$1 &
