package pkgMakeJarShouldContains;

class UnexportedClass{} // non-public top-level class
class MyClass{
    class Inner{}
    MyClass(){
        new Object(){}; // anonymous
    }
}

