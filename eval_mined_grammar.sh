#!/bin/bash

bench=$1

if [ -z "$PYTHON" ]; then
  echo "Please set \$PYTHON to the location of the python you want me to use (maybe a pypy? :) )"
  exit 1
fi

egrep -a "GRAMMAR|MERGE" glade-results/${bench}-eval.log > raw-gram.tmp
$PYTHON larkfixup.py raw-gram.tmp > glade-results/${bench}-gram.lark

$PYTHON eval_larkgram.py glade-results/${bench}-gram.lark examples/${bench}/test_set/* > glade-results/${bench}-recall.log

if [ -f glade-results/${bench}-recall.log ]; then
  ./print_results.sh $bench
fi
