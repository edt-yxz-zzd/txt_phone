
#include <utility> // forward, move
#include <type_traits>
#include <cassert>


//https://www.codesynthesis.com/~boris/blog/2012/06/26/efficient-argument-passing-cxx11-part2/



template <typename T>
struct InParam
{

    // Accessors.
    //
    bool is_lvalue() const {return case_ == LVALUE;}
    bool is_rvalue() const {return case_ != LVALUE;}

    operator T const&() const {return get();}
    T const& get() const {return *lv_;}//{return is_lvalue()? *lv_ : *rv_;}
    T&& move_as_xvalue()&&
        {
            if (is_lvalue()) throw "move_as_xvalue but initial by lvalue";
            // if (!rv_) throw "has move out"; after assign to other
            return std::move(*rv_);
        }


    // Move. Returns a copy if lvalue.
    //
    T move_as_prvalue()&& {return is_lvalue()? *lv_ : std::move(*rv_);}
    T force_move(){return std::move(*this).move_as_prvalue();}


    // Support for implicit conversion via perfect forwarding.
    //
    template <typename ArgT,
            typename std::enable_if<
              std::is_convertible<ArgT, T>::value, int>::type = 0>
    InParam(ArgT&& x)
        : case_(NEW), rv_(new T(std::forward<ArgT>(x))) {}
    ~InParam() noexcept { if (NEW == case_) delete rv_; }

    InParam(T const& l): case_(LVALUE), lv_(&l) {}
    InParam(T&& r): case_(XVALUE), rv_(&r) {}

    InParam(InParam&& a): case_(a.case_), rv_(a.rv_)
        { a.case_ = XVALUE; a.rv_ = nullptr; }

    private:
    InParam(InParam const& a) = delete;

    enum Case{LVALUE, XVALUE, NEW};
    Case case_;
    union
    {
        T const* lv_;   // should not delete
        T* rv_;         // unique; if NEW: should delete
    };
};


template <typename... ArgTs> struct are_convertible;
template <typename A>
struct are_convertible<A>
{
    //static_assert(false, "len(arguments) should be even");
};

template <>
struct are_convertible<>
{ static bool const value = true; };
template <typename I, typename O, typename... ArgTs>
struct are_convertible<I, O, ArgTs...>
{
    static bool const value = std::is_convertible<I, O>::value
                            && are_convertible<ArgTs...>::value;
};


#include <string>
using std::string;
class S3_1{
    string _a, _b, _c;
    public:
    // 1. perfect forwarding
    template<typename A, typename B, typename C
        , typename std::enable_if<
                are_convertible<A,string, B,string, C,string>::value
                //std::is_convertible<A, string>::value
                //&& std::is_convertible<B, string>::value
                //&& std::is_convertible<C, string>::value
                , int>::type = 0
        >
    S3_1(A&& a, B&& b, C&& c)
    : _a(std::forward<A>(a))
    , _b(std::forward<B>(b))
    , _c(std::forward<C>(c))
    {}
};
class S3_2{
    string _a, _b, _c;
    public:
    // 2. copy+move
    S3_2(string a, string b, string c)
    : _a(std::move(a))
    , _b(std::move(b))
    , _c(std::move(c))
    {}
};
class S3_3{
    string _a, _b, _c;
    public:
    S3_3(InParam<string> a, InParam<string> b, InParam<string> c)
        : _a(std::move(a).move_as_xvalue())
        , _b(std::move(b).move_as_xvalue())
        , _c(std::move(c).move_as_xvalue())
        {}
};

void f()
{
    string a = "";
    string const b = "";
    S3_1(a, b, "");
    S3_2(a, b, "");
    S3_3(a, b, "");
}

