
// is_decayed/are_decayed
// is_decayed_v/are_decayed_v
//
#ifndef NN_NS__ARE_DECAYED_HPP
#define NN_NS__ARE_DECAYED_HPP


#include <type_traits>

namespace nn_ns {



// is_decayed/are_decayed
//template<typename T> struct is_decayed;
template<typename T>
struct is_decayed : std::integral_constant<bool
    , std::is_same<T, typename std::decay<T>::type >::value>{};

template<typename... ArgTs>
using are_decayed = std::conjunction<is_decayed<ArgTs>...>;
#if 0
template<typename... ArgTs> struct are_decayed;
template<> struct are_decayed<> : std::integral_constant<bool, true>{};
template<typename T, typename... ArgTs>
struct are_decayed<T, ArgTs...> : std::integral_constant<bool
    , is_decayed<T>::value && are_decayed<ArgTs...>::value>{};
#endif

template<typename T>
constexpr bool is_decayed_v = is_decayed<T>::value;
template<typename... ArgTs>
constexpr bool are_decayed_v = are_decayed<ArgTs...>::value;



}namespace nn_ns {}
#endif // NN_NS__ARE_DECAYED_HPP

