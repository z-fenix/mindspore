# Copyright 2021 Huawei Technologies Co., Ltd
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

"""Coalesce op"""
from mindspore.ops.op_info_register import op_info_register, AiCPURegOp, DataType
coalesce_op_info = AiCPURegOp("Coalesce") \
    .fusion_type("OPAQUE") \
    .input(0, "x_indices", "required") \
    .input(1, "x_values", "required") \
    .input(2, "x_shape", "required") \
    .output(0, "y_indices", "required") \
    .output(1, "y_values", "required") \
    .output(2, "y_shape", "required") \
    .dtype_format(DataType.I64_Default, DataType.F64_Default, DataType.I64_Default, DataType.I64_Default,
                  DataType.F64_Default, DataType.I64_Default) \
    .dtype_format(DataType.I64_Default, DataType.F32_Default, DataType.I64_Default, DataType.I64_Default,
                  DataType.F32_Default, DataType.I64_Default) \
    .dtype_format(DataType.I64_Default, DataType.F16_Default, DataType.I64_Default, DataType.I64_Default,
                  DataType.F16_Default, DataType.I64_Default) \
    .get_op_info()

@op_info_register(coalesce_op_info)
def _coalesce_aicpu():
    """Coalesce aicpu register"""
    return
