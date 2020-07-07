


template <typename... Ts> struct C{};
template <typename R = void, typename... Ts1, typename T, typename... Ts2, int=0, typename _=void>
R f(T a, C<Ts1...>, C<Ts2...>) {}


template <typename A, typename B> struct CC;
template <typename... As, typename... Bs>
struct CC<CC<As...>, CC<Bs...> >{};


/*
function template vs class template:
* how to get concrete instances?
    when we try to get a function pointer
    we must specify the exacly input argument types
        (R(*)(T,C<...>, C<...>))f
        sometime maybe g<xx, yy> // but for "f" above, this is impossible
    when we try to get a template class
    we must specify at least those non-default parameters
        vector<int>
        vector<int, alloc>
    http://northstar-www.dartmouth.edu/doc/ibmcxx/en_US/doc/language/ref/rncldiff.htm
* how to decl?
    Basic:
        ID
        Template
        Type
        Value
    function template decl:
        FunDeclHead = "template" "<" FunArgX ("," FunArgX)* ">"
        FunArgX  = ClsArg | ClsArgs
            # X - means with/without "..."
    class template decl:
        ClsDeclHead = "template" "<" ClsArg ("," ClsArg)* ("," ClsArgs)? ">"
                    | "template" "<" ClsArgs ">"
        ClsArg  = ClsDeclHead "class" ID? ("=" Template)?
                | "typename" ID? ("=" Type)?
                | Type ID? ("=" Value)?
        ClsArgs = ClsDeclHead "class" "..." ID?
                | "typename" "..." ID?
                | Type "..." ID?

        ClsSpecHead = "template" "<" (ClsArgX ("," ClsArgX)*)? ">"
        ClsSpecArgX = ClsSpecArg | ClsSpecArgs
        ClsSpecArg  = ClsDeclHead "class" ID
                | "typename" ID
                | Type ID
        ClsSpecArgs = ClsDeclHead "class" "..." ID
                | "typename" "..." ID
                | Type "..." ID
    https://stackoverflow.com/questions/14040329/difference-between-class-template-and-function-template
        Function templates attempt to deduce the type of specialization from the argument types.
        Function templates can't be partially specialized while classes can.
        Function templates can't have default template parameters while classes can.
        ----
        Function templates are also able to do type-deduction, which can be useful for creating factory functions
        Class templates can be used to write programs that execute at compile-time (using types as values, and template instantiations with pattern matching as pure functions).
*/
