import sys, time, lcm
sys.path.append("../generated/python/aspn_r")
import param_configs, param_logging, param_request, param_return

import lcm
import time


lc = lcm.LCM("tcpq://")

logmsg = param_logging.param_logging()
logmsg.elapsed_nsec = 0
logmsg.value="Plane turned left"

requestmsg = param_request.param_request()
requestmsg.elapsed_nsec = 0
requestmsg.num_entries=2
requestmsg.group.append("foo")
requestmsg.group.append("bar")
requestmsg.key.append("big")
requestmsg.key.append("bad")

returnmsg = param_return.param_return()
returnmsg.elapsed_nsec = 0
returnmsg.num_entries=2
returnmsg.group.append("foo")
returnmsg.group.append("bar")
returnmsg.key.append("big")
returnmsg.key.append("bad")
returnmsg.value.append("555")
returnmsg.value.append("999")
returnmsg.return_codes.append(0)
returnmsg.return_codes.append(-1)

msg = param_configs.param_configs()
msg.elapsed_nsec = 0
msg.num_entries=3
msg.group.append("foo")
msg.group.append("bar")
msg.group.append("baz")
msg.key.append("foofoo")
msg.key.append("foobar")
msg.key.append("foobaz")
msg.value.append("5.0")
msg.value.append("string")
msg.value.append("5")



for i in range(10):
    lc.publish("param_configs", msg.encode())
    lc.publish("param_loging", logmsg.encode())
    lc.publish("param_return", returnmsg.encode())
    lc.publish("param_request", requestmsg.encode())
    time.sleep(1)
    msg.elapsed_nsec+=1
    logmsg.elapsed_nsec+=2
    returnmsg.elapsed_nsec+=7
    requestmsg.elapsed_nsec+=9
