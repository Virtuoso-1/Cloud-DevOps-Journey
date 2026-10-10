from chapter_11 import Employee

def test_give_default_raise():
    """Test if the default raise works"""
    employee1 = Employee('Seun', 'Olubode', 3000)
    assert employee1.give_raise() == 8000


def test_give_custom_raise():
    """Test if the given raise works"""
    employee1 = Employee('Seun', 'Olubode', 3000)
    assert employee1.give_raise(2000) == 5000
