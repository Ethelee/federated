package(default_visibility = ["//tensorflow_federated/python/research"])

licenses(["notice"])

py_library(
    name = "adapters",
    srcs = ["adapters.py"],
    srcs_version = "PY3",
)

py_library(
    name = "checkpoint_manager",
    srcs = ["checkpoint_manager.py"],
    srcs_version = "PY3",
)

py_test(
    name = "checkpoint_manager_test",
    srcs = ["checkpoint_manager_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [":checkpoint_manager"],
)

py_library(
    name = "checkpoint_utils",
    srcs = ["checkpoint_utils.py"],
    srcs_version = "PY3",
)

py_test(
    name = "checkpoint_utils_test",
    size = "large",
    srcs = ["checkpoint_utils_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [":checkpoint_utils"],
)

py_library(
    name = "fed_avg_schedule",
    srcs = ["fed_avg_schedule.py"],
    srcs_version = "PY3",
    deps = [
        ":adapters",
        "//tensorflow_federated",
    ],
)

py_test(
    name = "fed_avg_schedule_test",
    size = "large",
    srcs = ["fed_avg_schedule_test.py"],
    python_version = "PY3",
    shard_count = 2,
    srcs_version = "PY3",
    deps = [
        ":fed_avg_schedule",
        "//tensorflow_federated",
    ],
)

py_library(
    name = "metrics_manager",
    srcs = ["metrics_manager.py"],
    srcs_version = "PY3",
    deps = [":utils_impl"],
)

py_test(
    name = "metrics_manager_test",
    srcs = ["metrics_manager_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":metrics_manager",
        ":utils_impl",
    ],
)

py_library(
    name = "training_loop",
    srcs = ["training_loop.py"],
    srcs_version = "PY3",
    deps = [
        ":adapters",
        ":checkpoint_manager",
        ":utils_impl",
        "//tensorflow_federated",
    ],
)

py_test(
    name = "training_loop_test",
    size = "large",
    srcs = ["training_loop_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":checkpoint_manager",
        ":fed_avg_schedule",
        ":training_loop",
        "//tensorflow_federated",
    ],
)

py_library(
    name = "training_loops",
    srcs = ["training_loops.py"],
    srcs_version = "PY3",
    deps = ["//tensorflow_federated"],
)

py_test(
    name = "training_loops_test",
    size = "large",
    srcs = ["training_loops_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":training_loops",
        "//tensorflow_federated",
    ],
)

py_library(
    name = "utils_impl",
    srcs = ["utils_impl.py"],
    srcs_version = "PY3",
)

py_test(
    name = "utils_impl_test",
    srcs = ["utils_impl_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [":utils_impl"],
)
