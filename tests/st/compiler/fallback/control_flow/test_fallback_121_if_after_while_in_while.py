# Copyright 2022 Huawei Technologies Co., Ltd
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
""" test graph fallback control flow."""
import numpy as np
from mindspore import Tensor, jit, context
from tests.st.compiler.fallback.cases_register import case_register

context.set_context(mode=context.GRAPH_MODE)


@case_register.level1
@case_register.target_gpu
@case_register.target_ascend
def test_if_after_while_in_while_tensor():
    """
    Feature: JIT Fallback
    Description: Test fallback with control flow.
    Expectation: No exception.
    """
    @jit
    def control_flow_if_after_while_in_while():
        x = Tensor(1)
        y = Tensor(2)
        z = Tensor(0)
        while z < 3:
            z = z + y
            while y > x:
                y -= x
        if x + y >= z and x > y:
            y = y * x - z
        return y
    res = control_flow_if_after_while_in_while()
    assert res == 1


@case_register.level1
@case_register.target_gpu
@case_register.target_ascend
def test_if_after_while_in_while_tensor_2():
    """
    Feature: JIT Fallback
    Description: Test fallback with control flow.
    Expectation: No exception.
    """
    @jit
    def control_flow_if_after_while_in_while():
        x = Tensor(1)
        y = Tensor(2)
        z = Tensor(3)
        while z <= 3:
            z = z + y
            while y >= x:
                y -= x
            x = y - z
        if x + y >= z and not y:
            y = y * x - z
        return y
    res = control_flow_if_after_while_in_while()
    assert res == 0


@case_register.level1
@case_register.target_gpu
@case_register.target_ascend
def test_if_after_while_in_while_numpy():
    """
    Feature: JIT Fallback
    Description: Test fallback with control flow.
    Expectation: No exception.
    """
    @jit
    def control_flow_if_after_while_in_while():
        x = np.array([1, 2, 3, 4])
        y = Tensor(5)
        while y > Tensor(x[3]):
            while y > Tensor(x[0]):
                y -= Tensor(x[1])
        if y != 0:
            y = y + Tensor(sum(x))
        return y
    res = control_flow_if_after_while_in_while()
    assert res == 11
