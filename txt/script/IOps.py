
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
#'''
i



class OpsMeta(type):
    def __getattribute__(sf, attr):
    def __getattr__(sf, attr):
    def __setattr__(sf, attr, value):
    def __getitem__(sf, key):
    def __setitem__(sf, key, value):




