def test_whatever():
    assert True


# Okay, first thing I always do when testing is make sure that I'm even running
# the right tests. So let's just make a test with `assert False`.  I just name
# it test_whatever - as long as test_ is the start of the function name, it'll
# execute. So go ahead and write that.

#hmmm idk@s
# okay, now ^b<right> and then <up><enter> should launch that test session.
# ^b where ^ is ctrl :) ctrl+b, <right> -- like that. Give it a try?

# Yeeeaah! A sweet sweet successful failure, lol. Okay. So... Let's just do
# something silly. We're going to write tests for an addition function. Nothing
# intense, but I think it should be good. At least as far as a learn-y thing goes, lol.

# OKay, so this plan thing is a thing that I've started doing recently and it's
# *amazing*.

# Let's go ahead and add our first test - we'll need to:
# 1) Import the thing module (should be saltext.vmware_vsphere.modules.thing as thing) 
# 2) write a simple test. Maybe 2+2 = 4? So def test_two_plus_two_should_equal_4():
# and a simple assert thing.add(2,2) == 4 is probably fine.

#################
# Tests Go Here #
#################
# VVVVV -- do you see the error here?
#should it be this?

# from ... import ...  rather than import ... from ...

# but in this case, do import saltext.vmware_vsphere.modules.thing as thing
# should work
# can edit this line with vim like so...
# This is my keypresses:
#+fsd$FtPa r.$ciwhciwas tinghingk
# I'll try to remember to record macros when I'm doing things :D
import saltext.vmware_vsphere.modules.thing as thing
def test_two_plus_two_equals_four():
	assert thing.add(n1=2,n2=2) == 4
# you'll get used to <esc>:w<enter> just being what your fingers do ;)
