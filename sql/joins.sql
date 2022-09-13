-- combine two table with matching first table  
select p.firstName, p.lastName, a.city, a.state from person p 
left join address a 
on p.personId = a.personId