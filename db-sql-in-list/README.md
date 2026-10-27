# IN List Matching

Beginner | db

Your permissions system applies special rules to a few specific ages. Instead of writing three `OR` conditions, use a list.

Write a query returning all columns of `users` where `age` is one of 12, 16 or 66.

### Constraints

- Return all columns
- Only ages 12, 16 and 66 (exact matches)

### Hints

<details>
<summary>Hint 1</summary>

`IN (...)` takes a comma-separated list of values.

</details>

<details>
<summary>Hint 2</summary>

`age IN (12, 16, 66)` is shorthand for three `=` tests joined with `OR`.

</details>
