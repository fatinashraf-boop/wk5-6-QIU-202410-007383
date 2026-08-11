"""
Tests for csp_map_coloring.py

Run with:
    pytest 02_CSP/starter_code/test_csp_map_coloring.py -v

`test_given_example` below is COMPLETE -- study it as a template.

You must then write the 3 required test cases (test_case_1, test_case_2,
test_case_3). Read ../../03_Test_Case_Design/mindmap.md and
training_guide.md before choosing what your 3 cases should cover. Aim to
pick 3 *different* categories rather than 3 variations of the same thing
(e.g. one typical/solvable case, one edge/boundary case, one
unsolvable/over-constrained case).

For each test case, write a short comment explaining WHICH category from
the mind-map it represents and WHY you chose it.
"""
import pytest

from csp_map_coloring import (
    backtracking_search,
    is_consistent
)


def _is_valid_solution(solution, variables, neighbours):
    """
    Helper: check a solution assigns every variable and breaks no
    adjacency constraint.
    """

    if solution is None:
        return False

    if set(solution.keys()) != set(variables):
        return False

    for var, value in solution.items():
        for neighbour in neighbours[var]:
            if neighbour in solution:
                if solution[neighbour] == value:
                    return False

    return True


# ---------------------------------------------------------------------
# GIVEN EXAMPLE -- complete, do not modify.
#
# Category: typical/normal small solvable case
# ---------------------------------------------------------------------

def test_given_example():

    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(VARIABLES, DOMAIN)

    assert solution is not None
    assert _is_valid_solution(
        solution,
        VARIABLES,
        NEIGHBOURS
    )


# ---------------------------------------------------------------------
# Test Case 1
#
# Category: typical/solvable case
#
# This checks that the solver can find a valid colouring using
# the required three-colour domain.
# ---------------------------------------------------------------------

def test_case_1():

    from csp_map_coloring import VARIABLES, NEIGHBOURS

    domain = ["Red", "Green", "Blue"]

    solution = backtracking_search(
        VARIABLES,
        domain
    )

    assert solution is not None

    assert _is_valid_solution(
        solution,
        VARIABLES,
        NEIGHBOURS
    )


# ---------------------------------------------------------------------
# Test Case 2
#
# Category: edge/boundary case
#
# Tasmania has no neighbours. This test verifies that an isolated
# variable can still be assigned a valid colour.
# ---------------------------------------------------------------------

def test_case_2():

    from csp_map_coloring import VARIABLES, NEIGHBOURS

    assignment = {
        "T": "Red"
    }

    # T has no neighbours, so assigning Red must be consistent.
    assert is_consistent(
        assignment,
        "T",
        "Green"
    )

    assert NEIGHBOURS["T"] == []


# ---------------------------------------------------------------------
# Test Case 3
#
# Category: unsolvable / over-constrained case
#
# The Australia map cannot be coloured using only two colours.
# The solver should therefore return None after backtracking.
# ---------------------------------------------------------------------

def test_case_3():

    from csp_map_coloring import VARIABLES

    domain = ["Red", "Green"]

    solution = backtracking_search(
        VARIABLES,
        domain
    )

    assert solution is None


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
