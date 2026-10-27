# OR Alternative Filtering

Beginner | db

Age-appropriate messaging applies to very young users (under 18) and to seniors (over 65). A user matching **either** condition should be included.

Write a query returning all columns of `users` where `age < 18` OR `age > 65`.

### Constraints

- Return all columns
- Include a row if at least one condition holds
- 18 and 65 themselves are not included

### Hints

<details>
<summary>Hint 1</summary>

Combine the two conditions with `OR`.

</details>

<details>
<summary>Hint 2</summary>

Repeat the column name in each comparison: `age < 18 OR age > 65`.

</details>
