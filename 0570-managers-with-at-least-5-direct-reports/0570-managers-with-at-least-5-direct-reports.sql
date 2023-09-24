# Write your MySQL query statement below
with managerReports as
    (select managerId, count(id) as numReports from Employee group by managerId)
select  name  from managerReports join Employee where managerReports.managerId = Employee.id and numReports >= 5;