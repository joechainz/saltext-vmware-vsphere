# This is where we're going to write some code. I figure putting it close by
# the rest of the other code is a good idea, since it will get us used to
# having code in the right place.

# Questions/Comments/Concerns?

#sounds good to me

# Alrighty! TDD style: Oh yeah - gonna have to make sure the signature matches.
# Personally, I really like requiring keyword args like this.
#
# questions/comments about requiring keyword args?
# by adding * it allows you to specify the agument when passing in correct?
#
# Well, *requires* it.
#
#                 add(n1, n2)  |  vs  | add(*, n1, n2)
#-----------------------------------------------------
# add(2, 2)           ✓        |      |         X     
# add(2, n2=2)        ✓        |      |         X     
# add(n1=2, n2=2)     ✓        |      |         ✓     
# add(n1=2, 2)        X        |      |         X     
#
# Basically - you don't have to provide keywords if `*` isn't there. *
# FORCES you to have to provide the keywords. This is handy because if
# I add a new argument, e.g. `add(*, n1, n2, something='else') - then nothing
# gets borked. I can also do this:
# add(*, n2, n1) and it still works correctly.
# But if I shuffle the order of non-kwargs then sadness happens, lol.
#
#
# make sense?

#yes, thank you for explaining
# ✓ :)

# OKay, so now if we check the error - None == 4? Hardly. So now it's my turn to "fix" the code. I like taking this approach here...

def add(*, n1, n2):
    # Very good. I was confused cause I was like "Why is it 4 ==2??" Derp XD
    # Another tip - o and O to open the line below and above the current for
    # editing.

    # So this one turns out to be pretty straight forward. Let me introduce a
    # bug though, so we can write some other tests...

    # Okay, so can you write a test to expose this bug?
    #hmmm I think soo
    # (btw, ctrl+w goes to "window" mode - ctrl+w,j will move you to the
    # window down, k up, h and l side to side.

    return n1 + n2

