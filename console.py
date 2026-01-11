#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exit on EOF."""
        print()
        return True

    def do_quit(self, arg):
        """Quit command."""
        return True

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, arg):
        """Create a new instance."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        obj = classes[args[0]]()
        storage.new(obj)
        storage.save()
        print(obj.id)

    def do_show(self, arg):
        """Show an instance."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)

        if not obj:
            print("** no instance found **")
            return

        print(obj)

    def do_destroy(self, arg):
        """Destroy an instance."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Show all instances."""
        args = shlex.split(arg)
        result = []

        if not args:
            for obj in storage.all().values():
                result.append(str(obj))
            print(result)
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        for key, obj in storage.all().items():
            if key.startswith(args[0] + "."):
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Update an instance."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)

        if not obj:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr = args[2]
        value = args[3]

        if hasattr(obj, attr):
            try:
                value = type(getattr(obj, attr))(value)
            except Exception:
                pass

        setattr(obj, attr, value)
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
