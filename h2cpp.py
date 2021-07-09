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
- maybe make end of declaration checking smarter?
"""


import sys


if len(sys.argv) != 2:
    print("Usage: h2cpp <header file>")
    sys.exit()

# We know the class name from the header file name
className = sys.argv[1][:-2]
# print(f"className: '{className}'")


# Open files
hfile = open(sys.argv[1], 'r')
cppfile = open(className + ".cpp", 'w')

cppfile.write(f"#include \"{sys.argv[1]}\"\n")

inDefinition = False
for line in hfile:
    # discard lines before class definition
    if not inDefinition:
        if f"class {className} {{" not in line:
            continue
        else:
            inDefinition = True
            continue
    
    # strip that hoe
    line = line.strip()
    
    # stop reading when end of definition reached
    if line == "};":
        break

    # strip comments
    if "//" in line:
        line = line[:line.index("//")]
        line = line.strip()

    # Don't read private/public decorators
    if "private" in line or "public" in line:
        continue

    # skip empty lines
    if line == "":
        continue
    
    # skip non-function-declaration lines
    if "(" not in line and ")" not in line:
        continue
    
    if " " in line and line.index(" ") < line.index("("):  # If there's a space in the line
        theType = line[:line.index(" ")]
        theRest = line[line.index(" ") + 1:]
        conversion = f"{theType} {className}::{theRest[:-1]}\n{{\n    \n}}\n"
    else:  # It's one of the big five
        conversion = f"{className}::{line[:-1]}\n{{\n\n}}\n"
    
    print("Converting:\n"
    f"{line}\n"
    "into:\n"
    f"{conversion}")

    cppfile.write("\n" + conversion)
    

# Close files
hfile.close()
cppfile.close()