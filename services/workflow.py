from graph.graph import graph


class Workflow:

    def run(self, url):

        result = graph.invoke({
            "url": url
        })

        return result["analysis"]