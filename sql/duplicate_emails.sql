-- Find Duplicate Emails
SELECT Email
FROM person
GROUP BY email
HAVING COUNT(email) > 1;

-- Find distinct Emails
SELECT DISTINCT p1.email
FROM person p1, person p2
WHERE p1.email = p2.email AND p1.id= p2.id;