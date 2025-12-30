file_name = "report.md" # Using .md extension is a good practice

content = """
#  Monthly Report

Here are the key takeaways:

* **Sales are Up:** We saw a **20% increase** this month.
* *New Clients:* We acquired 5 new clients.
* ~~Old Goal:~~ The original target has been surpassed.

---

This is a draft.
"""

with open(file_name, 'w') as f:
    f.write(content)

print(f"Content written to {file_name}")
# When you view report.md in a Markdown editor, 'Sales are Up' will be bold.