/**
 * Copyright 2021 Huawei Technologies Co., Ltd
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
#ifndef MINDSPORE_INCLUDE_C_API_TYPES_C_H
#define MINDSPORE_INCLUDE_C_API_TYPES_C_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef MS_API
#ifdef _WIN32
#define MS_API __declspec(dllexport)
#else
#define MS_API __attribute__((visibility("default")))
#endif
#endif

typedef enum MSModelType {
  kMSModelTypeMindIR = 0,
  // insert new data type here
  kMSModelTypeInvalid = 0xFFFFFFFF
} MSModelType;

typedef enum MSDeviceType {
  kMSDeviceTypeCPU = 0,
  kMSDeviceTypeGPU,
  kMSDeviceTypeKirinNPU,
  // add new type here
  kMSDeviceTypeInvalid = 100,
} MSDeviceType;

typedef enum MSOptimizationLevel {
  /** Do not change */
  kMSKO0 = 0,
  /** Cast network to float16, keep batchnorm and loss in float32 */
  kMSKO2 = 2,
  /** Cast network to float16, including bacthnorm */
  kMSKO3 = 3,
  /** Choose optimization based on device */
  kMSKAUTO = 4,
  kMSKOPTIMIZATIONTYPE = 0xFFFFFFFF
} MSOptimizationLevel;

typedef enum MSQuantizationType {
  kMSNO_QUANT = 0,
  kMSWEIGHT_QUANT = 1,
  kMSFULL_QUANT = 2,
  kMSUNKNOWN_QUANT_TYPE = 0xFFFFFFFF
} MSQuantizationType;

#ifdef __cplusplus
}
#endif
#endif  // MINDSPORE_INCLUDE_C_API_TYPES_C_H
