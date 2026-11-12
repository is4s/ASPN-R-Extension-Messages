#!/usr/bin/env python3

import generated.python.aspn_r_lcm as aspn_r

print(f'param_return: {aspn_r.param_configs().get_hash()}')
print(f'param_return: {aspn_r.param_logging().get_hash()}')
print(f'param_return: {aspn_r.param_request().get_hash()}')
print(f'param_return: {aspn_r.param_return().get_hash()}')
