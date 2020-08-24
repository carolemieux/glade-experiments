bench=$1
java -Dglade.serialize.lark=true -cp glade.jar:snakeyaml-1.25.jar glade.main.Main -mode fuzz -program examples/$bench/config.yml -fuzzer grammar -verbose > ${bench}-eval.log

egrep "GRAMMAR|MERGE" ${bench}-eval.log > raw-gram.tmp
python3 larkfixup.py raw-gram.tmp > ${bench}-gram.lark
python3 eval_larkgram.py ${bench}-gram.lark examples/${bench}/test_set/* | tail -n 1

tail -n 1 ${bench}-eval.log | sed 's/PASS RATE/Precision/'
