# Lint as: python3
# Copyright 2018, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from absl.testing import absltest

import numpy as np
import tensorflow as tf

from tensorflow_federated.python.core.api import computation_types
from tensorflow_federated.python.core.api import computations
from tensorflow_federated.python.core.impl import reference_executor
from tensorflow_federated.python.core.impl.context_stack import context_stack_impl
from tensorflow_federated.python.core.impl.context_stack import set_default_executor
from tensorflow_federated.python.core.impl.executors import eager_tf_executor
from tensorflow_federated.python.core.impl.executors import executor_factory

tf.compat.v1.enable_v2_behavior()


class TestSetDefaultExecutor(absltest.TestCase):

  def test_basic_functionality(self):

    @computations.tf_computation(computation_types.SequenceType(tf.int32))
    def comp(ds):
      return ds.take(5).reduce(np.int32(0), lambda x, y: x + y)

    set_default_executor.set_default_executor(
        executor_factory.ExecutorFactoryImpl(
            lambda _: eager_tf_executor.EagerTFExecutor()))

    ds = tf.data.Dataset.range(1).map(lambda x: tf.constant(5)).repeat()
    v = comp(ds)
    self.assertEqual(v, 25)

    set_default_executor.set_default_executor()
    self.assertIn('ExecutionContext',
                  str(type(context_stack_impl.context_stack.current).__name__))

  def test_reference_executor(self):
    set_default_executor.set_default_executor(
        reference_executor.ReferenceExecutor())
    self.assertIsInstance(context_stack_impl.context_stack.current,
                          reference_executor.ReferenceExecutor)

    @computations.tf_computation(computation_types.SequenceType(tf.int32))
    def comp(ds):
      return ds.take(5).reduce(np.int32(0), lambda x, y: x + y)

    ds = tf.data.Dataset.range(1).map(lambda x: tf.constant(5)).repeat(10)
    v = comp(ds)
    self.assertEqual(v, 25)


if __name__ == '__main__':
  absltest.main()
