-- Tables available (already created and filled for you):
--
--   CREATE TABLE users (
--       id INTEGER PRIMARY KEY,
--       name TEXT NOT NULL
--   )
--
--   CREATE TABLE orders (
--       id INTEGER PRIMARY KEY,
--       user_id INTEGER NOT NULL,
--       product TEXT NOT NULL
--   )
--
-- Run (Ctrl/Cmd+Enter) executes your query; Submit checks it against the tests.

-- TODO: Return id, name and order_count for every user, including users with no orders.
select u.id, u.name, count(o.id) as order_count
from users u
left join orders o
 on o.user_id = u.id
group by u.id, u.name;
