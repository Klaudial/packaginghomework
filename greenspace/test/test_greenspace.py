from nose.tools import assert_true, assert_equal, assert_not_equal, assert_raises
from ..greenspace import show_green_in_png

def checklondongreen():
    assert_equal(show_green_in_png("London"),12006)
        
def checklondonlocation():
    from ..greenspace import geolocate
    assert_equal(geolocate("London"),"(51.5073509, -0.1277583)")
        