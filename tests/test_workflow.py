from services.workflow import Workflow

workflow = Workflow()

result = workflow.run("https://books.toscrape.com/")

print(result)