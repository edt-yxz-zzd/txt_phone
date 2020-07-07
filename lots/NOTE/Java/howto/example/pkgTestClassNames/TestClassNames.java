// see: "class info.txt"

/*
command:
    example>javac -cp . pkgTestClassNames/TestClassNames.java
    example>java -cp . pkgTestClassNames.TestClassNames
    example>java -cp . pkgTestClassNames.TestClassNames > pkgTestClassNames/output.txt
*/


//https://stackoverflow.com/questions/15202997/what-is-the-difference-between-canonical-name-simple-name-and-class-name-in-jav

package pkgTestClassNames;
import java.util.HashMap;

public final class TestClassNames {
    private static void showClass(Class<?> c) {
        System.out.println("getName():          " + c.getName());
        System.out.println("getCanonicalName(): " + c.getCanonicalName());
        System.out.println("getSimpleName():    " + c.getSimpleName());
        System.out.println("toString():         " + c.toString());
        System.out.println();
    }

    private static void x(Runnable r) {
        showClass(r.getClass());
        showClass(java.lang.reflect.Array.newInstance(r.getClass(), 1).getClass()); // Obtains an array class of a lambda base type.
    }

    public static class NestedClass {}

    public class InnerClass {}

    public static void main(String[] args) {
        class LocalClass {}
        showClass(void.class);
        showClass(int.class);
        showClass(String.class);
        showClass(Runnable.class);
        showClass(SomeEnum.class);
        showClass(SomeAnnotation.class);
        showClass(UnexportedClass.class);
        //showClass(HashMap<String, String>.class);
        showClass(HashMap.class);
        showClass(new HashMap<String, String>().getClass());
        assert HashMap.class == new HashMap<String, String>().getClass();

        showClass(int[].class);
        showClass(String[].class);
        showClass(NestedClass.class);
        showClass(InnerClass.class);
        showClass(LocalClass.class);
        showClass(LocalClass[].class);
        Object anonymous = new java.io.Serializable() {};
        showClass(anonymous.getClass());
        showClass(java.lang.reflect.Array.newInstance(anonymous.getClass(), 1).getClass()); // Obtains an array class of an anonymous base type.
        x(() -> {});
    }
}

enum SomeEnum {
   BLUE, YELLOW, RED;
}

@interface SomeAnnotation {}
//private
class UnexportedClass{}

