# AVG Averaging

Beginner | db

The reporting screen shows the average age of your users. Calculate it in SQL. One user has no recorded age; that user should not drag the average down.

Write a query that returns a single value: the average of the `age` column of `users`.

### Constraints

- Return a single row with a single column
- Users whose age is NULL are ignored (AVG does this for you)

### Hints

<details>
<summary>Hint 1</summary>

`AVG(column)` averages a numeric column.

</details>

<details>
<summary>Hint 2</summary>

You do not need `WHERE age IS NOT NULL`; aggregates skip NULLs already.

</details>
