-- Employees Earning More Than Their Managers

-- 1
SELECT e2.name as Employee FROM Employee e1 
      JOIN Employee e2 ON e1.Id = e2.ManagerId  
      WHERE e1.salary < e2.salary
      
-- 2  
SELECT e1.name as Employee FROM Employee e1 JOIN Employee e2 ON e1.ManagerId = e2.Id 
WHERE e1.salary > e2.salary
