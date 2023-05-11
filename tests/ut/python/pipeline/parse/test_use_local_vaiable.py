# Copyright 2023 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
""" test use undefined variables for error reporting in control flow scenarios"""
import pytest

import mindspore.nn as nn
from mindspore import Tensor
from mindspore import context
from mindspore import dtype as mstype

context.set_context(mode=context.GRAPH_MODE)


def test_use_local_variable_in_if_true_branch():
    """
    Feature: use undefined variables in if.
    Description: local variable 'y' referenced before assignment.
    Expectation: Raises UnboundLocalError.
    """
    class Net(nn.Cell):
        def construct(self, x):
            if x < 0:
                y = 0
            return y

    net = Net()
    with pytest.raises(UnboundLocalError) as err:
        net(Tensor([1], mstype.float32))
    assert "The local variable 'y'" in str(err.value)


def test_use_local_variable_in_if_false_branch():
    """
    Feature: use undefined variables in if.
    Description: local variable 'y' referenced before assignment.
    Expectation: Raises UnboundLocalError.
    """
    class Net(nn.Cell):
        def construct(self, x):
            if x < 0:
                print(x)
            else:
                y = 0
            return y

    net = Net()
    with pytest.raises(UnboundLocalError) as err:
        net(Tensor([1], mstype.float32))
    assert "The local variable 'y'" in str(err.value)


def test_use_local_variable_in_while_body_branch():
    """
    Feature: use undefined variables in while.
    Description: local variable 'y' referenced before assignment.
    Expectation: Raises UnboundLocalError.
    """
    class Net(nn.Cell):
        def construct(self, x):
            while x < 0:
                y = 0
            return y

    net = Net()
    with pytest.raises(UnboundLocalError) as err:
        net(Tensor([1], mstype.float32))
    assert "The local variable 'y'" in str(err.value)


def test_use_local_variable_in_def_if():
    """
    Feature: use undefined variables in if with defined function.
    Description: local variable 'y' referenced before assignment.
    Expectation: Raises UnboundLocalError.
    """
    class Net(nn.Cell):
        def construct(self, x):
            def func(x):
                if x < 0:
                    y = 0
                return y

            return func(x)

    net = Net()
    with pytest.raises(UnboundLocalError) as err:
        net(Tensor([1], mstype.float32))
    assert "The local variable 'y'" in str(err.value)


def test_use_local_variable_in_def_while():
    """
    Feature: use undefined variables in while with defined function.
    Description: local variable 'y' referenced before assignment.
    Expectation: Raises UnboundLocalError.
    """
    class Net(nn.Cell):
        def construct(self, x):
            def func(x):
                while x < 0:
                    y = 0
                return y

            return func(x)

    net = Net()
    with pytest.raises(UnboundLocalError) as err:
        net(Tensor([1], mstype.float32))
    assert "The local variable 'y'" in str(err.value)