from pydecorators.basic import timeit, grid_search
from time import sleep


def test_timeit():

    @timeit
    def sleep_function(sleep_time):
        sleep(sleep_time)
        return 2

    sleep_time = 0.4
    function_result, function_time = sleep_function(sleep_time)
    assert function_result == 2
    assert abs(function_time - sleep_time) <= 1e-2


def test_timeit_accuracy():

    @timeit(1)
    def sleep_function(sleep_time):
        sleep(sleep_time)
        return 2

    sleep_time = 0.41
    function_result, function_time = sleep_function(sleep_time)
    assert function_result == 2
    assert function_time == 0.4


def test_grid_search():

    @grid_search(argument_parameters={'a': [1, 2], 'b': [2, 3]})
    def add(a=1, b=1):
        return a + b

    best_args, best_value = add()
    assert best_args == (2, 3)
    assert best_value == 5


def test_grid_search_all_values():

    @grid_search(argument_parameters={'a': [1, 2], 'b': [2, 3]}, return_all_values=True)
    def add(a=1, b=1):
        return a + b

    all_values = add()
    assert isinstance(all_values, dict)
    assert (1, 2) in all_values


def test_grid_search_without_arguments():

    @grid_search(argument_parameters={'a': [1, 2], 'b': [2, 3]}, return_without_arguments=True)
    def add(a=1, b=1, c=3):
        return (a + b) * c

    value = add(c=2)
    assert value == 10
