/**
 * Copyright 2023 Huawei Technologies Co., Ltd
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef MINDSPORE_NNACL_KERNEL_MATMUL_F32_BASE_H_
#define MINDSPORE_NNACL_KERNEL_MATMUL_F32_BASE_H_

#include "nnacl/op_base.h"
#include "nnacl/tensor_c.h"
#include "nnacl/matmul_parameter.h"
#include "nnacl/kernel/matmul_base.h"

void MatmulFp32Base_GetThreadCuttingPolicy(MatmulFp32Struct *matmul);
void MatmulFp32Base_FreeBatchOffset(MatmulFp32Struct *matmul);
int MatmulFP32Base_MallocBatchOffset(MatmulFp32Struct *matmul);
int MatmulFp32Base_InitParameter(MatmulFp32Struct *matmul);
int matmul_f32_prepare(KernelBase *self);
int matmul_f32_resize(KernelBase *self);
int matmul_f32_release(KernelBase *self);
KernelBase *CreateMatmulFp32Base();
KernelBase *CreateMatmulFp32();

#endif  // MINDSPORE_NNACL_KERNEL_MATMUL_F32_BASE_H_