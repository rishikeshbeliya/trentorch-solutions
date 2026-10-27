# DISTINCT Deduplication

Beginner | db

A signup form has a "city" dropdown that should list every city where at least one of your users lives, with each city appearing only once even if many users share it.

Write a query that returns the distinct values of the `city` column of `users`.

### Constraints

- Return only the `city` column
- Each city appears exactly once
- Row order does not matter

### Hints

<details>
<summary>Hint 1</summary>

`DISTINCT` goes right after `SELECT`.

</details>

<details>
<summary>Hint 2</summary>

Selecting `name` as well would make every row unique again, so select only `city`.

</details>
