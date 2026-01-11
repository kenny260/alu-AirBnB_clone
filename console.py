#!/usr/bin/python3
"""AirBnB clone command interpreter."""

import cmd
import models
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB console."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User}

    def do_quit(self, arg):
        """Exit the console."""
        return True

    def do_EOF(self, arg):
        """Exit on EOF."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, arg):
        """Create a new instance."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[arg]()
        obj.save()
        print(obj.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
