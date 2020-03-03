from sources.graph_generation import*
import line_profiler

f = generate_random_graph
g = generate_random_graph_2


class GraphGeneration:
    def __init__(self, n, percent):
        self.n = n
        self.percent = percent

    def gen(self):
        n = self.n
        percent = self.percent
        f1 = f(n, percent * n * (n - 1) / 2, directed=False)
        g1 = g(n, percent * n * (n - 1) / 2, directed=False)


def main(params, n_runs=3):
    n1, n2, n3 = params['n_nodes']
    p1, p2, p3 = params['edges_percent']
    for i in range(n_runs):
        print('Run', i)
        n = np.random.choice([n1, n2, n3])
        p = np.random.choice([p1, p2, p3])
        m = GraphGeneration(n, p)
        m.gen()


if __name__ == '__main__':
    my_params = {
        'n_nodes': (300, 1000, 2000), 'edges_percent': (0.1, 0.2, 0.3)
    }
    lp = line_profiler.LineProfiler()
    lp.add_function(f)
    lp.add_function(g)
    lp_wrapper = lp(main)
    lp_wrapper(my_params)

    lp.print_stats(output_unit=1e-3)

    stats_file = 'profile_generation.lprof'
    lp.dump_stats(stats_file)
    print('Run the following command to display the results:')
    print('$ python -m line_profiler {}'.format(stats_file))
