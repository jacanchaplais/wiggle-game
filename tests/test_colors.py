from wiggle import color


def test_colors():
    assert color.color_tuple("red") == (255, 0, 0)
