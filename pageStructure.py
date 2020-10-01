from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
import reportlab.platypus as platypus
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, PageBreak, Frame, FrameBreak, Spacer, Paragraph,
)


def create_doc(frame_num):
    doc = BaseDocTemplate(
        'medium_highlights.pdf',
        pagesize=A4,
        topMargin=1*inch,
        bottomMargin=1*inch,
        leftMargin=0.5*inch,
        rightMargin=0.5*inch)

    frameCount = frame_num
    frameWidth = (doc.width- 0.1*inch) / frameCount
    frameHeight = doc.height - 0.05*inch

    frame_list = [
        Frame(
            x1=doc.leftMargin,
            y1=doc.bottomMargin,
            width=frameWidth,
            height=frameHeight),
        Frame(
            x1=doc.leftMargin + frameWidth + 0.1*inch,
            y1=doc.bottomMargin,
            width=frameWidth,
            height=frameHeight),
    ]
    template = platypus.PageTemplate(frames=frame_list)
    doc.addPageTemplates(template)

    return doc