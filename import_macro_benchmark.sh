#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage: $0 [example-name]"
	exit 1
fi

if [[ -z $MACRO_EXAMPLES_ROOT ]]; then
	echo "Please set MACRO_EXAMPLES_ROOT to the root location of the macro benchmarks"
	exit 1
fi

name=$1
orig_example_dir=$MACRO_EXAMPLES_ROOT/$1
example_dir=examples/$name

if [[ -d $example_dir ]]; then
	echo "$example_dir already exists"
	exit 1
fi

mkdir $example_dir
cp -r $orig_example_dir/${name}-train $example_dir/guides
cp -r $orig_example_dir/${name}-test $example_dir/test_set
cp $orig_example_dir/parse_${name} $example_dir/parse_${name}

echo "name: \"$name\"" >> $example_dir/config.yml
echo "empty: \"$(cat ${example_dir}/guides/$(ls ${example_dir}/guides | head -n 1) | sed 's/"/\\"/g')\"" >> $example_dir/config.yml
echo "iserror: true" >> $example_dir/config.yml
echo "extension: \".ex\"" >> $example_dir/config.yml
echo "command: \"parse_${name}\"" >> $example_dir/config.yml
echo "traindir: \"guides\"" >> $example_dir/config.yml

