load("@my_deps//:requirements.bzl", "requirement")

py_test(
    name = "json_parser_test",
    srcs = ["json_parser_test.py"],
    data = ["sorted_comp_notcomp.json"],
    deps = [
        requirement("requests"),
    ]
)

py_binary(
    name = "json_parser",
    srcs = ["json_parser.py", "ToDo.py"],
    main = "json_parser.py",
    deps = [
        requirement("requests"),
    ],
)
