class CPMCalculator:
    """
    Bertanggung jawab melakukan perhitungan Critical Path Method (CPM) pada ProjectGraph
    """
    def __init__(self, project_graph):
        self.project_graph = project_graph

    def calculate(self):
        """
        Menjalankan seluruh proses CPM dan
        mengembalikan hasil analisis proyek.
        """

        topo_order = self.project_graph.topological_sort()
        self.forward_pass(topo_order)
        self.backward_pass(topo_order)
        self.calculate_slack()
        critical_path = self.get_critical_path(topo_order)
        project_duration = max(
            activity.ef
            for activity in self.project_graph.activities.values()
        )

        return {
            "project_duration": project_duration,
            "critical_path": critical_path,
            "activities": self.project_graph.activities,
            "total_activities": len(self.project_graph.activities),
            "critical_count": len(critical_path)
        }
    
    def forward_pass(self, topo_order: list[str]) -> None:
        for activity_id in topo_order:
            activity = self.project_graph.activities[activity_id]
            if not activity.dependencies:
                activity.es = 0
                activity.ef = activity.duration

            else:
                max_ef = max(
                    self.project_graph.activities[dep].ef
                    for dep in activity.dependencies
                )
                activity.es = max_ef
                activity.ef = activity.es + activity.duration
    
    def backward_pass(self, topo_order):
        """
        Menghitung Latest Start (LS) dan
        Latest Finish (LF).
        """
        # Total durasi proyek
        project_duration = max(
            activity.ef
            for activity in self.project_graph.activities.values()
        )

        # Proses dari belakang
        for activity_id in reversed(topo_order):
            activity = self.project_graph.activities[activity_id]
            # Jika tidak memiliki successor
            if not (self.project_graph.graph[activity_id]):

                activity.lf = project_duration
                activity.ls = activity.lf - activity.duration

            else:
                min_ls = min(
                    self.project_graph.activities[successor].ls
                    for successor in self.project_graph.graph[activity_id]
                )
                activity.lf = min_ls
                activity.ls = activity.lf - activity.duration

    def calculate_slack(self):
        """
        Menghitung slack setiap aktivitas dan
        menentukan apakah aktivitas tersebut
        termasuk jalur kritis.
        """

        for activity in self.project_graph.activities.values():

            activity.slack = activity.ls - activity.es

            activity.is_critical = activity.slack == 0

    def get_critical_path(self, topo_order):
        """
        Mengembalikan daftar aktivitas
        yang berada pada jalur kritis.
        """

        critical_path = []
        for activity_id in topo_order:
            activity = self.project_graph.activities[activity_id]
            if activity.is_critical:
                critical_path.append(activity_id)
        return critical_path