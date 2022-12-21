# Nouns-Coreference-Annotation

annotate.py is the main program you want to run.
annotate.tsv is where your annotations get outputted.

The way you input your coreference chains is as a comma seperated list.
Here's an example.
With an input like "James couldn 't sleep . [He]_1 was restless. [He]_2 felt tired."
You would output: "James,[He]_1,[He]_2"
Note three things:
-You have to type the words in the exact weird way they are formatted
	("James,He,He" won't fly)
	("james,[He]_1,[He]_2" also won't work)
-You do not put a space after the comma 
	("James, [He]_1, [He]_2" also isn't ok.)
	(It will be accepted by the program but to make interannotion socres easier, avoid it.)
-You have to put the coreferenced words in the order they appear in the sentence 
	("[He]_1,[He]_2,James" will not be accepted)

After you type your chain and you press enter you can write another seperate coreference chain.

If you are done typing coreference chains, type "!" to move onto the next text.

NOTE: 
You can use ctrl+C to stop the program at any time. 
HOWEVER, your progress is only saved when you type "!" !

NOTE 2:
You can type ? to see the original unaltered text to make it easier to read. 
It wont have any of the numbers going on.
HOWEVER, you do still have to write your coreference chain with all the brackets and numbers.

NOTE 3:
I currently have the program set to only have you annotate the first 50 texts just to test the waters.
I can remove this limitation if we want to annotate all 241 texts, or at least the first 100.
