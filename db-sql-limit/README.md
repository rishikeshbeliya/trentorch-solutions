# LIMIT Pagination

Beginner | db

The admin screen lists users two per page, ordered by `id`. Page 1 shows users 1 and 2; page 2 shows users 3 and 4.

Write a query that returns page 2: all columns of `users`, ordered by `id`, skipping the first 2 rows and returning the next 2.

### Constraints

- Order the rows by `id` ascending
- Skip the first 2 rows and return exactly the next 2
- Return all columns

### Hints

<details>
<summary>Hint 1</summary>

`LIMIT n` caps the number of rows; `OFFSET m` skips rows first.

</details>

<details>
<summary>Hint 2</summary>

Pagination only makes sense with an `ORDER BY`, otherwise pages are arbitrary.

</details>
