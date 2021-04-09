import saltext.vmware_vsphere.modules.joey as joey

def test_dance_return():
    assert joey.dance() == 'shake a leg'

def test_add_one_plus_one():
    assert joey.add(num1=1,num2=1) == 2

def test_add_two_plus_ten():
    assert joey.add(num1=2,num2=10) == 12

def test_add_neg_two_plus_ten():
    assert joey.add(num1=-2,num2=10) == 8