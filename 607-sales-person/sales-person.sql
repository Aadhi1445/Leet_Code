# Write your MySQL query statement below
select name 
from salesperson
where sales_id not in (
    select sales_id 
    from company 
    join orders
    on company.com_id=orders.com_id
    where company.name='red'
);
-- select *
-- from SalesPerson p
-- left join Orders o 
-- on p.sales_id=o.sales_id
-- left join Company c
-- on o.com_id=c.com_id
-- where c.name!='red';