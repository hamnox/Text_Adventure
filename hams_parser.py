import parsley #do add this into the installer or whatever.
import sys
thismodule = sys.modules[__name__]

def use(thing):
    print thing.upper(), "WORKS"
    
x = parsley.makeGrammar("""
toplevel = pairs+ | 'quit'
pairs = command:cmd ws thing:this ws? -> cmd,this
command = use | go | custom
use = ('use' ' the'? | 'try' 'the'?):txt -> "use"
go = ('go' ' to'? | 'walk' ' to'?):txt -> 'goto'
custom = ('cucumber walowitz'):txt -> 'walowitz'
thing = ('bathroom' | 'genius')""",{}) #{"rule": function/object"}


#result = x('use the bathroom try genius').toplevel()


#next must add a method for extending grammar
"""for pair in result:
    methodToCall = getattr(thismodule, pair[0])
    methodToCall(pair[1])"""