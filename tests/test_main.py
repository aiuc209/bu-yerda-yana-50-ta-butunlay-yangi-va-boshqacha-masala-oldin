import pytest

def test_map_1():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * 2, numbers))
    assert result == [2, 4, 6, 8, 10]

def test_map_2():
    names = ["John", "Alice", "Bob"]
    result = list(map(lambda x: x.upper(), names))
    assert result == ["JOHN", "ALICE", "BOB"]

def test_map_3():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x ** 2, numbers))
    assert result == [1, 4, 9, 16, 25]

def test_map_4():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: x["name"], data))
    assert result == ["John", "Alice"]

def test_map_5():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x + 1, numbers))
    assert result == [2, 3, 4, 5, 6]

def test_map_6():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: x["age"], data))
    assert result == [30, 25]

def test_map_7():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * x, numbers))
    assert result == [1, 4, 9, 16, 25]

def test_map_8():
    names = ["John", "Alice", "Bob"]
    result = list(map(lambda x: x.lower(), names))
    assert result == ["john", "alice", "bob"]

def test_map_9():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: x["name"] + " " + str(x["age"]), data))
    assert result == ["John 30", "Alice 25"]

def test_map_10():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x - 1, numbers))
    assert result == [0, 1, 2, 3, 4]

def test_map_11():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: {"name": x["name"], "age": x["age"] + 1}, data))
    assert result == [{"name": "John", "age": 31}, {"name": "Alice", "age": 26}]

def test_map_12():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * x * x, numbers))
    assert result == [1, 8, 27, 64, 125]

def test_map_13():
    names = ["John", "Alice", "Bob"]
    result = list(map(lambda x: x.capitalize(), names))
    assert result == ["John", "Alice", "Bob"]

def test_map_14():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: x["name"] + " is " + str(x["age"]) + " years old", data))
    assert result == ["John is 30 years old", "Alice is 25 years old"]

def test_map_15():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x ** 3, numbers))
    assert result == [1, 8, 27, 64, 125]

def test_map_16():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: {"name": x["name"], "age": x["age"] - 1}, data))
    assert result == [{"name": "John", "age": 29}, {"name": "Alice", "age": 24}]

def test_map_17():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * x * x * x, numbers))
    assert result == [1, 16, 81, 256, 625]

def test_map_18():
    names = ["John", "Alice", "Bob"]
    result = list(map(lambda x: x.replace("o", "0"), names))
    assert result == ["J0hn", "Alice", "B0b"]

def test_map_19():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: x["name"] + " is " + str(x["age"] + 1) + " years old", data))
    assert result == ["John is 31 years old", "Alice is 26 years old"]

def test_map_20():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x ** 4, numbers))
    assert result == [1, 16, 81, 256, 625]

def test_map_21():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: {"name": x["name"], "age": x["age"] + 2}, data))
    assert result == [{"name": "John", "age": 32}, {"name": "Alice", "age": 27}]

def test_map_22():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * x * x * x * x, numbers))
    assert result == [1, 32, 243, 1024, 3125]

def test_map_23():
    names = ["John", "Alice", "Bob"]
    result = list(map(lambda x: x.replace("a", "4"), names))
    assert result == ["John", "4lice", "Bob"]

def test_map_24():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: x["name"] + " is " + str(x["age"] - 1) + " years old", data))
    assert result == ["John is 29 years old", "Alice is 24 years old"]

def test_map_25():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x ** 5, numbers))
    assert result == [1, 32, 243, 1024, 3125]

def test_map_26():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: {"name": x["name"], "age": x["age"] - 2}, data))
    assert result == [{"name": "John", "age": 28}, {"name": "Alice", "age": 23}]

def test_map_27():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * x * x * x * x * x, numbers))
    assert result == [1, 64, 729, 4096, 15625]

def test_map_28():
    names = ["John", "Alice", "Bob"]
    result = list(map(lambda x: x.replace("e", "3"), names))
    assert result == ["John", "Al3c3", "Bob"]

def test_map_29():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: x["name"] + " is " + str(x["age"] + 3) + " years old", data))
    assert result == ["John is 33 years old", "Alice is 28 years old"]

def test_map_30():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x ** 6, numbers))
    assert result == [1, 64, 729, 4096, 15625]

def test_map_31():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: {"name": x["name"], "age": x["age"] + 3}, data))
    assert result == [{"name": "John", "age": 33}, {"name": "Alice", "age": 28}]

def test_map_32():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * x * x * x * x * x * x, numbers))
    assert result == [1, 128, 2187, 16384, 78125]

def test_map_33():
    names = ["John", "Alice", "Bob"]
    result = list(map(lambda x: x.replace("i", "1"), names))
    assert result == ["John", "Al1ce", "Bob"]

def test_map_34():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: x["name"] + " is " + str(x["age"] - 3) + " years old", data))
    assert result == ["John is 27 years old", "Alice is 22 years old"]

def test_map_35():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x ** 7, numbers))
    assert result == [1, 128, 2187, 16384, 78125]

def test_map_36():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: {"name": x["name"], "age": x["age"] - 3}, data))
    assert result == [{"name": "John", "age": 27}, {"name": "Alice", "age": 22}]

def test_map_37():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * x * x * x * x * x * x * x, numbers))
    assert result == [1, 256, 6561, 65536, 390625]

def test_map_38():
    names = ["John", "Alice", "Bob"]
    result = list(map(lambda x: x.replace("o", "0"), names))
    assert result == ["J0hn", "Alice", "B0b"]

def test_map_39():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: x["name"] + " is " + str(x["age"] + 4) + " years old", data))
    assert result == ["John is 34 years old", "Alice is 29 years old"]

def test_map_40():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x ** 8, numbers))
    assert result == [1, 256, 6561, 65536, 390625]

def test_map_41():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: {"name": x["name"], "age": x["age"] + 4}, data))
    assert result == [{"name": "John", "age": 34}, {"name": "Alice", "age": 29}]

def test_map_42():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * x * x * x * x * x * x * x * x, numbers))
    assert result == [1, 512, 19683, 262144, 1953125]

def test_map_43():
    names = ["John", "Alice", "Bob"]
    result = list(map(lambda x: x.replace("u", "7"), names))
    assert result == ["John", "Alice", "Bob"]

def test_map_44():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: x["name"] + " is " + str(x["age"] - 4) + " years old", data))
    assert result == ["John is 26 years old", "Alice is 21 years old"]

def test_map_45():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x ** 9, numbers))
    assert result == [1, 512, 19683, 262144, 1953125]

def test_map_46():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: {"name": x["name"], "age": x["age"] - 4}, data))
    assert result == [{"name": "John", "age": 26}, {"name": "Alice", "age": 21}]

def test_map_47():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * x * x * x * x * x * x * x * x * x, numbers))
    assert result == [1, 1024, 59049, 1048576, 9765625]

def test_map_48():
    names = ["John", "Alice", "Bob"]
    result = list(map(lambda x: x.replace("b", "8"), names))
    assert result == ["John", "Alice", "8ob"]

def test_map_49():
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    result = list(map(lambda x: x["name"] + " is " + str(x["age"] + 5) + " years old", data))
    assert result == ["John is 35 years old", "Alice is 30 years old"]

def test_map_50():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x ** 10, numbers))
    assert result == [1, 1024, 59049, 1048576, 9765625]
