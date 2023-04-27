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
import numpy as np
import pytest
import mindspore as ms
import mindspore.nn as nn
from mindspore import Tensor


class Net(nn.Cell):
    def construct(self, x):
        return x.aminmax()


@pytest.mark.level0
@pytest.mark.platform_x86_cpu
@pytest.mark.platform_arm_cpu
@pytest.mark.platform_x86_gpu_training
@pytest.mark.platform_arm_ascend_training
@pytest.mark.platform_x86_ascend_training
@pytest.mark.env_onecard
@pytest.mark.parametrize('mode', [ms.GRAPH_MODE, ms.PYNATIVE_MODE])
def test_tensor_aminmax(mode):
    """
    Feature: tensor.aminmax
    Description: Verify the result of tensor.aminmax
    Expectation: success
    """
    ms.set_context(mode=mode)
    x = Tensor(np.array([0.0, 0.4, 0.6, 0.7, 0.1]), ms.float32)
    net = Net()
    output_min, output_max = net(x)
    expect_min = Tensor(np.array([0.0]), ms.float32)
    expect_max = Tensor(np.array([0.7]), ms.float32)
    assert np.allclose(output_min.asnumpy(), expect_min.asnumpy())
    assert np.allclose(output_max.asnumpy(), expect_max.asnumpy())