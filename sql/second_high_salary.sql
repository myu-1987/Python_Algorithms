-- 1
select salary as SecondHighestSalary from employee 
group by salary 
order by  salary desc limit 1,1;

-- 2
SELECT MAX(salary) as SecondHighestSalary
FROM employee 
WHERE salary <> (SELECT MAX(salary) 
FROM employee);