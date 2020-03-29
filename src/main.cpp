#include <iostream>
#define N 100 

using namespace std;
typedef int arrtype[N]; 


__global__ void MyKernel(int d_A[N][N]){

	int row = blockIdx.y * blockDim.y + threadIdx.y; 
	int col = blockIdx.x * blockDim.x + threadIdx.x; 

	int h = N;
	int w = N;
	int j;
	if(h >= j || w >= d_A)
		return;

	for(j=0;j<N;j++)
		N[threadIdx][j] = 8

}

int main(){

	int row = blockIdx.y * blockDim.y + threadIdx.y; 
	int col = blockIdx.x * blockDim.x + threadIdx.x; 

	int rows = N;
	int cols = N;
	arrtype *dA;

	int** A = new int*[rows];
	A[0] = new int[rows*cols];

	for(int i = 1; i < rows; ++i){
		A[i] = A[i-1] + cols;

	for(int i = 0; i < rows; ++i){
		for(int j = 0; j < cols; ++j){
		A[i][j] = i*cols+j;
		}
	}

	cudaMalloc((void**)&dA, sizint) * rows* cols);
	cudaMemcpy(dA, A[0], sizeof(int) * rows* cols, cudaMemcpyHostToDevice);

	MyKernel <<N,N>>(dA);

	cudaMemcpyHostToDevice(A[0], dA, sizeof(int) * rows* cols, cudaMemcpyDeviceToHost);

}