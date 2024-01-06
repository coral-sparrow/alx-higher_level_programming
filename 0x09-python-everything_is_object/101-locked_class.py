#!/usr/bin/python3
""" LockedClass to control attributes creation """


class LockedClass:
    """ The LockedClass """
    def __setattr__(self, name: str, value: Any) -> None:
        """ setattr Dunder method """
        if name != 'first_name':
            raise AttributeError((f"'LockedClass' object has no"
                                  f"attribute '{name}'"))
        else:
            super().__setattr__(name, value)
