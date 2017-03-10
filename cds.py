import numpy
import commonFunction
import interface
#####################################################
# algorithm for cds
#####################################################


def get_merge(start_index, end_index, data, nb_jobs):
    data_prime = numpy.zeros(nb_jobs)
    for j in range(nb_jobs):
        data_prime[j] = data[start_index][j]
    if start_index + 1 < end_index:
        for k in range(start_index + 1, end_index):
            for j in range(nb_jobs):
                data_prime[j] += data[k][j]
    return data_prime


def cds(data, nb_machines, nb_jobs):
    c_max_best = float("inf")
    for k in range(1, nb_machines):
        p1_prime = get_merge(0, k, data, nb_jobs)
        p2_prime = get_merge(nb_machines - k, nb_machines, data, nb_jobs)
        ss_pb = [p1_prime, p2_prime]
        print(ss_pb)
        current_seq = commonFunction.u(ss_pb, nb_jobs) + commonFunction.v(ss_pb, nb_jobs)
        c_max = commonFunction.makespan(current_seq, data, nb_machines)[nb_machines - 1][nb_jobs]
        print(current_seq, c_max)
        if c_max < c_max_best:
            c_max_best = c_max
            best_seq = current_seq

    return best_seq, c_max_best

# run CDS
nbm, nbj, p_ij = commonFunction.read_from_file("example2.txt")
seq, cmax = cds(p_ij, nbm, nbj)
print("nbMachines:", nbm)
print("nbJobs:", nbj)
print("data: p_ij, the processing time of jth job on ith machine\n", p_ij)
print("cds:", seq, cmax)
interface.graphic("CDS", seq, nbj, nbm, commonFunction.makespan(seq, p_ij, nbm), p_ij)
