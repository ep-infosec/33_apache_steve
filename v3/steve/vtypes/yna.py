#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----
#
# ### TBD: DOCCO
#

# The votestring will be lower-cased. What is the result?
YES = { 'y', 'yes', '1', 'true', }
NO = { 'n', 'no', '0', 'false', }
# "abstain" is any other (non-affirmative) value.


def tally(votestrings, kv):
    y = n = a = 0
    for v in votestrings:
        if v in YES:
            y += 1
        elif v in NO:
            n += 1
        else:
            a += 1

    human = f'''\
Yes:     {y:#4}
No:      {n:#4}
Abstain: {a:#4}'''

    return human, {'y': y, 'n': n, 'a': a,}
