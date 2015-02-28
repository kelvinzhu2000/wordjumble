import jumble

def test_jumble():
    assertEqual(jumble.find_words(""), [])
    assertEqual(jumble.find_words("dog"), ["do", "go", "god", "dog"])
    assertEqual(jumble.find_words("odg"), ["do", "go", "god", "dog"])
    assertEqual(jumble.find_words("hello"), ["hell", "he", "hello", "oh", "eh", "ho", "hole"])
    assertEqual(jumble.find_words("a"), ["a"])

def assertEqual(L1, L2):
    assert len(L1) == len(L2) and sorted(L1) == sorted(L2)
