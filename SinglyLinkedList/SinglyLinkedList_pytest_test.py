def func():
    return "z"

def test_thing():
    assert func() == "z"

class TestClass:
    def test_he_has_an_h_in_it(self):
        x = "he"
        assert "h" in x 