from grade import grade


def test_negative_score_is_invalid():
    assert grade(-1, False) == "invalid"


def test_on_time_pass():
    assert grade(75, False) == "pass"


def test_on_time_fail():
    assert grade(50, False) == "fail"


def test_late_penalty_drops_to_fail():
    assert grade(65, True) == "fail"


def test_boundary_exactly_60_passes():
    assert grade(60, False) == "pass"