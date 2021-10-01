import importlib
from datetime import datetime

module_name = "project_10"


module_full_name = "projects." + module_name


my_module = importlib.import_module(module_full_name)

get_statement = True
get_answer = True

if get_statement:
    my_module.problem_statement()

if get_answer:
    start_time = datetime.now()
    my_module.run()
    time_taken = (datetime.now() - start_time).total_seconds()
    print("Total time taken is", time_taken, "seconds")
    # my_module.run_brute_force_np()
