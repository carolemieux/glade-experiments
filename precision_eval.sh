#!/bin/bash
bench=$1
java -Dglade.serialize.lark=true -cp glade.jar:snakeyaml-1.25.jar glade.main.Main -mode fuzz -program examples/$bench/config.yml -fuzzer grammar -verbose > glade-results/${bench}-eval.log

