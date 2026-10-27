-- Tables available (already created and filled for you):
--
--   CREATE TABLE users (
--       id INTEGER PRIMARY KEY,
--       name TEXT NOT NULL,
--       age INTEGER NOT NULL
--   )
--
-- Run (Ctrl/Cmd+Enter) executes your query; Submit checks it against the tests.

-- TODO: Return all columns for users whose name does NOT start with the letter C.

select *
from users
where name not LIKE "C%"
