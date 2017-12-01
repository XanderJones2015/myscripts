def ping(hostname):
    import os
    response = not os.system('ping %s -n 1' % (hostname,))
    if response == 1:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    return pingstatus
