#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name: str, value: Any) -> None:
        if name != 'first_name':
            raise AttributeError((f"'LockedClass' object has no"
                                  f"attribute '{name}'"))
        else:
            super().__setattr__(name, value)
