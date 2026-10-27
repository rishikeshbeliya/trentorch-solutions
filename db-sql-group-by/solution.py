-- Tables available (already created and filled for you):
--
--   CREATE TABLE orders (
--       id INTEGER PRIMARY KEY,
--       user_id INTEGER NOT NULL,
--       product TEXT NOT NULL,
--       amount INTEGER NOT NULL
--   )
--
-- Run (Ctrl/Cmd+Enter) executes your query; Submit checks it against the tests.

-- TODO: Return each user_id with the number of orders they placed, as order_count.

select user_id, count(product) as order_count from orders
group by user_id
