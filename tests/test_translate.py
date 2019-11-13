import pytest

from translator import translate


@pytest.mark.parametrize('input, expected', [
    ('вшы дфв шы ещефд ищтлукы!', 'dis lad is total bonkers!'),
    ('Ешьу 2 ызуфл куфд дфтпгфпу срфз!!!', 'time 2 speak real language chap!!!'),  # TODO: Capital `T`
    ('njkmrj bp ,jkmijq k.,db r nt,t', 'только из большой любви к тебе')
])
def test_translate(input, expected):
    cooked = translate(input)
    assert expected == cooked