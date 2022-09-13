-- Department Top Three Salaries

select d.Name as Department,
       e.Name as Employee,
       Salary
from Employee e left join Department d
on e.DepartmentId = d.Id
where
(select count(distinct Salary) from Employee t1
where t1.DepartmentId = d.Id and t1.Salary >= e.Salary) <= 3
and d.Name is not null
order by d.Id desc;