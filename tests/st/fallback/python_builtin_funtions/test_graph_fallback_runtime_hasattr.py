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

import pytest
import numpy as np
from mindspore import Tensor, context
import mindspore as ms

context.set_context(mode=context.GRAPH_MODE)


@pytest.mark.level0
@pytest.mark.platform_x86_gpu_training
@pytest.mark.platform_arm_ascend_training
@pytest.mark.platform_x86_ascend_training
@pytest.mark.env_onecard
def test_fallback_hasattr_custom_class():
    """
    Feature: JIT Fallback
    Description: Test hasattr in fallback runtime
    Expectation: No exception.
    """

    class UserDefinedNet:
        def __init__(self):
            self.net_value = 10

    class UNet(ms.nn.Cell):
        def __init__(self, net):
            super().__init__()
            self.net = net

        def construct(self):
            return hasattr(self.net, "net_value")

    res = UNet(UserDefinedNet())
    assert res


@pytest.mark.level0
@pytest.mark.platform_x86_gpu_training
@pytest.mark.platform_arm_ascend_training
@pytest.mark.platform_x86_ascend_training
@pytest.mark.env_onecard
def test_fallback_hasattr_asnumpy():
    """
    Feature: JIT Fallback
    Description: Test hasattr in fallback runtime
    Expectation: No exception.
    """

    class Net(ms.nn.Cell):
        def construct(self):
            x = Tensor(np.array([1, 2, 3, 4])).asnumpy()
            return hasattr(x, "__len__")

    res = Net()
    assert res