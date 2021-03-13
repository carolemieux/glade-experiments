#!/bin/bash

bench=$1

egrep "GRAMMAR|MERGE" glade-results/${bench}-eval.log > raw-gram.tmp
python3 larkfixup.py raw-gram.tmp > glade-results/${bench}-gram.lark

recall=$(python3 eval_larkgram.py glade-results/${bench}-gram.lark examples/${bench}/test_set/* | tail -n 1 | awk '{print $2}' )
precision=$(tail -n 1 glade-results/${bench}-eval.log | sed 's/PASS RATE://' )
runtime=$(tail -n 1 glade-results/${bench}-learn.log | awk '{print $3}')
f1=$(echo $recall $precision | awk '{print 2*$1*$2/($1+$2)}')
oracles=$(grep ORACLE glade-results/${bench}-learn.log | awk '{s += $3} END {print s}')
printf " %.2f & %.2f & %.2f & %.0fs & %i \n" $recall $precision $f1 $runtime $oracles > glade-results/${bench}-results.asv
