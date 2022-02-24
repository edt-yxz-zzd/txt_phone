
r'''

e script/IOps.py


public/protected/private
as_obj/as_obj_ops/as_obj_ops_cls
3*3==>>9 dict!
    obj:user_defined
    obj_ops:as_obj/as_obj_ops
        3*2=6 dict
    obj_ops_cls:as_obj/as_obj_ops/as_obj_ops_cls
        3*3=9 dict
of_obj_at_obj/of_obj_at_obj_ops/of_obj_at_obj_ops_cls///of_obj_ops_at_obj_ops/of_obj_ops_at_obj_ops_cls///of_obj_ops_cls_at_obj_ops_cls
    of_obj_at_obj:
        obj.__dict__[attr]
        obj_ops.of_obj_at_obj[attr:public, obj]
    of_obj_at_obj_ops:
        obj_ops.as_obj_ops[attr:public]
        obj_ops.of_obj_at_obj_ops[attr:public]
    of_obj_at_obj_ops_cls:
        obj_ops_cls.as_obj_ops_cls[attr:public]
        obj_ops_cls.of_obj_at_obj_ops_cls[attr:public]
    of_obj_ops_at_obj_ops:
        obj_ops.as_obj[attr:public]
        obj_ops.of_obj_ops_at_obj_ops[attr:public]
    of_obj_ops_at_obj_ops_cls:
        obj_ops_cls.as_obj_ops[attr:public]
        obj_ops_cls.of_obj_ops_at_obj_ops_cls[attr:public]
    of_obj_ops_cls_at_obj_ops_cls:
        obj_ops_cls.as_obj[attr:public]
        obj_ops_cls.of_obj_ops_cls_at_obj_ops_cls[attr:public]

obj_ops_cls_meta:
    ???
    __getitem__
        obj_ops_cls[]
    obj_ops_cls.__getitem__
        obj_ops[]
obj_ops_cls:
    # * public/protected/private
    .as_obj
        store obj_ops setting
    .as_obj_ops
        store obj const setting
    .as_obj_ops_cls
        store obj const property
    # 3*3=9 dict
obj_ops:
    # * public/protected/private
    .as_obj
        store obj setting
    .as_obj_ops
        store obj const property
    # 3*2=6 dict



get_property
set_property

get_function/method
set_function/method

call_callable_property
call_method_property

      ---
      命名空间 既 区分 private/public/protected，又 区分 of_obj/of_obj_ops/of_obj_ops_cls,
      #as_obj,as_obj_ops,as_obj_ops_cls
        ops[xxx:protected:as_obj_ops, arg...., :, kw:arg...]
          ops[xxx:protected:as_obj_ops](arg...., kwargs={kw:arg...})
          ops[xxx:protected:as_obj_ops](arg...., **kwargs[kw:arg...])
      property:
        @obj
          ops.get_xxx__of_obj_at_obj(obj)
        @obj_ops
          ops.get_xxx__of_obj_at_obj_ops()
          ops.get_yyy__of_obj_ops_at_obj_ops()
        @obj_ops_cls
          type(ops).get_xxx__of_obj_at_obj_ops_cls()
          ops.get_yyy__of_obj_ops_at_obj_ops_cls()
          ops.get_zzz__of_obj_ops_cls_at_obj_ops_cls()
        []:
            ops.of_obj_at_obj["xxx"](obj)
            ops.of_obj_at_obj_ops["xxx"]
            ops.of_obj_at_obj_ops_cls["xxx"]
            ops.of_obj_ops_at_obj_ops["yyy"]
            ops.of_obj_ops_at_obj_ops_cls["yyy"]
            ops.of_obj_ops_cls_at_obj_ops_cls["zzz"]
      ---





-------
===========================
===========================
===========================
3. Data model
3.3.3.1. Metaclasses
    When a class definition is executed, the following steps occur:
        MRO entries are resolved;
        the appropriate metaclass is determined;
        the class namespace is prepared;
        the class body is executed;
        the class object is created.



3.3.3.2. Resolving MRO entries

If a base that appears in class definition is not an instance of type, then an __mro_entries__ method is searched on it. If found, it is called with the original bases tuple. This method must return a tuple of classes that will be used instead of this base. The tuple may be empty, in such case the original base is ignored.

See also

PEP 560 - Core support for typing module and generic types
3.3.3.3. Determining the appropriate metaclass

The appropriate metaclass for a class definition is determined as follows:

    if no bases and no explicit metaclass are given, then type() is used;

    if an explicit metaclass is given and it is not an instance of type(), then it is used directly as the metaclass;

    if an instance of type() is given as the explicit metaclass, or bases are defined, then the most derived metaclass is used.

The most derived metaclass is selected from the explicitly specified metaclass (if any) and the metaclasses (i.e. type(cls)) of all specified base classes. The most derived metaclass is one which is a subtype of all of these candidate metaclasses. If none of the candidate metaclasses meets that criterion, then the class definition will fail with TypeError.
3.3.3.4. Preparing the class namespace

Once the appropriate metaclass has been identified, then the class namespace is prepared. If the metaclass has a __prepare__ attribute, it is called as namespace = metaclass.__prepare__(name, bases, **kwds) (where the additional keyword arguments, if any, come from the class definition).

If the metaclass has no __prepare__ attribute, then the class namespace is initialised as an empty ordered mapping.

See also

PEP 3115 - Metaclasses in Python 3000

    Introduced the __prepare__ namespace hook

3.3.3.5. Executing the class body

The class body is executed (approximately) as exec(body, globals(), namespace). The key difference from a normal call to exec() is that lexical scoping allows the class body (including any methods) to reference names from the current and outer scopes when the class definition occurs inside a function.

However, even when the class definition occurs inside the function, methods defined inside the class still cannot see names defined at the class scope. Class variables must be accessed through the first parameter of instance or class methods, or through the implicit lexically scoped __class__ reference described in the next section.
3.3.3.6. Creating the class object

Once the class namespace has been populated by executing the class body, the class object is created by calling metaclass(name, bases, namespace, **kwds) (the additional keywords passed here are the same as those passed to __prepare__).

This class object is the one that will be referenced by the zero-argument form of super(). __class__ is an implicit closure reference created by the compiler if any methods in a class body refer to either __class__ or super. This allows the zero argument form of super() to correctly identify the class being defined based on lexical scoping, while the class or instance that was used to make the current call is identified based on the first argument passed to the method.

CPython implementation detail: In CPython 3.6 and later, the __class__ cell is passed to the metaclass as a __classcell__ entry in the class namespace. If present, this must be propagated up to the type.__new__ call in order for the class to be initialised correctly. Failing to do so will result in a RuntimeError in Python 3.8.

When using the default metaclass type, or any metaclass that ultimately calls type.__new__, the following additional customisation steps are invoked after creating the class object:

    first, type.__new__ collects all of the descriptors in the class namespace that define a __set_name__() method;

    second, all of these __set_name__ methods are called with the class being defined and the assigned name of that particular descriptor;

    finally, the __init_subclass__() hook is called on the immediate parent of the new class in its method resolution order.

After the class object is created, it is passed to the class decorators included in the class definition (if any) and the resulting object is bound in the local namespace as the defined class.

When a new class is created by type.__new__, the object provided as the namespace parameter is copied to a new ordered mapping and the original object is discarded. The new copy is wrapped in a read-only proxy, which becomes the __dict__ attribute of the class object.

See also

PEP 3135 - New super

    Describes the implicit __class__ closure reference

3.3.3.7. Uses for metaclasses

The potential uses for metaclasses are boundless. Some ideas that have been explored include enum, logging, interface checking, automatic delegation, automatic property creation, proxies, frameworks, and automatic resource locking/synchronization.
3.3.4. Customizing instance and subclass checks

The following methods are used to override the default behavior of the isinstance() and issubclass() built-in functions.

In particular, the metaclass abc.ABCMeta implements these methods in order to allow the addition of Abstract Base Classes (ABCs) as “virtual base classes” to any class or type (including built-in types), including other ABCs.

class.__instancecheck__(self, instance)

    Return true if instance should be considered a (direct or indirect) instance of class. If defined, called to implement isinstance(instance, class).

class.__subclasscheck__(self, subclass)

    Return true if subclass should be considered a (direct or indirect) subclass of class. If defined, called to implement issubclass(subclass, class).

Note that these methods are looked up on the type (metaclass) of a class. They cannot be defined as class methods in the actual class. This is consistent with the lookup of special methods that are called on instances, only in this case the instance is itself a class.

See also

PEP 3119 - Introducing Abstract Base Classes

    Includes the specification for customizing isinstance() and issubclass() behavior through __instancecheck__() and __subclasscheck__(), with motivation for this functionality in the context of adding Abstract Base Classes (see the abc module) to the language.

3.3.5. Emulating generic types

One can implement the generic class syntax as specified by PEP 484 (for example List[int]) by defining a special method:

classmethod object.__class_getitem__(cls, key)

    Return an object representing the specialization of a generic class by type arguments found in key.

This method is looked up on the class object itself, and when defined in the class body, this method is implicitly a class method. Note, this mechanism is primarily reserved for use with static type hints, other usage is discouraged.

See also

PEP 560 - Core support for typing module and generic types
3.3.6. Emulating callable objects

object.__call__(self[, args...])

    Called when the instance is “called” as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).

3.3.7. Emulating container types¶

#'''
i



class OpsMeta(type):
    def __getattribute__(sf, attr):
    def __getattr__(sf, attr):
    def __setattr__(sf, attr, value):
    def __getitem__(sf, key):
    def __setitem__(sf, key, value):




