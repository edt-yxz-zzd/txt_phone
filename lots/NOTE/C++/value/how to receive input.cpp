
#include "PassByValueWhenReadOnly.hpp"
#include "are_convertible2.hpp"
#include "are_decayed.hpp"
#include "TypeList.hpp"
#include "bool_pack.hpp"
#include <cstddef> // nullptr_t
#include <utility> // forward, move
#include <type_traits>
#include <cassert>
#include <tuple>


using namespace nn_ns;
#if 0
namespace std{
    /*
    using std::is_trivially_copyable;
    error: 'is_trivially_copyable' is not a member of 'std'
    GCC versions < 5 do not support std::is_trivially_copyable
    */

    template <typename T>
    struct is_trivially_copyable : std::integral_constant<bool, false>{};
}
#endif




























#if 0
template<typename Base, typename... RecTs>
struct Call
{
    //static_assert(are_decayed<RecTs...>::value, "should all decayed");
    template<
        //typename std::enable_if<are_decayed<RecTs...>::value, int>::type=0
            typename... InTs
            >
    static inline auto impl(InTs&&... args)
    {
        static_assert(sizeof...(RecTs) == sizeof...(InTs), "num args should be same");
        return Base::impl<RecTs>(std::forward<InTs>(args)...);
    }
};
#endif


#if 0
template <typename> struct Template1;
template<typename Base
        , typename... BaseImplArgTs
        //, std::nullptr_t
        , template <typename> class
        , typename... RecTs
        //, std::nullptr_t
        , template <typename> class
        , typename... InTs
        //, std::nullptr_t
        , template <typename> class
        >
inline auto call(InTs&&... args) -> decltype(
    Base::template impl<typename std::decay<BaseImplArgTs>::type...>(std::forward<InTs>(args)...)
    )
{
    static_assert(sizeof...(RecTs) == sizeof...(InTs), "num args should be same");
    //static_assert(std::enable_if<are_decayed<RecTs...>::value, "RecTs should be all decayed");
    //static_assert(are_decayed<BaseImplArgTs...>::value, "should all decayed");
    //return Base::template impl<BaseImplArgTs...>(std::forward<InTs>(args)...);
    return Base::template impl<typename std::decay<BaseImplArgTs>::type...>(std::forward<InTs>(args)...);
};
#endif

#if 0
template<typename Base
        , typename BaseImplArgsT    // TypeTuple<...>
        , typename RecsT            // TypeTuple<...>
        , typename InsT             // TypeTuple<...>
        , typename ReturnT=void>
inline ReturnT call();
template<typename Base
        , typename... BaseImplArgTs
        , typename... RecTs
        , typename... InTs
        , typename ReturnT =
            decltype(Base::template impl
                    <typename std::decay<BaseImplArgTs>::type...>
                    (std::forward<InTs>(std::declval<InTs&&>())...))
        >
inline ReturnT call<Base
                , TypeTuple<BaseImplArgTs...>
                , TypeTuple<RecTs...>
                , TypeTuple<InTs...>
                , ReturnT
                >(InTs&&... args)
{
    static_assert(sizeof...(RecTs) == sizeof...(InTs), "num args should be same");
    static_assert...(are_convertible2<InTs, RecTs>::value, "InTs... =[convertible]=>> RecTs...");
    static_assert(std::is_same<ReturnT
                    , decltype(Base::template impl
                            <typename std::decay<BaseImplArgTs>::type...>
                            (std::forward<InTs>(args)...))
                    >
                , "ReturnT should be omit");
    //static_assert(are_decayed<BaseImplArgTs...>::value, "should all decayed");
    return Base::template impl
                <typename std::decay<BaseImplArgTs>::type...>
                (std::forward<InTs>(args)...);
};
#endif


template<typename Base
            // TODO: doc
        , typename BaseImplArgsT    // TypeTuple<...>
                = typename Base::BaseImpl
        , typename RecsT            // TypeTuple<...>
                = typename Base::BaseRecs
        >
