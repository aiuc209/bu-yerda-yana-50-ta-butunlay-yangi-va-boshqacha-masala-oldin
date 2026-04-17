1. `list(map(lambda x: x**2, [1, 2, 3, 4, 5]))`
2. `list(map(lambda x: x.upper(), ["hello", "world"]))`
3. `list(map(lambda x: x*2, [1, 2, 3, 4, 5]))`
4. `list(map(lambda x: x.split(), ["hello world", "python programming"]))`
5. `list(map(lambda x: x.strip(), ["   hello", "world   "]))`
6. `list(map(lambda x: x.replace("a", "b"), ["apple", "banana"]))`
7. `list(map(lambda x: x.title(), ["hello world", "python programming"]))`
8. `list(map(lambda x: x.lower(), ["HELLO", "WORLD"]))`
9. `list(map(lambda x: x.count("a"), ["apple", "banana"]))`
10. `list(map(lambda x: x.find("a"), ["apple", "banana"]))`
11. `list(map(lambda x: x.index("a"), ["apple", "banana"]))`
12. `list(map(lambda x: len(x), ["hello", "world"]))`
13. `list(map(lambda x: x.isdigit(), ["123", "abc"]))`
14. `list(map(lambda x: x.isalpha(), ["123", "abc"]))`
15. `list(map(lambda x: x.isalnum(), ["123", "abc"]))`
16. `list(map(lambda x: x.isspace(), [" ", "abc"]))`
17. `list(map(lambda x: x.startswith("a"), ["apple", "banana"]))`
18. `list(map(lambda x: x.endswith("a"), ["apple", "banana"]))`
19. `list(map(lambda x: x.swapcase(), ["HELLO", "WORLD"]))`
20. `list(map(lambda x: x.center(10), ["hello", "world"]))`
21. `list(map(lambda x: x.ljust(10), ["hello", "world"]))`
22. `list(map(lambda x: x.rjust(10), ["hello", "world"]))`
23. `list(map(lambda x: x.zfill(10), ["123", "456"]))`
24. `list(map(lambda x: x.encode(), ["hello", "world"]))`
25. `list(map(lambda x: x.decode(), [b"hello", b"world"]))`
26. `list(map(lambda x: x.splitlines(), ["hello\nworld", "python\nprogramming"]))`
27. `list(map(lambda x: x.partition("a"), ["apple", "banana"]))`
28. `list(map(lambda x: x.rpartition("a"), ["apple", "banana"]))`
29. `list(map(lambda x: x.maketrans("a", "b"), ["apple", "banana"]))`
30. `list(map(lambda x: x.translate(str.maketrans("a", "b")), ["apple", "banana"]))`
31. `list(map(lambda x: x.format(), ["{} {}", "{} {}"]))`
32. `list(map(lambda x: x.format("hello", "world"), ["{} {}", "{} {}"]))`
33. `list(map(lambda x: x.format_map({"a": "hello", "b": "world"}), ["{a} {b}", "{a} {b}"]))`
34. `list(map(lambda x: x.__add__(" world"), ["hello", "python"]))`
35. `list(map(lambda x: x.__mul__(2), ["hello", "world"]))`
36. `list(map(lambda x: x.__len__(), ["hello", "world"]))`
37. `list(map(lambda x: x.__getitem__(0), ["hello", "world"]))`
38. `list(map(lambda x: x.__setitem__(0, "a"), ["hello", "world"]))`
39. `list(map(lambda x: x.__delitem__(0), ["hello", "world"]))`
40. `list(map(lambda x: x.__contains__("a"), ["apple", "banana"]))`
41. `list(map(lambda x: x.__iter__(), ["hello", "world"]))`
42. `list(map(lambda x: x.__reversed__(), ["hello", "world"]))`
43. `list(map(lambda x: x.__str__(), [123, 456]))`
44. `list(map(lambda x: x.__int__(), ["123", "456"]))`
45. `list(map(lambda x: x.__float__(), ["123.45", "678.90"]))`
46. `list(map(lambda x: x.__complex__(), ["123+45j", "678+90j"]))`
47. `list(map(lambda x: x.__bool__(), [True, False]))`
48. `list(map(lambda x: x.__dict__, [{"a": 1}, {"b": 2}]))`
49. `list(map(lambda x: x.__class__, [123, "hello"]))`
50. `list(map(lambda x: x.__hash__(), [123, "hello"]))`
