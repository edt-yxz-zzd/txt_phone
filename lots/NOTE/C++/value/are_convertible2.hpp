
// are_convertible/are_convertible2
// are_convertible2_to
// are_convertible2_v
//
// example:
//  are_convertible<I, O, ...>::value
//  are_convertible2<MkTypeList<I, ...>, MkTypeList<O, ...> >::value
//  are_convertible2_to<I, ...>::to<O, ...>::value
//  are_convertible2_v<MkTypeList<I, ...>, MkTypeList<O, ...> >
#ifndef NN_NS__ARE_CONVERTIBLE2_HPP
#define NN_NS__ARE_CONVERTIBLE2_HPP


#include "TypeList.hpp" // MkTypeList, ListEmpty, ListCon, ...
#include <type_traits>

namespace nn_ns {



template <typename... ArgTs> struct are_convertible;
template <typename A>
struct are_convertible<A>
{
    //static_assert(false, "len(arguments) should be even");
};

template <>
struct are_convertible<> : std::integral_constant<bool, true>{};
template <typename I, typename O, typename... ArgTs>
struct are_convertible<I, O, ArgTs...> : std::integral_constant<bool
     , std::is_convertible<I, O>::value && are_convertible<ArgTs...>::value>{};




template <typename ArgTs1, typename ArgTs2> struct are_convertible2;
template <typename ArgTs1, typename ArgTs2>
    struct are_convertible2
        : std::integral_constant<bool, false>{};

template <>
    struct are_convertible2<ListEmpty, ListEmpty>
        : std::integral_constant<bool, true>{};
template <typename I, typename ArgTs1, typename O, typename ArgTs2>
    struct are_convertible2<ListCon<I, ArgTs1>, ListCon<O, ArgTs2> >
        : std::integral_constant<bool
            , std::is_convertible<I,O>::value
              && are_convertible2<ArgTs1, ArgTs2>::value
            >{};

#if 0
// well I can not findout a specialization of
//  are_convertible2_f/are_convertible2_v
template <typename... InTs
        , std::nullptr_t nul
        , typename... OutTs
        //, typename std::enable_if<sizeof...(InTs) == sizeof...(OutTs)
        //    , std::nullptr_t>::type = nullptr
        >
constexpr bool are_convertible2_f()
{
    static_assert(sizeof...(InTs) == sizeof...(OutTs), "should be same number");
    return are_convertible2<MkTypeList<InTs...>, MkTypeList<OutTs...> >::value;
}


// c++14
template <typename... InTs
        , std::nullptr_t nul
        , typename... OutTs
        >
constexpr bool are_convertible2_v = are_convertible2_f<InTs..., nul, OutTs...>();
#endif

template <typename InsT
        , typename OutsT
        >
constexpr bool are_convertible2_v = are_convertible2<InsT, OutsT>::value;

template <typename... ArgTs1> struct are_convertible2_to;
//template <typename... ArgTs1> struct are_convertible2_to
//    :: template <typename... ArgTs2> struct to;

template <typename... ArgTs1>
struct are_convertible2_to
{
    template <typename... ArgTs2>
    struct to : std::integral_constant<bool
            , are_convertible2<MkTypeList<ArgTs1...>, MkTypeList<ArgTs2...> >::value
            //, are_convertible2_f<ArgTs1..., nullptr, ArgTs2...>()
            //      it seem GCC versions < 5 donot support constexpr yet
            //, are_convertible2_v<ArgTs1..., nullptr, ArgTs2...>
            //      it seem constexpr is a C99 feature, not C++
            //      so, we can use in array, "int array[cexpr];" but not in template argument
            //  https://stackoverflow.com/questions/6354386/is-it-valid-to-use-constexpr-function-as-template-argument
            >{};
};

#if 0
template <>
struct are_convertible2_to<>
{
    template <typename... ArgTs2>
    struct to : std::integral_constant<bool, false>{};
    //template <> struct to<>;
};

template <>
struct are_convertible2_to<>::to<> : std::integral_constant<bool, true>{};

template <typename I, typename... ArgTs1>
struct are_convertible2_to<I, ArgTs1...>
{
    template <typename... ArgTs2>
    struct to : std::integral_constant<bool, false>{};

    template <typename O, typename... ArgTs2>
    struct to<O, ArgTs2...> : std::integral_constant<bool
        , std::is_convertible<I,O>::value
          //&& (typename are_convertible2_to<ArgTs1...>::to<ArgTs2...>)::value
          //&& (typename are_convertible2_to<ArgTs1...>::to)<ArgTs2...>::value
          //&& (template are_convertible2_to<ArgTs1...>::to)<ArgTs2...>::value
          && are_convertible2_to<ArgTs1...>::template to<ArgTs2...>::value
        > : std::integral_constant<bool, true>{};
};
#endif



}namespace nn_ns {}
#endif // NN_NS__ARE_CONVERTIBLE2_HPP

