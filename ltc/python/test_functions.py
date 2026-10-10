from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Olamide Olubode' work?"""
    formatted_name = get_formatted_name('olamide', 'olubode')
    assert formatted_name == 'Olamide Olubode'

def test_first_last_middle_name():
    """Do name like 'Isaac Ufuooma Ejemudaro' work? """
    formatted_name = get_formatted_name('isaac', 'ejemudaro', 'ufuooma')
    assert formatted_name == 'Isaac Ufuooma Ejemudaro'
