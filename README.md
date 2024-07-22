# Lab Assignment #6 – Using Maps and Hash Tables

## Exercise 1

**If your first name starts with a letter from A-J inclusively:**

Our *AbstractHashMap* class maintains a load factor l ≤ 0.5. Reimplement
that class to allow the user to specify the maximum load, and adjust the
concrete subclasses accordingly.

Perform experiments on our *ProbeHashMap* classes to measure its
efficiency using random key sets and varying limits on the load factor.
Do you think ProbeHashMap is better or ChainHashMap? When and how?

**Hint** The load factor can be controlled from within the abstract
class, but there must be means for setting the parameter (either through
the constructor, or a new method).

Write a Java/Python application to test your solution.

**If your first name starts with a letter from K-Z inclusively:**

Our *AbstractHashMap* class maintains a load factor l ≤ 0.5. Reimplement
that class to allow the user to specify the maximum load, and adjust the
concrete subclasses accordingly.

Perform experiments on our *ChainHashMap* classes to measure its
efficiency using random key sets and varying limits on the load factor.
Do you think ProbeHashMap is better or ChainHashMap? When and how?

**Hint** The load factor can be controlled from within the abstract
class, but there must be means for setting the parameter (either through
the constructor, or a new method).

Write a Java/Python application to test your solution

(7 marks)

## Exercise 2

**If your first name starts with a letter from A-J inclusively:**

The use of **null** values in a map is problematic, as there is then no
way to differentiate whether a **null** value returned by the call
get(k) represents the legitimate value of an entry (k, null), or
designates that key k was not found. The java.util.Map interface
includes a boolean method, *containsKey(k)*, that resolves any such
ambiguity.

Implement the *containKey(k)* method for the *SortedTableMap* class.
**Hint:** Use the existing *findIndex(k)* method.

Write a Java/Python application to test your solution.

**If your first name starts with a letter from K-Z inclusively:**

Implement the *containKey(k)* method for the *UnSortedTableMap* class.
**Hint:** Use the existing *findIndex(k)* method.

Write a Java/Python application to test your solution.

(3 marks)
