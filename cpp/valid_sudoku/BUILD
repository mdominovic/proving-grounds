cc_test(
    name = "valid_sudoku_test",
    srcs = ["valid_sudoku_test.cpp"],
    deps = [
        ":valid_sudoku_lib",
        "@googletest//:gtest_main",
    ],
)

cc_library(
    name = "valid_sudoku_lib",
    hdrs = ["valid_sudoku.hpp"]
)

cc_binary(
    name = "valid_sudoku",
    srcs = ["valid_sudoku.cpp"],
    deps = [":valid_sudoku_lib"]
)