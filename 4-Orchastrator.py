
def orchestrator(task):
    task = task.lower()
    workers = []

    if "api" in task or "backend" in task:
        workers.append("backend")

    if "database" in task:
        workers.append("database")

    if "test" in task:
        workers.append("testing")
    if "documentation" in task:
        workers.append("documentation")

    return workers


def backend_worker(task):
    return "Backend API implementation plan"


def database_worker(task):
    return "Database schema implementation plan"


def testing_worker(task):
    return "Automated testing plan"

def documentation_worker(task):
    return "Documentation plan"
WORKERS = {
    "backend": backend_worker,
    "database": database_worker,
    "testing": testing_worker,
    "documentation": documentation_worker
}


def run_workflow(task):
    selected_workers = orchestrator(task)
    results = {}

    for worker_name in selected_workers:
        worker = WORKERS[worker_name]
        results[worker_name] = worker(task)

    return results


task = "Build a backend API with a database and tests and documentation"

print(run_workflow(task))
