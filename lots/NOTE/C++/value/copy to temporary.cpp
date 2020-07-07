
#include <utility>
#include <string>

void f(int&& i){}
void g()
{
    int j = 0;
    //f(j); // compile ERROR!
}



using std::string;

class S3{
    string _a, _b, _c;

    // how?
    //S3(string const& a, string const& b, string const& c);
    //S3(string&& a, string&& b, string&& c);

    // 1. perfect forwarding
    template<typename A, typename B, typename C>
    S3(A&& a, B&& b, C&& c)
    : _a(std::forward<A>(a))
    , _b(std::forward<B>(b))
    , _c(std::forward<C>(c))
    {}

    // 2. copy+move
    S3(string a, string b, string c)
    : _a(std::move(a))
    , _b(std::move(b))
    , _c(std::move(c))
    {}
    //https://www.codesynthesis.com/~boris/blog/2012/06/19/efficient-argument-passing-cxx11-part1/
    //the overhead of pass-by-value is one extra move in each case.
    //pass-by-value only works if you are definitely making a copy of the argument.
    //  otherwise be a whole extra copy.

};


/*
*/


