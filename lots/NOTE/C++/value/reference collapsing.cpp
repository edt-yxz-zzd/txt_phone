
#include <utility> // forward, move
// g++ "reference collapsing.cpp" -std=c++11 -c

template<typename I>
void Call(I i){}
template<typename I, typename T>
void Fwd(T &&v) { Call<I>(std::forward<T>(v)); }


void f()
{
    using I1 = int; // always success
    //using I2 = int const;
    using I3 = int&; // success only for i
    using I4 = int const&; // always success
    using I5 = int&&; // fail for i, k, move(k)
    //using I6 = int const&&;
    int i = 1;
    int const k = 2;

    // 0 - int const; prvalue // prvalue donot have const!!
    // T = int
    Fwd<I1>(0);
    //Fwd<I3>(0); // cannot convert 'std::forward<int>((* & v))' (type 'int') to type 'int&'
    Fwd<I4>(0);
    Fwd<I5>(0);

    // int(0) - int; prvalue
    // T = int
    Fwd<I1>(int(0));
    //Fwd<I3>(int(0)); // cannot convert 'std::forward<int>((* & v))' (type 'int') to type 'int&'
    Fwd<I4>(int(0));
    Fwd<I5>(int(0));

    // std::move(i) - int&&; xvalue
    // T = int
    Fwd<I1>(std::move(i));
    //Fwd<I3>(std::move(i)); // cannot convert 'std::forward<int>((* & v))' (type 'int') to type 'int&'
    Fwd<I4>(std::move(i));
    Fwd<I5>(std::move(i));

    // std::move(k) - int const&&; xvalue
    // T = const int
    Fwd<I1>(std::move(k));
    //Fwd<I3>(std::move(k)); // cannot convert 'std::forward<const int>((* & v))' (type 'const int') to type 'int&'
    Fwd<I4>(std::move(k));
    //Fwd<I5>(std::move(k)); // cannot convert 'std::forward<const int>((* & v))' (type 'const int') to type 'int&&'

    // i - int&; lvalue
    // T = int&
    Fwd<I1>(i);
    Fwd<I3>(i);
    Fwd<I4>(i);
    //Fwd<I5>(i); // cannot convert 'std::forward<int&>((* & v))' (type 'int') to type 'int&&'

    // k - int const&; lvalue
    // T = const int&
    Fwd<I1>(k);
    //Fwd<I3>(k); // cannot convert 'std::forward<const int&>((* & v))' (type 'const int') to type 'int&'
    Fwd<I4>(k);
    //Fwd<I5>(k); // cannot convert 'std::forward<const int&>((* & v))' (type 'const int') to type 'int&&'
}


