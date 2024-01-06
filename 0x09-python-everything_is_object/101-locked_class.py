#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """
    def __setattr__(self, name: str, value: Any) -> None:
        """ setattr Dunder method """
        if name != 'first_name':
            raise AttributeError((f"'LockedClass' object has no"
                                  f"attribute '{name}'"))
        else:
            super().__setattr__(name, value)
