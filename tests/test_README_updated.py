def test_README():
    with open("README.md") as f:
        contents = f.read().lower()
        assert "snowman" in contents

