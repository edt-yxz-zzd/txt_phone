-- e script/lua/numeric_for_loop.lua
-- lua script/lua/numeric_for_loop.lua
for i=0, 9, 1 do
  print(i)
end
-- => [0..=9] === range(10)

print(i)    -- nil
do
  local j = 0
  repeat
    print(j)
    if j == 9 then break end
    j = j+1
  until false
end
print(j)    -- nil

