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
   return 4


# Success! :troll: But also... good! Because the idea is that you should only write the minimum amount of code to pass tests means you have to test things that you need. So lets go ahead and commit this...
