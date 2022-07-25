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


test_defaultValue()
test_booleanValue()
test_integerValue()
test_stringValue()
test_doubleValue()