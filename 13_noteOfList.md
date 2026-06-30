# Python Notes: List, Set, Tuple, Dictionary and Nested List

## 1. List in Python

A **list** is a collection of elements that is ordered, changeable (mutable), and allows duplicate values.

### Syntax:

```python
list_name = [value1, value2, value3]
```

### Example:

```python
fruits = ["apple", "banana", "mango"]
print(fruits)
```

### Features:

* Ordered collection
* Mutable (can be changed)
* Allows duplicate values
* Can store different data types

### Common Methods:

```python
fruits.append("orange")   # Add element
fruits.remove("banana")   # Remove element
fruits.sort()             # Sort list
fruits.pop()              # Remove last element
```

---

# 2. Nested List

A **nested list** is a list inside another list. It is used to store multiple lists together.

### Example:

```python
students = [
    ["John", 20],
    ["Mary", 21],
    ["Alex", 19]
]

print(students[0])
```

Output:

```
['John', 20]
```

Accessing elements:

```python
print(students[1][0])
```

Output:

```
Mary
```

### Example: Matrix using nested list

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

---

# 3. Tuple in Python

A **tuple** is an ordered collection that is immutable (cannot be changed).

### Syntax:

```python
tuple_name = (value1, value2, value3)
```

### Example:

```python
numbers = (10, 20, 30)
print(numbers)
```

### Features:

* Ordered
* Immutable
* Allows duplicate values
* Faster than lists

### Accessing tuple:

```python
print(numbers[1])
```

Output:

```
20
```

---

# 4. Set in Python

A **set** is an unordered collection of unique elements.

### Syntax:

```python
set_name = {value1, value2}
```

### Example:

```python
numbers = {1, 2, 3, 4}
print(numbers)
```

### Features:

* Unordered
* Mutable
* Does not allow duplicates
* No indexing

Example:

```python
a = {1,2,2,3}
print(a)
```

Output:

```
{1,2,3}
```

### Common Methods:

```python
a.add(5)        # Add element
a.remove(2)     # Remove element
a.clear()       # Remove all elements
```

---

# 5. Dictionary in Python

A **dictionary** stores data in key-value pairs.

### Syntax:

```python
dict_name = {
    key:value
}
```

### Example:

```python
student = {
    "name":"John",
    "age":20,
    "course":"Python"
}

print(student)
```

Output:

```
{'name':'John','age':20,'course':'Python'}
```

### Access values:

```python
print(student["name"])
```

Output:

```
John
```

### Common Methods:

```python
student.keys()     # Get keys
student.values()   # Get values
student.items()    # Get key-value pairs
student.update()   # Update dictionary
```

---

# Difference Between List, Tuple, Set and Dictionary

| Feature   | List    | Tuple   | Set         | Dictionary       |
| --------- | ------- | ------- | ----------- | ---------------- |
| Order     | Ordered | Ordered | Unordered   | Ordered          |
| Mutable   | Yes     | No      | Yes         | Yes              |
| Duplicate | Allowed | Allowed | Not Allowed | Keys not allowed |
| Indexing  | Yes     | Yes     | No          | Using keys       |
| Symbol    | []      | ()      | {}          | {key:value}      |

---

## Summary

* **List:** Used when data can change and order matters.
* **Tuple:** Used for fixed data that should not change.
* **Set:** Used for unique values and removing duplicates.
* **Dictionary:** Used for storing data as key-value pairs.
* **Nested List:** Used to store lists inside another list, useful for matrices and grouped data.
