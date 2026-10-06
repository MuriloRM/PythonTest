import roberty_code as roberty

error = roberty.exception()
if error:
    print(f"Robot failed (exit code {error['exitCode']}): {error['message']}")
    roberty.output({"status": "error", "message": error["message"]})
