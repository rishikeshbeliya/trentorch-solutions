-- Tables available (already created and filled for you):
--
--   CREATE TABLE employees (
--       id INTEGER PRIMARY KEY,
--       name TEXT NOT NULL,
--       manager_id INTEGER
--   )
--
-- Run (Ctrl/Cmd+Enter) executes your query; Submit checks it against the tests.

-- TODO: Return each employee's name as employee and their manager's name as manager. Skip employees who have no manager.

select e.name as employee, f.name as manager from employees as e
join employees as f
  on f.id = e.manager_id
