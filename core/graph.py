from collections import defaultdict, deque


class ProjectGraph:
    """
    Merepresentasikan graph proyek menggunakan
    adjacency list.
    """

    def __init__(self):

        # Menyimpan object Activity
        self.activities = {}

        # Adjacency list
        self.graph = defaultdict(list)

        # In-degree untuk topological sort
        self.in_degree = defaultdict(int)

    # ==================================================
    # TAMBAH AKTIVITAS
    # ==================================================

    def add_activity(self, activity):
        """
        Menambahkan aktivitas ke dalam graph.
        """

        if activity.id in self.activities:

            raise ValueError(
                f"Aktivitas dengan ID '{activity.id}' sudah ada."
            )

        self.activities[activity.id] = activity

        # Pastikan key tersedia
        self.graph[activity.id]

        self.in_degree[activity.id]

    # ==================================================
    # TAMBAH DEPENDENCY
    # ==================================================

    def add_dependency(self, predecessor, successor):
        """
        predecessor -> successor
        """

        if predecessor not in self.activities:

            raise ValueError(
                f"Aktivitas '{predecessor}' tidak ditemukan."
            )

        if successor not in self.activities:

            raise ValueError(
                f"Aktivitas '{successor}' tidak ditemukan."
            )

        self.graph[predecessor].append(successor)
        self.in_degree[successor] += 1
        self.activities[successor].dependencies.append(
            predecessor
        )

    # ==================================================
    # TOPOLOGICAL SORT
    # ==================================================

    def topological_sort(self):
        """
        Menghasilkan urutan topologi menggunakan
        algoritma Kahn.
        """
        in_degree = self.in_degree.copy()
        queue = deque()
        for node in self.activities:
            if in_degree[node] == 0:
                queue.append(node)

        topo_order = []

        while queue:
            current = queue.popleft()
            topo_order.append(current)
            for neighbor in self.graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return topo_order

    # ==================================================
    # DETEKSI CYCLE
    # ==================================================

    def has_cycle(self):
        """
        Mengembalikan True apabila graph
        mengandung cycle.
        """
        topo_order = self.topological_sort()
        return len(topo_order) != len(self.activities)