struct Call;
template<typename Base
        , typename... BaseImplArgTs
        , typename... RecTs
        >
struct Call<Base
            , TypeTuple<BaseImplArgTs...>
            , TypeTuple<RecTs...>
            >
{
    template <typename... InTs>
    inline static constexpr
    auto call(InTs&&... args)
    {
        static_assert(sizeof...(RecTs) == sizeof...(InTs), "num args should be same");
        static_assert(are_convertible2<MkTypeList<InTs...>, MkTypeList<RecTs...> >::value, "InTs... =[convertible]=>> RecTs...");
        #if 0
        static_assert(std::is_same<ReturnT
                        , decltype(Base::template impl
                                <typename std::decay<BaseImplArgTs>::type...>
                                (std::forward<InTs>(args)...))
                        >
                    , "ReturnT should be omit");
        #endif

        //static_assert(are_decayed<BaseImplArgTs...>::value, "should all decayed");
        return Base::template impl
                    <typename std::decay<BaseImplArgTs>::type...>
                    (std::forward<InTs>(args)...);
    }
};



/////////////////////// example //////////////////////////
#include <iostream>
struct _F_IMPL
{
    // TODO: use InTs2BaseImplsT/InTs2BaseRecsT
    //      instead of BaseImpl/BaseRecs
    typedef TypeTuple<int, int*> BaseImpl;
        // standarded types
        // to min the instances of impl()
    typedef TypeTuple<int, int, int*> BaseRecs;
        // accept what?
    //template <typename... InTs> void InTs2BaseImplsT();
    //template <typename... InTs> void InTs2BaseRecsT();
    template <typename... InTs> TypeTuple<int, int*> InTs2BaseImplsT();
    template <typename... InTs> TypeTuple<int, int, int*> InTs2BaseImplsT();

    template <typename INT1, typename INT2>
    static void impl(int, ReadOnlyConstIN<INT1>, ReadOnlyConstIN<INT2>)
    {
        // called by f only
        static_assert(are_decayed<INT1, INT2>::value, "should all be decayed");
        std::cout << "here" << std::endl;
    }
};



template<typename A, typename B, typename C
    , typename std::enable_if<
        are_convertible<A,int, B,int, C,int*>::value
        && are_convertible2<MkTypeList<A,B,C>, MkTypeList<int,int,int*> >::value
        && are_convertible2_to<A,B,C>::template to<int,int,int*>::value
        //&& are_convertible2_f<A,B,C, nullptr, int,int,int*>()
        , int>::type = 0
    >
inline void f(A&& a, B&& b, C&& c)
{
    _F_IMPL::impl<int, int*>
        // prefect forwarding, actual type determined by _f_impl
        (std::forward<A>(a)

        // T or T const&, determined by ReadOnlyIN/ReadOnlyConstIN
        , std::forward<B>(b)
        , std::forward<C>(c)
        );
}

void t()
{
    int ls[3] = {};
    f(0, 1, ls);
    //call<_F_IMPL, int, int*, nullptr, nullptr, nullptr>();
    //auto h = call<_F_IMPL, int, int*, nullptr, int, int, int*, nullptr, int, int, int (&) [3], nullptr>;
    //auto h = call<_F_IMPL, int, int*, Template1, int, int, int*, Template1, int, int, int (&) [3], Template1>;
    //h(0, 1, ls);
    //auto h = Call<_F_IMPL, TypeTuple<int, int*>, TypeTuple<int, int, int*>, TypeTuple<int, int, int (&) [3]> >::call;
    //h(0, 1, ls);
    Call<_F_IMPL, TypeTuple<int, int*>, TypeTuple<int, int, int*> >::call(0, 1, ls);
    Call<_F_IMPL>::call(0, 1, ls);
}

int main()
{
    t();
    return 0;
}
