-- e script/lua/generic_for_loop.lua
-- lua script/lua/generic_for_loop.lua

days = { "monday", "tuesday", "wednesday", "thursday" }
function walk(array)
  local index = 0
  return function()
    index = index + 1
    return array[index]
  end
end
for day in walk(days) do
  print (day)
end
-- iterator_factory :: ... -> (iterator_function, invariant_state, control_variable)
-- iterator_function :: invariant_state -> non_nil-control_variable -> (nil-or-next-control_variable, assoc_result)
-- invariant_state === self/this
-- control_variable ~~~ key/idx
function iterator_factory()
  iterator_function = function (a,b,c,d)
    print(111, a,b,c,d)
      if b==664 then return nil end
      return b-1, 888
  end
  invariant_state = 999
  control_variable = 666
  return iterator_function, invariant_state, control_variable
end
for a,b,c,d in iterator_factory() do
    print(333, a,b,c,d)
end

-- output:
-- monday
-- tuesday
-- wednesday
-- thursday
-- 111     999     666     nil     nil
-- 333     665     888     nil     nil
-- 111     999     665     nil     nil
-- 333     664     888     nil     nil
-- 111     999     664     nil     nil

