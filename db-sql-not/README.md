# NOT Negation

Beginner | db

A report must exclude a group of users: everyone whose name starts with the letter C. Remember that SQLite's `LIKE` ignores case, so `chris` counts as starting with C.

Write a query returning all columns of `users` where the name does NOT start with 'C'.

### Constraints

- Return all columns
- Exclude every name starting with C or c

### Hints

<details>
<summary>Hint 1</summary>

`NOT` can be placed in front of a condition or in the operator: `NOT LIKE`.

</details>

<details>
<summary>Hint 2</summary>

Reuse the pattern `'C%'`.

</details>
