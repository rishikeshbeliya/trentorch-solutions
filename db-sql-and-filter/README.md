# AND Compound Filtering

Beginner | db

A mailing campaign targets adult users (age 18 or older) whose name starts with "A". A user has to satisfy **both** conditions to be included.

Write a query returning all columns of `users` where `age >= 18` AND `name` starts with `'A'`.

### Constraints

- Return all columns
- Both conditions must hold: `age >= 18` and the name starts with A
- Row order does not matter

### Hints

<details>
<summary>Hint 1</summary>

Combine the conditions with `AND`.

</details>

<details>
<summary>Hint 2</summary>

`LIKE 'A%'` matches text that starts with A (`%` stands for any run of characters).

</details>
