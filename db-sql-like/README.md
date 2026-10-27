# LIKE Pattern Matching

Beginner | db

Your search feature lets support staff find users by email domain. Return everyone whose email address ends with `@example.com`. Addresses such as `carol@example.com.au` (a different domain) and `erin@notexample.com` must not be matched. SQLite's `LIKE` ignores case for ASCII letters, so `dave@EXAMPLE.COM` does count.

Write a query returning all columns of `users` whose `email` ends with `'@example.com'`.

### Constraints

- Return all columns
- The address must **end** with `@example.com`
- Match case-insensitively (the default for SQLite's `LIKE`)

### Hints

<details>
<summary>Hint 1</summary>

`%` in a `LIKE` pattern means "any characters".

</details>

<details>
<summary>Hint 2</summary>

Put the `%` at the start of the pattern so only the ending is fixed.

</details>
