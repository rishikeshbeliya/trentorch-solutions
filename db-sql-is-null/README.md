# IS NULL Checking

Beginner | db

A data-quality audit needs to find incomplete user records. Some users have no email recorded at all (the value is `NULL`). One user has an _empty string_ instead, which is a different thing and is not part of this audit.

Write a query returning all columns of `users` where `email` IS NULL.

### Constraints

- Return all columns
- Only rows where `email` is NULL
- An empty string `''` is not NULL

### Hints

<details>
<summary>Hint 1</summary>

`= NULL` never matches anything; SQL has a dedicated operator.

</details>

<details>
<summary>Hint 2</summary>

Use `IS NULL`, and `IS NOT NULL` for the opposite.

</details>
