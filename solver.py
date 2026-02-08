VALID_FACES = {"U", "D", "L", "R", "F", "B"}


def normalize_move(token: str) -> str:
    token = token.strip()
    if not token:
        raise ValueError("Empty move token")

    face = token[0].upper()
    if face not in VALID_FACES:
        raise ValueError(f"Invalid face '{token[0]}' in move '{token}'")

    suffix = token[1:]
    if suffix not in {"", "'", "2"}:
        raise ValueError(
            f"Invalid move suffix '{suffix}' in move '{token}'. Use only '', "
            "' or '2'."
        )

    return face + suffix


def parse_scramble(scramble: str) -> list[str]:
    if not scramble or not scramble.strip():
        raise ValueError("Please enter a scramble sequence.")

    raw_tokens = scramble.split()
    return [normalize_move(token) for token in raw_tokens]


def inverse_move(move: str) -> str:
    if move.endswith("2"):
        return move
    if move.endswith("'"):
        return move[0]
    return move + "'"


def solve_from_scramble(scramble: str) -> dict:
    moves = parse_scramble(scramble)
    solution_moves = [inverse_move(move) for move in reversed(moves)]

    return {
        "scramble": " ".join(moves),
        "move_count": len(solution_moves),
        "solution": " ".join(solution_moves),
        "steps": solution_moves,
    }
