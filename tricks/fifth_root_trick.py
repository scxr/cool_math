def trick_main(number):
    result = None
    temp_cnt = 10
    if number < 100_000:
        return int(str(number)[len(str(number))-1])
    if number == 100_000:
        return 10
    while result is None:
        if temp_cnt ** 5 <= number:
            pass
        else:
            result = temp_cnt - 10 + int(str(number)[len(str(number))-1])
        temp_cnt += 10
    return result

def tests():
    assert trick_main(32) == 2, 'should be 10'
    assert trick_main(100000) == 10, 'should be 10'
    assert trick_main(161051) == 11, 'should be 11'
    assert trick_main(371293) == 13, 'should be 13'
    assert trick_main(1048576) == 16, 'should be 16'
    assert trick_main(3200000) == 20, 'should be 20'
    assert trick_main(9765625) == 25, 'should be 25'
    assert trick_main(28629151) == 31, 'should be 31'
    assert trick_main(79235168) == 38, 'should be 38'
    assert trick_main(205962976) == 46, 'should be 46'
    assert trick_main(539218609632) == 222, 'should be 222'
    assert trick_main(518797610148157) == 877, 'should be 877'



if __name__ == "__main__":
    tests()
    print('tests passed')
