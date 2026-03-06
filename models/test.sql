MODEL (
    name test.full_model,
    kind FULL,
    ignored_rules ['nomissingaudits', 'nomissingunittest']
);

SELECT
 1 AS column_one;