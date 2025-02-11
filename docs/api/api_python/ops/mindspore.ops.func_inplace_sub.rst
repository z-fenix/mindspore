mindspore.ops.inplace_sub
=========================

.. py:function:: mindspore.ops.inplace_sub(x, v, indices)

    将 `v` 依照索引 `indices` 从 `x` 中减去。计算 :math:`y = x`; :math:`y[i,] -= input\_v`。

    .. note::
        `indices` 只能沿着最高轴进行索引。

    参数：
        - **x** (Tensor) - 输入Tensor，shape为：:math:`(N,*)` ，其中 :math:`*` 表示任何数量的附加维度。
        - **v** (Tensor) - 从 `x` 减去的Tensor。除第一个维度之外shape必须与 `x` 的shape相同。第一个维度必须与 `indices` 的长度相同。数据类型与 `x` 相同。
        - **indices** (Union[int, tuple]) - 待更新值在原Tensor中的索引。取值范围[0, len(x))。若为tuple，则大小与 `v` 的第一维度大小相同。

    返回：
        Tensor，更新后的Tensor。

    异常：
        - **TypeError** - `indices` 不是int或tuple。
        - **TypeError** - `indices` 是元组，但是其中的元素不是int。
        - **ValueError** - `x` 的维度与 `v` 的维度不相等。
        - **ValueError** - `indices` 的长度与 `v.shape[0]` 不相等。
        - **ValueError** - `indices` 的值不属于范围 `[0, x.shape[0])` 。