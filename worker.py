while True:
    raw_task = r.brpop(queue_name, timeout=5)  # waits max 5 seconds
    if raw_task:
        _, task_json = raw_task
        task = json.loads(task_json)
        pprint.pprint(task)
    else:
        # this is no task
        print("No task arrived, waiting again...")das
