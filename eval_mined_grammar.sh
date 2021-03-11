bench=$1
java -Dglade.serialize.lark=true -cp glade.jar:snakeyaml-1.25.jar glade.main.Main -mode fuzz -program examples/$bench/config.yml -fuzzer grammar -verbose > ${bench}-eval.log

egrep "GRAMMAR|MERGE" ${bench}-eval.log > raw-gram.tmp
python3 larkfixup.py raw-gram.tmp > ${bench}-gram.lark

recall=$(python3 eval_larkgram.py ${bench}-gram.lark examples/${bench}/test_set/* | tail -n 1 | awk '{print $2}' )
precision=$(tail -n 1 ${bench}-eval.log | sed 's/PASS RATE://' )
runtime=$(tail -n 1 ${bench}-learn.log | awk '{print $3}')
f1=$(echo $recall $precision | awk '{print 2*$1*$2/($1+$2)}')
printf " %.2f & %.2f & %.2f & %.0fs \n" $recall $precision $f1 $runtime
