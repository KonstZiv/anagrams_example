# anagrams_foxminded

---

## Task 1

### student: XXXXXXXXXXXXX

Write an application that reverses all the words of input text:
Example "abcd efgh" => "dcba hgfe"

All non-letter symbols should stay on the same places:

Example "a1bcd efg!h" => "d1cba hgf!e"
Use Latin alphabet for test only.

You should write a function which returns reverse text

Hint
Use statement "if __name__ ==  '__main__':" as wrapper for printing result of function.
Test strings should be declared in statement "if __name__ ==  '__main__':"
And call function should also be here.

```python
if __name__ == "__main__":
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),
    ]

    for text, reversed_text in cases:
        assert your_function(text) == reversed_text
```