#!/usr/bin/env python
#
# https://trinket.io/library/trinkets/0bb2886505
#
# Copyright (c) 2016, Stephen Warren <swarren@wwwdotorg.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from turtle import *

# Screen resolution fixup
# Use 1 on screens with regular resolution
# Use 3 on 3k/4k screens
scale = 1
init_length = 150.0 * scale

def tree(length, n):
  color((0, int(n * 255 / 8.0), 0))

  if n > 7:
    fd(length)
    back(length)
    return

  fd(length)
  lt(30)
  tree(length * 0.5, n + 1)
  rt(90)
  tree(length * 0.7, n + 1)
  lt(60)
  pu()
  back(length)
  pd()

pensize(scale)
colormode(255)
speed(0)
hideturtle()
pu()
back(75 * scale)
lt(90)
back(175 * scale)
pd()
tree(init_length, 0)




print "Press CTRL-C in shell/console to exit"
while True: pass
