
// g++11
void f()
{
    int&& i{0};
    int const& k{0};
    int&& i2 = 0;
    int const& k2 = 0;
    &i;
    &k;
    &i2;
    &k2;
}

/*
https://stackoverflow.com/questions/17980570/pass-by-reference-constant-reference-rvalue-reference-or-constant-rvalue-refe
This is because the notion of an rvalue is that you can recycle its contents, e.g. claim ownership of the memory it has dynamically allocated. This can be dangerous if you still have access to the object after the operation, therefore the explicit std::move is required for lvalues.


*/
