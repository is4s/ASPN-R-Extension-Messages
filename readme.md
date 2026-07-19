# Readme
This is a quick readme on how the headers were generated.  Included here is one quick example program to run as well for testing.  
Note the program was done in python, and the jar file was used with LCM spy to validate.  

DDS is still in IDL format as no particular version of DDS is specified to run through their generation software.  

## Python
```
lcm-gen -p lcm/* --ppath generated/python
```

## Java and Jar File
```
lcm-gen -j lcm/ --jpath generated/java/
lcm-gen -j lcm/* --jpath generated/java/
cd generated/java/
javac aspn_r/*.java
jar cf aspn_r.jar aspn_r/*.class
```

## C 
```
lcm-gen -c lcm/* --c-cpath generated/c/src --c-hpath generated/c/include
```

## C++
```
lcm-gen -x lcm/* --cpp-hpath generated/cpp/
```