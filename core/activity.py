class Activity:
    """Representasi satu aktivitas proyek."""

    def __init__(self, activity_id: str, name: str, duration: int):
        self.id = activity_id
        self.name = name
        self.duration = duration

        self.dependencies = []

        self.es = 0
        self.ef = 0 

        self.ls = 0
        self.lf = 0

        self.slack = 0

        self.is_critical = False

    def __repr__(self):
        return f"{self.id} - {self.name}"