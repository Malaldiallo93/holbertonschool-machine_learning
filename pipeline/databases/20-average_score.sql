-- Procedure that computes and store average score for a student
DROP TRIGGER IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT)

    BEGIN
        UPDATE users
        SET average_score = (
                SELECT AVG(score)
                FROM corrections
                WHERE corrections.user_id = user_id)
        WHERE id = user_id;

    END $$

DELIMITER;