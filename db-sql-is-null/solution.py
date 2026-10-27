-- Tables available (already created and filled for you):
--
--   CREATE TABLE users (
--       id INTEGER PRIMARY KEY,
--       name TEXT NOT NULL,
--       email TEXT
--   )
--
-- Run (Ctrl/Cmd+Enter) executes your query; Submit checks it against the tests.

-- TODO: Return all columns for users whose email is NULL.
select *
from users
where email is NULL
