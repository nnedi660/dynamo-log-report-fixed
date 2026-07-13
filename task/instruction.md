An Apache-style access log is available at the absolute path /app/data/access.log. Parse this log file and write your JSON summary report to the exact path /app/report.json.

Required Output Format:
Your report must be a single valid JSON object containing exactly these three keys:
1. "total_requests": Integer count of all non-empty log lines in the file.
2. "unique_ips": Integer count of distinct client IP addresses (the first whitespace-separated value on each log line).
3. "top_path": String of the most frequently requested URL path (extracted from the quoted HTTP request line, e.g. "/index.html").

Rules:
• Do not modify or delete the input file /app/data/access.log.
• Use only the provided log file to compute your results.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
