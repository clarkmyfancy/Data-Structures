def func():
    return "z"

def test_thing():
    assert func() == "z"

class TestClass:
    def test_he_has_an_h_in_it(self):
        x = "he"
        assert "h" in x 
    
    def test_travis_ci_hooks_are_working(self):
        x = "she"
        assert "s" in x