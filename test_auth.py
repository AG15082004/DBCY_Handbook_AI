from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

print("Connected")
print(w.current_user.me().user_name)