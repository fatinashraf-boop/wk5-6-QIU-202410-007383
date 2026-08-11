"""
Assignment starter: backtracking CSP solver for map colouring.

Read ../guide.md and ../worked_example.md BEFORE you start coding here.

Your job: fill in every function marked TODO. Do not change function
signatures (the tests in test_csp_map_coloring.py rely on them).

The problem: colour a map of Australia's 7 regions so that no two adjacent
regions share a colour, using only 3 colours.
"""
VARIABLES = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

NEIGHBOURS = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V": ["SA", "NSW"],
    "T": [],
}

DOMAIN = ["Red", "Green", "Blue"]


def is_consistent(assignment, var, value):
    """
    Return True if assigning value to var does not conflict
    with any already-assigned neighbour.
    """

    for neighbour in NEIGHBOURS[var]:

        if neighbour in assignment:
            if assignment[neighbour] == value:
                return False

    return True


def select_unassigned_variable(assignment):
    """
    Return the first variable that has not been assigned.

    Return None when all variables have been assigned.
    """

    for var in VARIABLES:

        if var not in assignment:
            return var

    return None


def backtracking_search(variables, domain):
    """
    Run backtracking search.

    Returns:
        A complete and consistent assignment, or None
        if no solution exists.
    """

    assignment = {}

    def backtrack():

        # 1. Check whether assignment is complete
        if len(assignment) == len(variables):
            return dict(assignment)

        # 2. Select an unassigned variable
        var = select_unassigned_variable(assignment)

        # 3. Try every value in the domain
        for value in domain:

            # 4. Check consistency
            if is_consistent(assignment, var, value):

                # Tentatively assign the value
                assignment[var] = value

                # 5. Recursively search
                result = backtrack()

                if result is not None:
                    return result

                # 6. Backtrack
                del assignment[var]

        # 7. No value worked
        return None

    return backtrack()


if __name__ == "__main__":

    solution = backtracking_search(VARIABLES, DOMAIN)

    if solution:

        print("Solution found:")

        for region in VARIABLES:
            print(f"  {region}: {solution[region]}")

    else:
        print("No solution exists with this domain.")