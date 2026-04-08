# یک فایل HTML ساده می‌سازیم
html_content = """
<html>
<head><title>Emad's CD Project</title></head>
<body>
    <h1>Salam! In safe tavasote CD sakhte shode.</h1>
    <p>Akharin update: 2026-04-07</p>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("Website created successfully!")

