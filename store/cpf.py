def _check_digit(digits: list[int]) -> int:
    weight = len(digits) + 1
    remainder = sum(d * (weight - i) for i, d in enumerate(digits)) % 11
    return 0 if remainder < 2 else 11 - remainder


def is_valid_cpf(cpf: str) -> bool:
    digits = [int(c) for c in cpf if c.isdigit()]
    if len(digits) != 11:
        return False
    first = _check_digit(digits[:9])
    second = _check_digit(digits[:9] + [first])
    return digits[9] == first and digits[10] == second
