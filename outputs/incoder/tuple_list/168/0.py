
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest third value.
    """
    
    lst = sorted(lst)
    
    return lst[2]
</cell>
<cell>
# Test your extract_value function below
v1 = [
    ('Archery', 80000, 1),
    ('Bayonet', 60000, 2),
    ('Bruce', 60000, 3),
    ('Bruce', 70000, 4),
    ('Bruce', 80000, 5),
    ('Bruce', 90000, 6),
    ('Bruce', 100000, 7),
    ('Bruce', 110000, 8),
    ('Bruce', 120000, 9),
    ('Bruce', 130000, 10),
    ('Bruce', 140000, 11),
    ('Bruce', 150000, 12),
    ('Bruce', 160000, 13),
    ('Bruce', 170000, 14),
    ('Bruce', 180000, 15),
    ('Bruce', 190000, 16),
    ('Bruce', 210000, 17),
    ('Bruce', 220000, 18),
    ('Bruce', 230000, 19),
    ('Bruce', 240000, 20),
    ('Bruce', 250000, 21),
    ('Bruce', 260000, 22),
    ('Bruce', 270000, 23),
    ('Bruce', 280000, 24),
    ('Bruce', 290000, 25),
    ('Bruce', 310000, 26),
    ('Bruce', 320000, 27),
    ('Bruce', 330000, 28),
    ('Bruce', 340000, 29),
    ('Bruce', 350000, 30),
    ('Bruce', 360000, 31),
    ('Bruce', 370000, 32),
    ('Bruce', 380000, 33),
    ('Bruce', 390000, 34),
    ('Bruce', 410000, 35),
    ('Bruce', 420000, 36),
    ('Bruce', 430000, 37),
    ('Bruce', 440000, 38),
    ('Bruce', 450000, 39),
    ('Bruce', 460000, 40),
    ('Bruce', 470000, 41),
    ('Bruce', 480000, 42),
    ('Bruce', 490000, 43),
    ('Bruce', 500000, 44),
    ('Bruce', 510000