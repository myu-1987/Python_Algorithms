-- Write an SQL query to rank the scores. The ranking should be calculated according to the following rules:

-- The scores should be ranked from the highest to the lowest.
-- If there is a tie between two scores, both should have the same ranking.
-- After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
-- Return the result table ordered by score in descending order.

-- 1 approch
select s1.Score, 
       (select count(distinct Score) 
                from Scores s2 WHERE s2.Score >= s1.Score)as 'Rank'
from Scores s1
order by s1.Score desc

-- 2 approch
select Score, dense_rank() over(order by Score desc) as 'Rank' from Scores

-- 3 approch
select s.Score, l.Rank 
from Scores s
left join (
    select Score, row_number() over (order by Score desc) as 'Rank' 
    from Scores 
    group by Score
) l on l.Score=s.Score
order by s.Score desc