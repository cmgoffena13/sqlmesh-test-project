from sqlmesh.core.context import Context

from config import config

if __name__ == "__main__":
    try:
        context = Context(config=config)
        print("Context initialized. Attempting migrate...")
        context.migrate()
        print("Migration successful.")
    except Exception as e:
        print("\n--- ROOT CAUSE ERROR ---")
        print(f"Type: {type(e).__name__}")
        print(f"Message: {e!s}")
        print("\n--- FULL TRACEBACK ---")

        import traceback

        traceback.print_exc()
        print("\n--- CAUSE CHAIN ---")
        cause = e.__cause__
        while cause:
            print(f"Caused by: {type(cause).__name__}: {cause}")
            cause = cause.__cause__
