from game_functions import check_higher_lower

def test_check_higher_lower():
    result1 = check_higher_lower(0,10,'h')
    assert result1==True
    
    result2 = check_higher_lower(0,10,'l')
    assert result2==False
    
    result3 = check_higher_lower(10,0,'h')
    assert result3==False
    
    result4 = check_higher_lower(10,0,'l')
    assert result4==True