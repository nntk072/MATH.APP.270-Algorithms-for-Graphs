# /usr/bin/env python
from copy import deepcopy as copy
from Ford_Fulkerson import *

if __name__ == "__main__":
    test_function('test_flow_simple_1', 'testset_simple_1')
    test_function('test_flow_simple_2', 'testset_simple_2')
    test_function('test_flow_simple_3', 'testset_simple_3')
    test_function('test_flow_simple_4', 'testset_simple_4')
    test_function('test_flow_simple_5', 'testset_simple_5')

    test_function('testflow_10', 'testset_10')
    test_function('testflow_100', 'testset_100')
    test_function('testflow_1000', 'testset_1000')
    test_function('testflow_10000', 'testset_10000')
