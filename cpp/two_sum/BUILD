cc_test(
    name = "two_sum_test",
    srcs = ["two_sum_test.cpp"],
    deps = [
        ":two_sum_lib",
        "@googletest//:gtest_main",
    ],
)

cc_library(
    name = "two_sum_lib",
    hdrs = ["two_sum.hpp"]
)

cc_binary(
    name = "two_sum",
    srcs = ["two_sum.cpp"],
    deps = [":two_sum_lib"]
)