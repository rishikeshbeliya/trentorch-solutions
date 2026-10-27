# COUNT Aggregation

Beginner | db

The dashboard header shows "N users". Compute N in SQL instead of downloading every row and counting in application code. Some users have not given an email address yet, and they still count as users.

Write a query that returns a single number: how many rows `users` has.

### Constraints

- Return a single row with a single column
- Count every row, including users whose `email` is NULL

### Hints

<details>
<summary>Hint 1</summary>

`COUNT(*)` counts rows.

</details>

<details>
<summary>Hint 2</summary>

`COUNT(column)` skips rows where that column is NULL, which would undercount here.

</details>
