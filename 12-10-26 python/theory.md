1.List - list
Ordered . Mutable . Duplicates allowed
Use when data may change, such as a shopping cart or student marks.

2.Tuple - tuple
Ordered . Immutable . Duplicates allowed
Use when a group of values should remain fixed, such as coordinates.

3.Dictionary - dict
Key-value pairs . Mutable . Unique keys
Use when each value needs a meaningful label, such as a student's name and marks.

4.Set - set
Unique elements . Mutable . Unordered
Use when you need unique values, such as finding distinct email addresses or removing
duplicates.

=================================================================================================================================

. Ordered: The collection preserves a defined order. Lists and tuples support indexing; dictionaries
preserve insertion order.
. Mutable: The collection can be modified after creation.
. Immutable: The collection cannot be modified after creation.
. Duplicates: Whether repeated elements are allowed.

A set does not guarantee a useful or stable display order, and it does not support indexing.

=================================================================================================================================

4.3 Tuple operations and methods

Operation

Access

Slice

Count

Find index

Length

Membership

Loop

Sort

Convert

=================================================================================================================================
Example

t[0]

t[1:3]

t.count(10)

t.index(20)

len(t)

20 in t

for x in t:

sorted(t)

list(t)

=================================================================================================================================
Purpose

Get an element

Get a portion

Count occurrences

Find first matching index

Count elements

Check whether an item exists

Visit each element

Return a sorted list

Convert to a list

=================================================================================================================================

3.2 List operations and methods

Operation

Access

Update

Add one item

Insert

Extend

Remove by value

Remove by index

Delete

Clear

Find index

Count

Sort

Reverse

Copy

=================================================================================================================================
Example

fruits[0]

fruits[0] = "Grapes"

fruits.append("Kiwi")

fruits.insert(1, "Guava")

fruits.extend(["kiwi", "pear"])

fruits.remove("Mango")

fruits.pop(ø)

del fruits[e]

fruits.clear()

fruits. index("Banana")

fruits.count("Apple")

fruits.sort()

fruits.reverse()

fruits.copy()

=================================================================================================================================
Purpose

Get an item

Change an item

Add at the end

Add at a specific index

Add multiple items

Remove first matching value

Remove and return an item

Delete an item

Remove all items

Find first matching index

Count occurrences

Sort the list in place

Reverse the current order

Make a shallow copy

=================================================================================================================================

Important dictionary methods:

Method

get(key)

keys()

values()

items()

update()

pop(key)

popitem()

setdefault()

clear()

copy()

=================================================================================================================================
Purpose

Safely retrieve a value

Get a view of all keys

Get a view of all values

Get key-value pairs

Add or update multiple entries

Remove a key and return its value

Remove and return the last inserted pair

Return a value, inserting a default if absent

Remove all entries

Create a shallow copy

=================================================================================================================================

Method

add()

update()

remove()

discard()

pop()

clear()

copy()

issubset()

issuperset()

isdisjoint()

=================================================================================================================================

Use

Add one element

Add multiple elements

Remove an element; error if absent

Remove an element if present

Remove and return an arbitrary element

Remove all elements

Create a shallow copy

Check whether one set is contained in another

Check whether a set contains another

Check whether two sets share no elements