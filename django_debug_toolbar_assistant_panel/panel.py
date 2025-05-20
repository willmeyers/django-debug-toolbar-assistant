from debug_toolbar.panels import Panel
from django.db import connection
from django.templatetags.static import static
from .gemini import query_gemini

class AssistantPanel(Panel):
    title = "Assistant"
    has_content = True
    template = "panels/djdt_assistant.html"
    
    @property
    def scripts(self):
        return [
            static("__debug__/djdt_assistant_panel/js/panel.js")
        ]

    def generate_stats(self, request, response):
        queries = connection.queries
        self.record_stats({
            "queries": [
                {"sql": q["sql"], "time": q.get("time", "?")}
                for q in queries
            ]
        })
