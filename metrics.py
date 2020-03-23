import statsd
import get_prefix

def Counter(name):
    return statsd.Counter("%s.%s" % (get_prefix(), name))

    from metrics import Counter

    counter = Counter(__name__)

    coutner +=1
