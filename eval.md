# Evaluation Mode notes

To quickly evaluate Glade on a variety of programs without having to hardcode a different kind of program, I have implemented an evaluation mode which only involves the creation of a yaml file.

First, download snakeyaml: 
```
wget https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.25/snakeyaml-1.25.jar
```

Then build glade with `ant`.

To run on a new example, use the command:
```
java -cp glade.jar:snakeyaml-1.25.jar glade.main.Main -mode learn -program PROGEXAMPLEPATH/config.yml
```

We assume the following fields in the yaml:
```
name: [PRETTY NAME]
empty: [minimal parsing example]
iserror: [boolean, should I look at the output or error stream for errors]
extension: [extension of input training files]
command: [command to run the program, relative to PROGEXAMPLEPATH]
traindir: [directory containing training files, relateive to PROGEXAMPLEPATH]
```

Learned grammars will go into `GLADEDIR/data/grammars/NAME`, where `NAME` is the name from the .yml file. 
