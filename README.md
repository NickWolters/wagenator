# WAGenator

This repository is a collection of different grammar generation techniques, as part of research into grammars. The generate results are based upon a grammar called Weighted Attribute Grammar[(WAG)](https://www.grammarware.org/text/2022/conversational.pdf). Furhtermore, this repo contains other program, related to specication of WAG such as Standardised Weigthed Attribute Grammar(SWAG), and WAGANTLR an ANTLR implementation to test whether generated samples parse on the grammar.

## WAGerinator (Grammarinator)

WAGerinator is the WAG implementation of the Grammarintor frameworks, to generate fuzzers for the grammar. The original code base can be found [here](https://github.com/renatahodovan/grammarinator).

## WAGformer (Transformer Network)

WAGformer is a TUI which makes generation of grammar content possible through the use of Transformer Networks. There two implementations of transformer networks which are both from Hugging Face, these are [GPT-2](https://huggingface.co/openai-community/gpt2) and Bidirectional encoder representations from transformers [(BERT)](https://huggingface.co/docs/transformers/model_doc/bert-generation). 

## WAGSmith (XSmith)

WAGSmith is a partial WAG implementation for XSmith, which is not complete, since XSmith main focus is languages and not grammar. Nevertheless, XSmith provides semeantic correctness for WAG.
As for the original source you can visit the University of Utah [website](https://www.flux.utah.edu/project/xsmith) and [Gitlab](https://gitlab.flux.utah.edu/xsmith/xsmith) page.

## WAGenetics (Evolutionary Grammars)

WAGentics is an Evolutionary Grammar which makes use the [Grape](https://github.com/bdsul/grape) framework to generate WAG samples. These samples are based upon a Backus-Naur Form(BNF) version of the original grammar. The code itself is written in Python and use both grape and [DEAP](https://github.com/deap/deap) for Genetic Alogirhtms(GA).

# Thesis

This repository is part of proof written in my thesis for the University of Twente MSc Computers with a specialization of Software Technology. A link to the paper will be provided when it is published on the website of the University.

This thesis also took inspiration from one of my former classmates Rafael, which has his code base and paper [here](https://dulfer.be/wagon/wagon/index.html)
