import pytest
from Test import vote, solution, reverse

@pytest.mark.parametrize(
    'votes, expected',
    (
        [[1, 1, 1, 2, 3], 1],
        [[2, 2, 1, 3, 4], 2],
        [[3, 3, 4, 1, 2], 3]
    )
)
def test_vote(votes, expected):
    actual = vote(votes)
    assert expected == actual

@pytest.mark.parametrize(
    'a, b, c, expected',
    (
        [4, 5, 8, 'корней нет'],
        [3, 2, 4, 'корней нет'],
        [4, -8, 2, [1.71, 0.29]],
        [3, -6, 3, [1]]
    )
)
def test_solution(a, b, c, expected):
    actual = solution(a, b, c)
    assert expected == actual

@pytest.mark.parametrize(
    'string, expected',
    (
        ['Привет!', '!тевирп'],
    )
)
def test_reverse(string, expected):
    actual = reverse(string)
    assert expected == actual