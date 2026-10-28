# Write your MySQL query statement below
# Write your MySQL query statement below
select e.name as Employee
    from employee as e
    inner join employee as b
    on e.managerId=b.id
    where e.salary>b.salary;