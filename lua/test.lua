-- array = {"Lua", "Tutorial"}

-- for i= 1, 2 do
--    print(array[i])
-- end

-- mytable = {
--     var1 = function() print(11); end,
--     [2] = 'hello'
-- }

-- mymetatable = {
--     __index = {var1 = function() print(22); end}
-- }
-- setmetatable(mytable, mymetatable);
-- mytable.var1();
-- b = getmetatable(mytable)
-- for k,v in pairs(b) do
--     print(k, v)
-- end

-- for k,v in pairs(mytable) do
--     print(k, v)
-- end

-- mytable = setmetatable({key1 = "value1"}, {
--     __index = function(tbl, key)
--         if key == "key2" then
--             return tbl.key1
--         else
--             return nil
--         end
--     end
-- })

-- print(mytable.key1, mytable.key2)

-- mytable = setmetatable({key1 = "value1"}, {
--     __newindex = function(tbl, k, v)
--         rawset(tbl, k, "\"" .. v .. "\"")
--     end
-- })
-- mytable.key1 = "new value"
-- mytable.key2 = 4
-- print(mytable.key1, mytable.key2)

-- function table_maxn(t)
--     local mn = 0
--     for k, v in pairs(t) do
--         if mn < k then
--             mn = k
--         end
--     end
--     return mn
-- end

-- mytable = setmetatable({10}, {
--     __call = function(tbl1, tbl2)
--         sum = 0
--         for i = 1, table_maxn(tbl1) do
--             sum = sum + tbl1[i]
--         end
--         for i = 1, table_maxn(tbl2) do
--             sum = sum + tbl2[i]
--         end
--         return sum
--     end
-- })
-- newtable = {10,20,30}
-- print(mytable(newtable))
-- b = getmetatable(mytable)
-- for k,v in pairs(b) do
--     print(k, v)
-- end

-- mytable = setmetatable({10,20,30},{
--     __tostring = function(tbl)
--         sum = 0
--         for k, v in pairs(tbl) do
--             sum = sum + v
--         end
--         return "total count:" .. sum;
--     end
-- })
-- print(mytable)

-- b = 0
-- print(b)

-- function myfunc()
--     print(debug.traceback("Stack trace"))
--     -- print(debug.getinfo(1))
--     print("Stack trace end")
-- end
-- -- myfunc()
-- -- print(debug.getinfo(1))
-- for k,v in pairs(debug.getinfo(1)) do
--     print(k, v)
-- end

-- function newCounter()
--     local n = 0
--     local k = 0
--     return function()
--         k = n
--         n = n + 1
--         return n
--     end
-- end

-- counter = newCounter()
-- print(counter())
-- print(counter())

-- local i = 1
-- repeat
--     name, val = debug.getupvalue(counter, i)
--     if name then
--         print("index:", i, name, "=", val)
--         if name == "n" then
--             debug.setupvalue(counter, 2, 10)
--         end
--         i = i+1
--     end
-- until not name
-- print(counter())
-- print(i)

-- a,b = 100,200;
-- print(a,b)
