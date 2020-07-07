
// see: "access resources.txt"

/*
command:
    example>javac -cp . pkgResourceAccessor/ResourceAccessor.java
    example>java -cp . pkgResourceAccessor.ResourceAccessor
    example>jar -cfe ResourceAccessor.jar  pkgResourceAccessor.ResourceAccessor pkgResourceAccessor global_resources
    example>java -jar ResourceAccessor.jar
*/
package pkgResourceAccessor;
import java.util.ArrayList;
import java.io.IOException;
import java.lang.invoke.MethodHandles;

class ResourceAccessor{

public static void f(){
    ArrayList<Object> ls = new ArrayList<>();
}

public static void main(String[] argv)
throws IOException
{
    final String local = "local_resources/test.txt"; // relative
    final String global = "/global_resources/test.txt"; // absolute
    final String global_as_local = "global_resources/test.txt";

System.out.println("Thread.currentThread().getContextClassLoader().getResourceAsStream");

    ClassLoader loader = Thread.currentThread().getContextClassLoader();
    System.out.println(local);
    fail_if_null(loader.getResourceAsStream(local));
        // in filesystem: fail
        // in jar       : fail

    System.out.println(global);
    fail_if_null(loader.getResourceAsStream(global));
        // in filesystem: fail
        // in jar       : fail
    System.out.println(global_as_local);
    fail_if_null(loader.getResourceAsStream(global_as_local));
        // in filesystem: work
        // in jar       : work


System.out.println("\n");
System.out.println("getClass().getResourceAsStream");
    Class thisClass = MethodHandles.lookup().lookupClass();
    Class thisClass2 = ResourceAccessor.class;
    assert thisClass2 == thisClass;
    assert null != thisClass;
    System.out.println(thisClass.toString());

    System.out.println(local);
    fail_if_null(thisClass.getResourceAsStream(local));
        // in filesystem: work
        // in jar       : work
    System.out.println(global);
    fail_if_null(thisClass.getResourceAsStream(global));
        // in filesystem: work
        // in jar       : work
}

static void fail_if_null(Object obj){
    if (null == obj)
        System.out.println("fail");
    else
        System.out.println("work!");
}


}
