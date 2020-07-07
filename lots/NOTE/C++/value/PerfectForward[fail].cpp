
//////////////////// fail /////////////////////
#include <utility> // forward, move
#include <type_traits> // enable_if and others

template<typename T>
class _PerfectForward
{
    // T is (X) or (X&)
    // X is (Y) or (Y const)
    private:
    T&& ref;
    _PerfectForward(_PerfectForward const&)=delete;
    _PerfectForward(_PerfectForward&&)=delete;

    public:
    // implicit convert
    _PerfectForward(T&& t): ref(std::forward<T>(t)){}
    //template <typename Arg>
    //_PerfectForward(Arg&& a): _PerfectForward(T(std::forward<Arg>(a))){}

    public:
    T&& get_ref()&&
    { return std::forward<T>(this->ref); }
};

template<typename T>
using PerfectForward = _PerfectForward<T>; // _PerfectForward<T>&&;
// using PerfectForward in input parameters only




#include <string>
using std::string;

// how?
//S3(string const& a, string const& b, string const& c);
//S3(string&& a, string&& b, string&& c);

class S3_1{
    string _a, _b, _c;
    public:
    // 1. perfect forwarding
    template<typename A, typename B, typename C
        , typename std::enable_if<
              std::is_convertible<A, string>::value
              && std::is_convertible<B, string>::value
              && std::is_convertible<C, string>::value
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
    // fail!!!!!!!
    string _a, _b, _c;
    public:
    // 3. PerfectForward
    template<typename A, typename B, typename C>
    S3_3(PerfectForward<A> a, PerfectForward<B> b, PerfectForward<C> c)
    : _a(a.get_ref())
    , _b(b.get_ref())
    , _c(c.get_ref())
    {}
};

void f()
{
    string a = "";
    string const b = "";
    S3_1(a, b, "");
    S3_2(a, b, "");
    S3_3(a, b, "");
    //S3_3(a, a, a);
    //S3_3(b, b, b);
    //S3_3("", "", "");
}
