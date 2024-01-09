import numpy as np

from agents.agent_minimax.heuristic import *

def test_extract_windows():
    array = [0,1,2,3,4,5,6]
    position = 3
    windows = extract_windows(array,position)
    print(windows)

    assert np.all(windows == [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
)