
// https://stackoverflow.com/questions/36933176/how-do-you-static-assert-the-values-in-a-parameter-pack-of-a-variadic-template
// example: static_assert(all_v<f(ArgTs)...>, "");
// C++17 bool_constant, _v
//
// all/any/not_v
// all_v/any_v/not_v
#ifndef NN_NS__BOOL_PACK_HPP
#define NN_NS__BOOL_PACK_HPP

#include <type_traits>


namespace nn_ns {


template<bool...> struct bool_pack; // no definition
template<bool... bs>
using all = std::is_same<bool_pack<bs..., true>, bool_pack<true, bs...> >;
template<bool... bs>
constexpr bool all_v = all<bs...>::value;

template<bool b> struct not_ : std::bool_constant<!b>{};
template<bool b> constexpr bool not_v = !b;
template<bool... bs>
using any = not_<all_v<!bs...> >;
template<bool... bs>
constexpr bool any_v = any<bs...>::value;


}namespace nn_ns {}
#endif // NN_NS__BOOL_PACK_HPP

