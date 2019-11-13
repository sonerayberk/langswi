import pytest

from langswi import translate


@pytest.mark.parametrize('input, expected', [
    ('вшы дфв шы ещефд ищтлукы!', 'dis lad is total bonkers!'),
    ('Ешьу 2 ызуфл куфд дфтпгфпу срфз!!!', 'Time 2 speak real language chap!!!'),
    ('njkmrj bp ,jkmijq k.,db r nt,t', 'только из большой любви к тебе')
])
def test_translate(input, expected):
    cooked = translate(input)
    assert expected == cooked
