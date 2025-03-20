import os
import merged_bot  # Make sure this matches your main Python file/module

port = int(os.environ.get("PORT", 8080))
merged_bot.app.run(host="0.0.0.0", port=port)
