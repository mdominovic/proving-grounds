cc_test(
    name = "reverse_integer_test",
    srcs = ["reverse_integer_test.cpp"],
    deps = [
        ":reverse_integer_lib",
        "@googletest//:gtest_main",
    ],
)

cc_library(
    name = "reverse_integer_lib",
    hdrs = ["reverse_integer.hpp"]
)

cc_binary(
    name = "reverse_integer",
    srcs = ["reverse_integer.cpp"],
    deps = [":reverse_integer_lib"]
)