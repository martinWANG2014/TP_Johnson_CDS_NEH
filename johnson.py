import commonFunction
import interface


def johnson(data, nb_machines, nb_jobs):
    seq_current = commonFunction.u(data, nb_jobs) + commonFunction.v(data, nb_jobs)
    return seq_current, commonFunction.makespan(seq_current, p_ij, nb_machines)[nb_machines - 1][nb_jobs]


# run Johnson
nbm, nbj, p_ij = commonFunction.read_from_file("example.txt")
seq, cmax = johnson(p_ij, nbm, nbj)
print("nbMachines:", nbm)
print("nbJobs:", nbj)
print("data: p_ij, the processing time of jth job on ith machine\n", p_ij)
print("johnson:", seq, cmax)
interface.graphic("Johnson", seq, nbj, nbm, commonFunction.makespan(seq, p_ij, nbm), p_ij)
