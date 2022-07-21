# 0x05. Advanced Linear Algebra

## Tasks

### [0. Determinant](./0-determinant.py)

Write a function `def determinant(matrix):` that calculates the determinant of a matrix:

*   `matrix` is a list of lists whose determinant should be calculated
*   If `matrix` is not a list of lists, raise a `TypeError` with the message `matrix must be a list of lists`
*   If `matrix` is not square, raise a `ValueError` with the message `matrix must be a square matrix`
*   The list `[[]]` represents a `0x0` matrix
*   Returns: the determinant of `matrix`

```
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$ ./0-main.py 
    1
    5
    -2
    0
    192
    matrix must be a list of lists
    matrix must be a square matrix
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$
```

---

### [1. Minor](./1-minor.py)

Write a function `def minor(matrix):` that calculates the minor matrix of a matrix:

*   `matrix` is a list of lists whose minor matrix should be calculated
*   If `matrix` is not a list of lists, raise a `TypeError` with the message `matrix must be a list of lists`
*   If `matrix` is not square or is empty, raise a `ValueError` with the message `matrix must be a non-empty square matrix`
*   Returns: the minor matrix of `matrix`

```
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$ ./1-main.py 
    [[1]]
    [[4, 3], [2, 1]]
    [[1, 1], [1, 1]]
    [[-12, -36, 0], [10, -34, -32], [47, 13, -16]]
    matrix must be a list of lists
    matrix must be a non-empty square matrix
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$
```

---

### [2. Cofactor](./2-cofactor.py)

Write a function `def cofactor(matrix):` that calculates the cofactor matrix of a matrix:

*   `matrix` is a list of lists whose cofactor matrix should be calculated
*   If `matrix` is not a list of lists, raise a `TypeError` with the message `matrix must be a list of lists`
*   If `matrix` is not square or is empty, raise a `ValueError` with the message `matrix must be a non-empty square matrix`
*   Returns: the cofactor matrix of `matrix`

```
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$ ./2-main.py 
    [[1]]
    [[4, -3], [-2, 1]]
    [[1, -1], [-1, 1]]
    [[-12, 36, 0], [-10, -34, 32], [47, -13, -16]]
    matrix must be a list of lists
    matrix must be a non-empty square matrix
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$
```

---

### [3. Adjugate](./3-adjugate.py)

Write a function `def adjugate(matrix):` that calculates the adjugate matrix of a matrix:

*   `matrix` is a list of lists whose adjugate matrix should be calculated
*   If `matrix` is not a list of lists, raise a `TypeError` with the message `matrix must be a list of lists`
*   If `matrix` is not square or is empty, raise a `ValueError` with the message `matrix must be a non-empty square matrix`
*   Returns: the adjugate matrix of `matrix`

```
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$ ./3-main.py 
    [[1]]
    [[4, -2], [-3, 1]]
    [[1, -1], [-1, 1]]
    [[-12, -10, 47], [36, -34, -13], [0, 32, -16]]
    matrix must be a list of lists
    matrix must be a non-empty square matrix
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$
```

---

### [4. Inverse](./4-inverse.py)

Write a function `def inverse(matrix):` that calculates the inverse of a matrix:

*   `matrix` is a list of lists whose inverse should be calculated
*   If `matrix` is not a list of lists, raise a `TypeError` with the message `matrix must be a list of lists`
*   If `matrix` is not square or is empty, raise a `ValueError` with the message `matrix must be a non-empty square matrix`
*   Returns: the inverse of `matrix`, or `None` if `matrix` is singular

```
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$ ./4-main.py 
    [[0.2]]
    [[-2.0, 1.0], [1.5, -0.5]]
    None
    [[-0.0625, -0.052083333333333336, 0.24479166666666666], [0.1875, -0.17708333333333334, -0.06770833333333333], [0.0, 0.16666666666666666, -0.08333333333333333]]
    matrix must be a list of lists
    matrix must be a non-empty square matrix
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$
```

---

### [5. Definiteness](./5-definiteness.py)

Write a function `def definiteness(matrix):` that calculates the definiteness of a matrix:

*   `matrix` is a `numpy.ndarray` of shape `(n, n)` whose definiteness should be calculated
*   If `matrix` is not a `numpy.ndarray`, raise a `TypeError` with the message `matrix must be a numpy.ndarray`
*   If `matrix` is not a valid matrix, return `None`
*   Return: the string `Positive definite`, `Positive semi-definite`, `Negative semi-definite`, `Negative definite`, or `Indefinite` if the matrix is positive definite, positive semi-definite, negative semi-definite, negative definite of indefinite, respectively
*   If `matrix` does not fit any of the above categories, return `None`
*   You may `import numpy as np`

```
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$ ./5-main.py 
    Positive definite
    Positive semi-definite
    Negative semi-definite
    Negative definite
    Indefinite
    None
    None
    matrix must be a numpy.ndarray
    alexa@ubuntu-xenial:0x05-advanced_linear_algebra$
```

---
