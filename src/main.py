file = open("main.cpp", "w+")

# tab = ["#include <iostream>", "int", "main() {", "std", "cout <<", "endl;", "return", "}"]
# program = "{0}\n\n{1} {2} \n {3}::{4} \"Hello World!\" << {3}::{5} \n {6} 0; \n {7}".format(*tab)
# file.writelines(program)

libraries = ["#include", "<iostream>"]
namespaces = ["using namespace std;"]
keyWords = ["#define", "typedef", "return", "__global__", "void", "sizeof"]
functions = ["MyKernel", "main", "cudaMalloc", "cudaMemcpy", "cudaMemcpyHostToDevice", "cudaMemcpyDeviceToHost"]
typesVariables = ["int", "int*", "int**", ]
variables = ["N", "arrtype", "row", "col", "h", "w", "j", "d_A", "blockIdx", "blockDim", "threadIdx", "rows", "cols", "dA", "A"]
values = ["100", "8", "0"]

definitionLib = "\n{0} {1}\n".format(libraries[0], libraries[1])
file.writelines(definitionLib)

definitionConst = "\n{0} {1} {2} \n\n".format(keyWords[0], variables[0], values[0])
file.writelines(definitionConst)

file.writelines(namespaces)

definitionVariable1 = "\n{0} {1} {2}[{3}]; \n\n".format(keyWords[1], typesVariables[0], variables[1], variables[0])
file.writelines(definitionVariable1)

myKernelFunc = "\n{0} {1} {2}({3} {4}[{5}][{6}]){{\n\n".format(keyWords[3], keyWords[4], functions[0], typesVariables[0], variables[7], variables[0], variables[0])
file.writelines(myKernelFunc)
myKernelBody1 = "\t{0} {1} = {2}.y * {3}.y + {4}.y; \n\t{5} {6} = {7}.x * {8}.x + {9}.x; \n\n".format(typesVariables[0], variables[2], variables[8], variables[9],variables[10], typesVariables[0], variables[3], variables[8], variables[9], variables[10])
file.writelines(myKernelBody1)

definitionVariable2 = "\t{0} {1} = {2};\n\t{3} {4} = {5};\n\t{6} {7};\n\t".format(typesVariables[0], variables[4], variables[0], typesVariables[0], variables[5], variables[0], typesVariables[0], variables[6])
file.writelines(definitionVariable2)

myKernelIf = "if({0} >= {1} || {2} >= {3})\n\t\t{4};\n\n\t".format(variables[4], variables[6], variables[5], variables[7], keyWords[2])
file.writelines(myKernelIf)

myKernelFor = "for({0}={1};{0}<{2};{0}++)\n\t\t{3}[{4}][{0}] = {5}\n\n}}".format(variables[6], values[2], variables[0], variables[0], variables[10], values[1])
file.writelines(myKernelFor)

mainFunc = "\n\n{0} {1}(){{\n\n".format(typesVariables[0], functions[1])
file.writelines(mainFunc)

mainBody1 = "\t{0} {1} = {2}.y * {3}.y + {4}.y; \n\t{5} {6} = {7}.x * {8}.x + {9}.x; \n\n".format(typesVariables[0], variables[2], variables[8], variables[9],variables[10], typesVariables[0], variables[3], variables[8], variables[9], variables[10])
file.writelines(myKernelBody1)

mainBody2 = "\t{0} {1} = {2};\n\t{0} {3} = {2};\n\t{4} *{5};\n\n\t".format(typesVariables[0], variables[11], variables[0], variables[12], variables[1], variables[13])
file.writelines(mainBody2)

mainBody3 = "{0}** {1} = new {0}*[{2}];\n\t{1}[0] = new {0}[{2}*{3}];\n\n\t".format(typesVariables[0], variables[14], variables[11], variables[12])
file.writelines(mainBody3)

mainFor1 = "for({0} i = 1; i < {1}; ++i){{\n\t\t{2}[i] = {2}[i-1] + {3};\n\n\t".format(typesVariables[0], variables[11], variables[14], variables[12])
file.writelines(mainFor1)

mainFor2 = "for({0} i = 0; i < {1}; ++i){{\n\t\tfor({0} j = 0; j < {3}; ++j){{\n\t\t{2}[i][j] = i*{3}+j;\n\t\t}}\n\t}}\n\n".format(typesVariables[0], variables[11], variables[14], variables[12])
file.writelines(mainFor2)

mainCudaFunc1 = "\t{0}(({1}**)&{2}, sizint) * {3}* {4});\n".format(functions[2], keyWords[4], variables[13], variables[11], variables[12])
file.writelines(mainCudaFunc1)

mainCudaFunc2 = "\t{0}({1}, {2}[0], {3}({4}) * {5}* {6}, {7});\n\n".format(functions[3], variables[13], variables[14], keyWords[5], typesVariables[0], variables[11], variables[12], functions[4])
file.writelines(mainCudaFunc2)

mainCudaFunc3 = "\t{0} <<{1},{1}>>({2});\n\n".format(functions[0], variables[0], variables[13])
file.writelines(mainCudaFunc3)

mainCudaFunc4 = "\t{0}({2}[0], {1}, {3}({4}) * {5}* {6}, {7});\n\n}}".format(functions[4], variables[13], variables[14], keyWords[5], typesVariables[0], variables[11], variables[12], functions[5])
file.writelines(mainCudaFunc4)

file.close()
