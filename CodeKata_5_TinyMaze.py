from utils.tinymaze import TinyMazeSolver

def Test3by3():
    TestMazeSolver = TinyMazeSolver()

    maze = [ [ 'S',  0,  1, ],
             [ 1,  0,  1, ],
             [ 1,  0,  'E', ] ]

    solution = TestMazeSolver.solve(maze)

    assert solution == [['x',  'x',  1, ],
                        [ 1,  'x',  1, ],
                        [ 1,  'x',  'x',]]

def Test4by4():
    TestMazeSolver = TinyMazeSolver()

    maze = [[ 'S', 0, 1, 0],
            [ 1, 0, 1, 1],
            [ 1, 0, 0, 'E']]

    solution = TestMazeSolver.solve(maze)

    assert solution == [[ 'x', 'x', 1, 0],
                        [ 1, 'x', 1, 1],
                        [ 1, 'x', 'x', 'x']]



Test3by3()
Test4by4()