
// TypeTuple TypeList ListCon ListEmpty TupleCon
// TypeTuple2TypeList TypeList2TypeTuple
// MkTypeList GetArgsAs
#ifndef NN_NS__TYPE_LIST_HPP
#define NN_NS__TYPE_LIST_HPP

namespace nn_ns {



template <typename... ArgTs> struct TypeTuple; // no definition
template <typename A, typename B> struct ListCon; // no definition
struct ListEmpty; // no definition
template <typename... ArgTs> struct TypeList;
template <>
struct TypeList<>
{
    typedef ListEmpty type;
};
template <typename T, typename... ArgTs>
struct TypeList<T, ArgTs...>
{
    typedef ListCon<T, typename TypeList<ArgTs...>::type> type;
};
template <typename... ArgTs>
using MkTypeList = typename TypeList<ArgTs...>::type;


template <typename T, typename Tpl> struct TupleCon;
template <typename T, typename... ArgTs>
struct TupleCon<T, TypeTuple<ArgTs...> >
{
    typedef typename TypeTuple<T, ArgTs...>::type type;
};


template <template<typename...> class TP_OUT, typename I> struct GetArgsAs;
template <template<typename...> class TP_OUT
        , template<typename...> class TP_IN, typename... ArgTs>
struct GetArgsAs<TP_OUT, TP_IN<ArgTs...> >
{
    typedef TP_OUT<ArgTs...> type;
};

template <typename Tpl> struct TypeTuple2TypeList;
template <typename... ArgTs>
struct TypeTuple2TypeList<TypeTuple<ArgTs...> >
{
    typedef typename TypeList<ArgTs...>::type type;
};


template <typename Ls> struct TypeList2TypeTuple;
template <>
struct TypeList2TypeTuple<ListEmpty>
{
    typedef TypeTuple<> type;
};
template <typename T, typename Ls>
struct TypeList2TypeTuple<ListCon<T, Ls> >
{
    typedef typename TupleCon<T, TypeList2TypeTuple<Ls> >::type type;
};



}namespace nn_ns {}
#endif // NN_NS__TYPE_LIST_HPP

