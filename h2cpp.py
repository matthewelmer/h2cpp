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

# We know the class name from the header file name
className = sys.argv[1][:-2]
# print(f"className: {className}")


# Open files
hfile = open(sys.argv[1], 'r')
cppfile = open(className + ".cpp", 'w')


# Close files
hfile.close()
cppfile.close()
            

# skip until class declaration
