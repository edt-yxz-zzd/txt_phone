-- e script/lua/variable_shadowing.lua
-- lua script/lua/variable_shadowing.lua
print(x)        -- nil # global
x = 111
do
  print(x)      -- 111 # global
  local x = 222
  print(x)      -- 222 # local
  x = nil
  print(x)      -- nil # local
  x = 333
  print(x)      -- 333 # local
end
print(x)        -- 111 # global
x = 444
print(x)        -- 444 # global

