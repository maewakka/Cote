def solution(sequence):
    p = [(-1)**i for i in range(len(sequence))]
    psum = [0] * (len(sequence)+1)
    
    for i in range(len(sequence)):
        p[i] *= sequence[i]
        psum[i+1] = p[i]
        
    for i in range(1, len(psum)):
        psum[i] += psum[i-1]

    return max(psum) - min(psum)