## Arrays

**The simplest data structure is the array, which is a contiguous block of memory. It is usually used to represent sequences.**

> Array problems often have simple brute-force solutions that use O(n) space, but there are subtler solutions that use the array itself to reduce space complexity to O(1).
> Filling an array from the front is slow, so see if it’s possible to write values from the back.
> Instead of deleting an entry (which requires moving all entries to its right), consider overwriting it.
> When dealing with integers encoded by an array consider processing the digits from the back of the array. Alternately, reverse the array so the least-significant digit is the first entry.
> Be comfortable with writing code that operates on subarrays.
> It’s incredibly easy to make o-by-1 errors when operating on arrays—reading past the last element of an array is a common error which has catastrophic consequences.
> Don’t worry about preserving the integrity of the array (sortedness, keeping equal entries together, etc.) until it is time to return.
> An array can serve as a good data structure when you know the distribution of the elements in advance. For example, a Boolean array of length W is a good choice for representing a subset
of f0; 1; : : : ;W 􀀀 1g. (When using a Boolean array to represent a subset of f1; 2; 3; : : : ; ng, allocate an array of size n + 1 to simplify indexing.) .
> When operating on 2D arrays, use parallel logic for rows and for columns.
> Sometimes it’s easier to simulate the specification, than to analytically solve for the result. For example, rather than writing a formula for the i-th entry in the spiral order for an n  n matrix,
just compute the output from the beginning.

## I took the above extract from
```
   Elements of Programming Interviews in Python
   The Insider's Guide
   - Adnan Aziz
   - Tsung-Hsien Lee
   - Amit Prakash
   (http://elementsofprogramminginterviews.com/sample/epilight_python_new.pdf)
```