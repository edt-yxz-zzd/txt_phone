javac -cp . pkgResourceAccessor/ResourceAccessor.java
java -cp . pkgResourceAccessor.ResourceAccessor
jar -cfe ResourceAccessor.jar  pkgResourceAccessor.ResourceAccessor pkgResourceAccessor global_resources
java -jar ResourceAccessor.jar
