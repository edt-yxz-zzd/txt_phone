

// PassByValueWhenReadOnly
// ReadOnlyIN/ReadOnlyConstIN
//
// bool PassByValueWhenReadOnly<T>::value - user overload
// ReadOnlyIN<T>, ReadOnlyConstIN<T>
// example:
// how to receive input.cpp ::
//      _F_IMPL::impl, f, Call


#ifndef NN_NS__PASS_BY_VALUE_WHEN_READ_ONLY_HPP
#define NN_NS__PASS_BY_VALUE_WHEN_READ_ONLY_HPP


#include <type_traits>
#include <atomic>

namespace nn_ns {




// what about atomic types???? donot support
template <typename T, typename Enable=void>
struct PassByValueWhenReadOnly
{
    // user should overload the class
    constexpr static
    bool value = false; // pass-by-const-lvalue-reference
    // bool value = true; // pass-by-value
};

//is atomic // donot support
template <typename T>
struct PassByValueWhenReadOnly<std::atomic<T> >{};
    //: std::integral_constant<bool, false>{};

//is_array // pass-by-value
template <typename T>
struct PassByValueWhenReadOnly
        <T, typename std::enable_if<std::is_array<T>::value, void>::type>
    : std::integral_constant<bool, true>{};
//is_fundamental&&is_scalar // pass-by-value
template <typename T>
struct PassByValueWhenReadOnly<T, typename std::enable_if<
            !std::is_array<T>::value
            && (std::is_fundamental<T>::value
                || std::is_scalar<T>::value
                || (std::is_trivially_copyable<T>::value
                    && (sizeof(T) <= sizeof(int) // machine word
                        || sizeof(T) <= sizeof(void*) // object pointer
                        || sizeof(T) <= sizeof(double) // float point number
                        || sizeof(T) <= sizeof(void(*)()) // function pointer
                        )
                    )
                )
            , void>::type>
    : std::integral_constant<bool, true>{};

//is_abstract // pass-by-const-lvalue-reference
template <typename T>
struct PassByValueWhenReadOnly
        <T, typename std::enable_if<std::is_abstract<T>::value, void>::type>
    : std::integral_constant<bool, false>{};





namespace {
template <typename T, bool PassByValue> class _ReadOnlyIN_;
    // typedef (T_ or T_ const&) type;
template <> class _ReadOnlyIN_<void, false>{};
template <> class _ReadOnlyIN_<void, true>{};
template <typename T>
class _ReadOnlyIN_<T, false>
{
    private:typedef typename std::remove_reference<T>::type T_;
    public: typedef T_ const& type;
};
template <typename T>
class _ReadOnlyIN_<T, true>
{
    private:typedef typename std::remove_reference<T>::type T_;
    public: typedef T_ type;
};
template <typename T>
class _ReadOnlyIN_<std::atomic<T>, false>{};
template <typename T>
class _ReadOnlyIN_<std::atomic<T>, true>{};



template<typename T> // T decayed
using _ReadOnlyIN_2 = typename _ReadOnlyIN_<T, PassByValueWhenReadOnly<T>::value>::type;
} namespace {}

template<typename T>
using ReadOnlyIN = _ReadOnlyIN_2<typename std::decay<T>::type>;
template<typename T>
using ReadOnlyConstIN = typename std::add_const<ReadOnlyIN<T> >::type;



/*
struct is_fundamental
  : std::integral_constant<
        bool,
        std::is_arithmetic<T>::value ||
        std::is_void<T>::value  ||
        std::is_same<std::nullptr_t, typename std::remove_cv<T>::type>::value
> {};
template< class T >
struct is_arithmetic : std::integral_constant<bool,
                                              std::is_integral<T>::value ||
                                              std::is_floating_point<T>::value> {};
struct is_scalar : std::integral_constant<bool,
                     std::is_arithmetic<T>::value     ||
                     std::is_enum<T>::value           ||
                     std::is_pointer<T>::value        ||
                     std::is_member_pointer<T>::value ||
                     std::is_null_pointer<T>::value> {};
*/






namespace{
struct _Test_PassByValueWhenReadOnly
{
    void* _1;
    virtual ~_Test_PassByValueWhenReadOnly() = default;
};
struct _Test_PassByValueWhenReadOnly2
    : public virtual _Test_PassByValueWhenReadOnly
{
    void* _2;
};


static_assert(true, "");
static_assert(PassByValueWhenReadOnly<bool>::value, "bool MUST pass-by-value");
static_assert(PassByValueWhenReadOnly<char[2]>::value, "array MUST pass-by-value(decayed)");
static_assert(!PassByValueWhenReadOnly<_Test_PassByValueWhenReadOnly>::value, "abstract class MUST pass-by-reference");
//static_assert(sizeof(_Test_PassByValueWhenReadOnly) == sizeof(void*)*2, "sizeof virtual class");
//  _1 + vtable
//static_assert(sizeof(_Test_PassByValueWhenReadOnly2) == sizeof(void*)*4, "sizeof virtual base class");
//  _1 + vtable + _2 + ptr-to-_Test_PassByValueWhenReadOnly
}namespace {}


}namespace nn_ns {}
#endif// NN_NS__PASS_BY_VALUE_WHEN_READ_ONLY_HPP



