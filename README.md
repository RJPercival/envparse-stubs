# Type stubs for envparse

This package adds type annotations for the [envparse](https://github.com/rconradharris/envparse) library.

## Known Issues

- The `force` and `preprocessor` parameters have been omitted.
- A `default` value of `None` is not allowed for `list()`, `set()`, `tuple()` or `dict()`. Instead, use an empty list/set/tuple/dict
  as the default.
- A schema cannot be provided to `Env.__init__()`, as this would make it impossible to infer the return types of other methods.

## Author

[Rob Percival](https://www.linkedin.com/in/robpercival/)
