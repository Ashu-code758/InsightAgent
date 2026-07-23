import os

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class PDFTool:

    def create_report(self, text):

        # reports folder automatically create hoga
        os.makedirs("reports", exist_ok=True)

        doc = SimpleDocTemplate("reports/report.pdf")

        styles = getSampleStyleSheet()

        story = []

        story.append(Paragraph("<b>InsightAgent Report</b>", styles["Title"]))
        story.append(Paragraph(text.replace("\n", "<br/>"), styles["BodyText"]))

        doc.build(story)

        return "reports/report.pdf"