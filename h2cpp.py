"""
1. Open the h file
2. Parse out the class name
3. Figure out what's public and private -OR- just ignore everything that's not public
4. Read and close h file
5. Open new cpp file
6. #include header file
7. Write all function definition starters

Formatting:
For constructors/destructors:
ClassName(params);
->
ClassName::Classname(params)
{

}

For all tha functions/operators:
type funcName(params) isConst?
->
type ClassName::funcName(params) isConst?
{

}

To do:
- header guard check?
"""


import sys


if len(sys.argv) != 2:
    print("Usage: h2cpp <header file>")
    sys.exit()



# Open file
with open(sys.argv[1], 'r') as hfile:
    for line in hfile:
        if "class" in line and ';' in line and line.index("class") < line.index(';'):
            print(line)
            # So what I've done is I've found the class declaration, just want to yank its name
            # and go back and take care of everything else while attempting to preserve comments
            # (if easily possible)

# skip until class declaration
