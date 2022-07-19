import sys
import utils.argumentparser

args = sys.argv[1:]

ArgumentParser = utils.argumentparser.ArgParser(["l", "p#", "d*"], args)

print(ArgumentParser.getArgument("l"))
print(ArgumentParser.getArgument("p"))
print(ArgumentParser.getArgument("d"))


