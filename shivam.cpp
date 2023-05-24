#include <stdio.h>

// CUDA kernel to perform vector addition
__global__ void vectorAddition(float* a, float* b, float* c, int size) {
    int tid = blockIdx.x * blockDim.x + threadIdx.x;
    
    if (tid < size) {
        c[tid] = a[tid] + b[tid];
    }
}

int main() {
    int size = 1000000;  // Size of the vectors
    int numBytes = size * sizeof(float);
    
    // Allocate memory for the host vectors
    float *h_a = (float*)malloc(numBytes);
    float *h_b = (float*)malloc(numBytes);
    float *h_c = (float*)malloc(numBytes);
    
    // Initialize the host vectors
    for (int i = 0; i < size; i++) {
        h_a[i] = i;
        h_b[i] = i * 2;
    }
    
    // Allocate memory for the device vectors
    float *d_a, *d_b, *d_c;
    cudaMalloc((void**)&d_a, numBytes);
    cudaMalloc((void**)&d_b, numBytes);
    cudaMalloc((void**)&d_c, numBytes);
    
    // Copy the host vectors to device memory
    cudaMemcpy(d_a, h_a, numBytes, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, numBytes, cudaMemcpyHostToDevice);
    
    // Define the block and grid dimensions
    int threadsPerBlock = 256;
    int blocksPerGrid = (size + threadsPerBlock - 1) / threadsPerBlock;
    
    // Launch the vector addition kernel
    vectorAddition<<<blocksPerGrid, threadsPerBlock>>>(d_a, d_b, d_c, size);
    
    // Copy the result vector from device to host
    cudaMemcpy(h_c, d_c, numBytes, cudaMemcpyDeviceToHost);
    
    // Print the result
    for (int i = 0; i < size; i++) {
        printf("%.2f ", h_c[i]);
    }
    
    // Free device memory
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
    
    // Free host memory
    free(h_a);
    free(h_b);
    free(h_c);
    
    return 0;
}
