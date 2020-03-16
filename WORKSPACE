load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "googletest",
    remote = "https://github.com/google/googletest",
    tag = "release-1.8.1",
)

git_repository(
    name = "rules_python",
    remote = "https://github.com/bazelbuild/rules_python",
    commit = "94677401bc56ed5d756f50b441a6a5c7f735a6d4",
    shallow_since = "1573842889 -0500"
)

load("@rules_python//python:pip.bzl", "pip3_import")

pip3_import(
   name = "my_deps",
   requirements = "requirements.txt",
)

load("@my_deps//:requirements.bzl", "pip_install")

pip_install()