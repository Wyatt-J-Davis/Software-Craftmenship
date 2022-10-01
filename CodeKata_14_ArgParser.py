import utils.argumentparser

def test_defaultValue():
    args = ['-d', 'Hello', '-p', '7']
    ArgumentParser = utils.argumentparser.ArgParser(["l", "p#", "d*", "c##"], args)

    assert ArgumentParser.getArgument("l") == False

def test_booleanValue():
    args = ['-d', 'Hello', '-p', '7', '-l', 'True']
    ArgumentParser = utils.argumentparser.ArgParser(["l", "p#", "d*", "c##"], args)

    assert ArgumentParser.getArgument("l") == True

def test_integerValue():
    args = ['-d', 'Hello', '-p', '7', '-l', 'True']
    ArgumentParser = utils.argumentparser.ArgParser(["l", "p#", "d*", "c##"], args)

    assert ArgumentParser.getArgument("p") == 7

def test_stringValue():
    args = ['-d', 'Hello', '-p', '7', '-l', 'True']
    ArgumentParser = utils.argumentparser.ArgParser(["l", "p#", "d*", "c##"], args)

    assert ArgumentParser.getArgument("d") == 'Hello'

def test_doubleValue():
    args = ['-d', 'Hello', '-p', '7', '-l', 'True', '-c', "3.14"]
    ArgumentParser = utils.argumentparser.ArgParser(["l", "p#", "d*", "c##"], args)

    assert ArgumentParser.getArgument("c") == 3.14

def test_Cardinality():
    args = ['-d', 'Hello', '-p', '7', '-l', 'True', '-c', "3.14"]
    ArgumentParser = utils.argumentparser.ArgParser(["l", "p#", "d*", "c##"], args)

    assert ArgumentParser.cardinality() == 4

def test_usage():
    args = ['-d', 'Hello', '-p', '7', '-l', 'True', '-c', "3.14"]
    ArgumentParser = utils.argumentparser.ArgParser(["l", "p#", "d*", "c##"], args)

    assert ArgumentParser.usage() == "-['l', 'p#', 'd*', 'c##']-"
    
def test_hasTrue():
    args = ['-d', 'Hello', '-p', '7', '-l', 'True', '-c', "3.14"]
    ArgumentParser = utils.argumentparser.ArgParser(["l", "p#", "d*", "c##"], args)

    assert ArgumentParser.has('l') == True

def test_hasFalse():
    args = ['-d', 'Hello', '-p', '7', '-c', "3.14"]
    ArgumentParser = utils.argumentparser.ArgParser(["l", "p#", "d*", "c##"], args)

    assert ArgumentParser.has('l') == False


test_defaultValue()
test_booleanValue()
test_integerValue()
test_stringValue()
test_doubleValue()
test_Cardinality()
test_usage()
test_hasTrue()
test_hasFalse()