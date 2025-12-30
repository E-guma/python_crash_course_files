# Python Data Structures & Functions Master Reference

## Table of Contents
1. [List Methods](#1-list-methods-mutable)
2. [Tuple Methods](#2-tuple-methods-immutable)
3. [Dictionary Methods](#3-dictionary-methods-key-value)
4. [Set Methods](#4-set-methods-unique--unordered)
5. [Advanced "Spicy" Tools](#5-advanced-spicy-tools)
6. [Lambdas](#6-lambdas-anonymous-functions)
7. [Maps, Iterators & Generators](#7-maps-iterators--generators)
8. [Quick Comparison Cheat Sheet](#8-quick-comparison-cheat-sheet)

---

## 1. List Methods (Mutable)
Lists are ordered sequences that can be changed. `[1, 2, 3]`

### Adding Elements
* **`list.append(x)`**: Adds `x` to the end.
* **`list.extend(iterable)`**: Appends all items from an iterable.
* **`list.insert(i, x)`**: Inserts `x` at index `i`.

### Removing Elements
* **`list.remove(x)`**: Removes the first occurrence of `x`.
* **`list.pop([i])`**: Removes and returns item at index `i` (default last).
* **`list.clear()`**: Removes all items.

### Searching & Reordering
* **`list.index(x)`**: Returns index of first `x`.
* **`list.count(x)`**: Returns how many times `x` appears.
* **`list.sort(key=None, reverse=False)`**: Sorts in-place.
* **`list.reverse()`**: Reverses in-place.
* **`list.copy()`**: Returns a shallow copy.

---

## 2. Tuple Methods (Immutable)
Tuples are ordered sequences that cannot be changed. `(1, 2, 3)`

* **`tuple.count(x)`**: Returns how many times `x` appears.
* **`tuple.index(x)`**: Returns index of first `x`.
* **Note:** Supports indexing `t[0]` and slicing `t[1:3]`, but no modification.

---

## 3. Dictionary Methods (Key-Value)
Unordered collection of unique keys and values. `{'key': 'value'}`

### Accessing
* **`dict.get(key, default)`**: Returns value for key, or default if missing (safe).
* **`dict.keys()`**: Returns all keys.
* **`dict.values()`**: Returns all values.
* **`dict.items()`**: Returns `(key, value)` pairs.

### Modifying
* **`dict.update(other)`**: Merges another dict into this one.
* **`dict.setdefault(key, default)`**: Returns value if key exists; if not, inserts key with default.
* **`dict.pop(key)`**: Removes key and returns value.
* **`dict.popitem()`**: Removes and returns last inserted `(key, value)`.
* **`dict.clear()`**: Empties the dictionary.

---

## 4. Set Methods (Unique & Unordered)
Collection of unique elements. `{1, 2, 3}`

### Modifying
* **`set.add(x)`**: Adds element `x`.
* **`set.update(iterable)`**: Adds multiple items.
* **`set.remove(x)`**: Removes `x` (error if missing).
* **`set.discard(x)`**: Removes `x` (no error if missing).
* **`set.pop()`**: Removes random item.

### Math Operations (Return new sets)
* **`set.union(other)`** (`|`): All items in both.
* **`set.intersection(other)`** (`&`): Items only in both.
* **`set.difference(other)`** (`-`): Items in A but not B.
* **`set.symmetric_difference(other)`** (`^`): Items in A or B, but not both.
* **`set.issubset(other)`** (`<=`): Checks if A is inside B.

---

## 5. Advanced "Spicy" Tools
Functions that supercharge iteration.

* **`zip(list1, list2)`**: Combines lists into pairs. `[(a,1), (b,2)]`
* **`enumerate(list)`**: Returns `(index, value)` pairs during loops.
* **`any(list)`**: `True` if *one* item is True.
* **`all(list)`**: `True` if *all* items are True.
* **`filter(func, list)`**: Keeps items where `func(x)` is True.
* **`map(func, list)`**: Applies `func` to every item.
* **List Comprehension**: `[x*2 for x in list]` (Best way to transform lists).
* **Slicing**: `list[::-1]` (Reverse list).

---

## 6. Lambdas (Anonymous Functions)
Single-line functions used on the fly.
**Syntax:** `lambda arguments : expression`

```python
# Sort by second item in tuple
data = [(1, 10), (2, 5)]
data.sort(key=lambda x: x[1]) 

```

---

## 7. Maps, Iterators & Generators

### Map vs List

* **List**: `[1, 2, 3]` - Stores data in RAM. Reusable.
* **Map**: `map(...)` - Calculates data on-demand (Lazy). One-time use.

### Generators (`yield`)

Functions that pause and resume.

```python
def my_gen():
    yield 1
    yield 2 # Pauses here until next() is called

```

### Generator Expressions

Like list comprehensions but with `()`. Uses almost 0 RAM.

```python
gen = (x**2 for x in range(1000000))

```

### Manual Iteration

* **`next(iterator)`**: Manually retrieves the next item.
* **`list(iterator)`**: Forces an iterator to become a standard list.

---

## 8. Quick Comparison Cheat Sheet

| Feature | **List** | **Tuple** | **Set** | **Dict** |
| --- | --- | --- | --- | --- |
| **Syntax** | `[]` | `()` | `{}` | `{k:v}` |
| **Mutable** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| **Ordered** | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |
| **Duplicates** | ✅ Yes | ✅ Yes | ❌ No | ❌ Keys |

| Feature | **List Comp `[]**` | **Gen Expr `()**` |
| --- | --- | --- |
| **Memory** | High (All items) | Low (1 item at a time) |
| **Speed** | Fast Iteration | Efficient Startup |
| **Reuse** | Infinite | One-time only |

```

```