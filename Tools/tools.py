def get_external_ip():
    """get external IP """
    ip = run("wget -qO- ipecho.net/plain")
    print "The external IP is: %s" % ip