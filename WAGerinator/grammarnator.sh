/bin/bash 

grammarinator-process WagLexer.g4 WagParser.g4 -o codegen/ --no-actions
grammarinator-generate WagGenerator.WagGenerator -r wag -d 10 -o samples/sample_%d.wag -n 100 --sys-path codegen
