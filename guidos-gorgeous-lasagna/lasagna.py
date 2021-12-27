EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Return remaining baking time."""
    result = EXPECTED_BAKE_TIME - elapsed_bake_time
    return result


def preparation_time_in_minutes(number_of_layers):
    """Return total preparation time."""
    result = number_of_layers * PREPARATION_TIME
    return result


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return elapsed cooking time."""

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
