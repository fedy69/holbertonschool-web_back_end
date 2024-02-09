-- list all students that have score under 80
-- and no last meeting more than 1 month

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < CURRENT_DATE - INTERVAL 1 MONTH);