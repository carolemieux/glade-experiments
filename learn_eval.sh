#!/bin/bash
bench=$1
java -cp glade.jar:snakeyaml-1.25.jar glade.main.Main -mode learn -program examples/$bench/config.yml -verbose > glade-results/${bench}-learn.log

