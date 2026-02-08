from solver import inverse_move, parse_scramble, solve_from_scramble


def test_parse_scramble_normalizes_case():
    assert parse_scramble("r u r' u' f2") == ["R", "U", "R'", "U'", "F2"]


def test_inverse_move():
    assert inverse_move("R") == "R'"
    assert inverse_move("R'") == "R"
    assert inverse_move("R2") == "R2"


def test_solution_inverts_scramble():
    result = solve_from_scramble("R U R' U'")
    assert result["solution"] == "U R U' R'"
    assert result["move_count"] == 4
