#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage: $0 [example-name]"
	exit 1
fi

if [[ -z $EXAMPLES_ROOT ]]; then
	echo "Please set EXAMPLES_ROOT to the root location of the search-synth examples"
	exit 1
fi

name=$1
orig_example_dir=$EXAMPLES_ROOT/$1
example_dir=examples/$name

if [[ -d $example_dir ]]; then
	echo "$example_dir already exists"
	exit 1
fi

mkdir $example_dir
cp -r $orig_example_dir/guides $example_dir/guides
cp -r $orig_example_dir/test_set $example_dir/test_set
cp $orig_example_dir/parse_${name} $example_dir/parse_${name}

echo "name: \"$name\"" >> $example_dir/config.yml
echo "empty: \"$(cat ${orig_example_dir}/guides/guide-0.ex | sed 's/"/\\"/g')\"" >> $example_dir/config.yml
echo "iserror: true" >> $example_dir/config.yml
echo "extension: \".ex\"" >> $example_dir/config.yml
echo "command: \"parse_${name}\"" >> $example_dir/config.yml
echo "traindir: \"guides\"" >> $example_dir/config.yml

