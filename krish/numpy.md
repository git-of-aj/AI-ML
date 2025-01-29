# What
- NumPy is a Python tool that helps you work with large amounts of numbers quickly and easily. It provides a special kind of list called an array
- For example, with NumPy, you can:

1. Store and organize numbers in a grid-like structure (2D or more).
2. Do math like adding, multiplying, or finding averages across lots of numbers all at once.
3. Perform complex operations like sorting, reshaping, or even doing statistics.
4. Simulate random numbers or solve problems related to things like physics or data science.
> An array is a data structure that stores a fixed-size sequence of elements, all of the same type. Each element can be accessed using an index, with the first element typically having an index of 0. Arrays are used for efficient data storage and retrieval.
- heart of NumPy is something called the `ndarray (short for "N-dimensional array")`. It's like a supercharged list that stores lots of numbers (or other types of data) in a grid or matrix form.
- in ndarray whatever you do with 2 array(list) happens with each element inside (without you write loop) - [docs](https://numpy.org/doc/stable/user/whatisnumpy.html)
- its written in optimised c code so faster.
# Vectorization and brodcast:

### **Vectorization** (Without Loops, But Behind the Scenes)

Think of **vectorization** as **writing mathematical operations more like how you would do them on paper**—using the same symbols and formulas you’re familiar with, but with **no need for explicit loops** or repetitive steps.

#### Here's the key idea:
- **Behind the scenes**, vectorization makes sure that Python doesn’t need to manually loop through each element of an array or list (like we’d have to do in regular Python).
- **Instead**, **NumPy** handles it automatically, doing the element-by-element operations very efficiently **under the hood**, using faster, pre-compiled code (like C).

#### Example:
Imagine you want to **add two lists of numbers** in Python:

Without **vectorization**:
```python
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])  # This loop is slow for large data
```

With **vectorization** in NumPy, you can simply write:
```python
import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = a + b  # No explicit loop needed, NumPy handles it efficiently
```

- This simple `a + b` **does the element-by-element addition** of `a` and `b` without any loops.
- NumPy **handles the looping and indexing** behind the scenes in optimized C code, so the operation is much **faster**.

#### Why is this great?
- **Concise:** Less code to write and read.
- **Fewer bugs:** Since you're not manually writing loops, it's less likely to make mistakes.
- **Closer to math notation:** `a + b` looks like how you'd write it mathematically, making it easier to understand.

### **Broadcasting** (Making Different Shapes Work Together)

**Broadcasting** is a feature that lets NumPy **perform operations on arrays of different shapes** without needing you to manually adjust their sizes or reshape them.

#### Here's the basic idea:
- You can **combine arrays** of **different sizes or shapes** in a way that **NumPy automatically adjusts the smaller array** to fit the larger one (if it makes sense to do so).
- The key is that NumPy will "stretch" or "expand" the smaller array to match the dimensions of the larger one **behind the scenes**.

#### Example 1: Scalar and Array (Different Shape)
Let’s say you have a **single number** (scalar) and an **array**. You want to **multiply each element** of the array by that number:

```python
import numpy as np
a = np.array([1, 2, 3, 4])  # 1D array
b = 2  # Scalar (just a number)
c = a * b  # Broadcasting happens here
```

**What happens behind the scenes?**
- **NumPy "broadcasts"** the scalar `2` over each element of `a`, treating it like the array `[2, 2, 2, 2]`.
- So the operation is like:
  ```python
  c = [1*2, 2*2, 3*2, 4*2]
  c = [2, 4, 6, 8]
  ```
- You didn’t have to manually expand `b` to match the shape of `a`. NumPy did that for you!

#### Example 2: Two Arrays of Different Shapes
What if you wanted to **add two arrays** of **different sizes**? Let's say you have a 2D array (matrix) and a 1D array (vector).

```python
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array (2 rows, 3 columns)
b = np.array([10, 20, 30])  # 1D array (just one row with 3 elements)
c = a + b  # Broadcasting happens here
```

**What happens behind the scenes?**
- **NumPy stretches** the 1D array `b` to match the shape of the 2D array `a` (in this case, it copies the values of `b` to both rows).
- It effectively becomes:
  ```python
  a = [[1, 2, 3], 
       [4, 5, 6]]
  
  b = [[10, 20, 30], 
       [10, 20, 30]]  # Now b has been broadcasted to match a's shape
  ```
- The operation then becomes:
  ```python
  c = [[1+10, 2+20, 3+30], 
       [4+10, 5+20, 6+30]]
  c = [[11, 22, 33], 
       [14, 25, 36]]
  ```

#### Why is broadcasting great?
- You don’t need to manually reshape or duplicate arrays to make them match. NumPy does that **automatically**.
- It **saves memory** and **makes your code more efficient** because you're not creating large temporary arrays.

### To Summarize:

1. **Vectorization**:
   - Makes operations on entire arrays **faster and more concise** by automatically handling element-by-element operations **without explicit loops**.
   - Example: `a + b` adds all elements of `a` and `b` without you needing to write loops.

2. **Broadcasting**:
   - Allows you to perform operations on arrays of different sizes or shapes, **automatically adjusting** the smaller array to match the larger one if it makes sense.
   - Example: You can add a 1D array to a 2D array, and NumPy will **broadcast** the 1D array across all rows of the 2D array.

Both of these features make your code **simpler**, **faster**, and **more Pythonic**, especially when working with large datasets.
