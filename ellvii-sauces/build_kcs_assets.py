from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, ListFlowable, ListItem
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER

pdf_path = "KCS_Coaching_and_BSIT_KB.pdf"
title = "KCS Coaching & Process Documentation Framework"
subtitle = "KB Article | Article ID: KCS-0049 | Version 1.2 | Last Updated: Oct 2025 | Author: Lawrence Bloodsaw-Velasquez"
gold_hex = "#DAA520"  # change to your Ell Vii gold if you like

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='KBTitle', fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=colors.black, spaceAfter=10))
styles.add(ParagraphStyle(name='KBMeta', fontName='Helvetica', fontSize=9, leading=12, textColor=colors.grey, spaceAfter=12))
styles.add(ParagraphStyle(name='KBH2', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceBefore=8, spaceAfter=6))
styles.add(ParagraphStyle(name='KBBody', fontName='Helvetica', fontSize=10.5, leading=14, spaceAfter=6))
styles.add(ParagraphStyle(name='KBBold', fontName='Helvetica-Bold', fontSize=10.5, leading=14, spaceAfter=6))
styles.add(ParagraphStyle(name='KBFine', fontName='Helvetica', fontSize=9, leading=12, textColor=colors.HexColor("#444444"), spaceAfter=8))

doc = SimpleDocTemplate(pdf_path, pagesize=LETTER, topMargin=0.75*inch, bottomMargin=0.75*inch, leftMargin=0.75*inch, rightMargin=0.75*inch)

flow = []

from reportlab.platypus import Flowable
class GoldRule(Flowable):
    def __init__(self, height=8, color=colors.HexColor(gold_hex)):
        Flowable.__init__(self); self.height = height; self.color = color; self.width = 0
    def draw(self):
        self.canv.saveState()
        self.canv.setFillColor(self.color)
        self.canv.rect(-doc.leftMargin, 0, doc.width + doc.leftMargin + doc.rightMargin, self.height, stroke=0, fill=1)
        self.canv.restoreState()
    def wrap(self, availWidth, availHeight):
        self.width = availWidth; return availWidth, self.height

flow.append(GoldRule())
flow.append(Spacer(1, 12))
flow.append(Paragraph(title, styles['KBTitle']))
flow.append(Paragraph(subtitle, styles['KBMeta']))

flow.append(Paragraph("Summary", styles['KBH2']))
flow.append(Paragraph(
    "This article outlines how the <b>KCS (Coaching) Framework</b> was designed and implemented to transform fragmented support documentation into a unified knowledge ecosystem. It also showcases a key deliverable — the <b>BSIT Escalation Process SOP</b> — as a case study proving measurable operational impact.",
    styles['KBBody']
))

flow.append(Paragraph("Background / The Challenge", styles['KBH2']))
bg_points = [
    "Inconsistent knowledge article quality across business units",
    "Limited agent confidence in search results and KB reliability",
    "High onboarding friction for new agents",
    "Undefined escalation pathways for complex system issues",
]
flow.append(ListFlowable([ListItem(Paragraph(p, styles['KBBody'])) for p in bg_points], bulletType='bullet', leftIndent=14))
flow.append(Paragraph("<b>Business Impact:</b> Slow resolution times, duplicated tickets, and incomplete engineering handoffs.", styles['KBBody']))

flow.append(Paragraph("Solution Overview — The KCS Coaching Framework", styles['KBH2']))
flow.append(Paragraph("<b>Goal:</b> Establish a culture of continuous knowledge improvement supported by metrics and peer accountability.", styles['KBBody']))

components_data = [
    ["Component", "Description"],
    ["Article Quality Checklist (AQC)", "Objective rubric evaluating accuracy, structure, and findability."],
    ["Peer Coaching Program", "Senior agents mentor junior staff on style and taxonomy consistency."],
    ["Performance & Adoption Dashboard", "Tracks reuse rate, AQC scores, and KCS participation per team."],
    ["Standardized SOP Templates", "Pre-approved formats for procedures, job aids, and escalations."],
]
tbl = Table(components_data, hAlign='LEFT', colWidths=[2.4*inch, 3.9*inch])
tbl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor(gold_hex)),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 10),
    ('LINEABOVE', (0,0), (-1,0), 0.5, colors.HexColor(gold_hex)),
    ('LINEBELOW', (0,0), (-1,0), 0.5, colors.HexColor(gold_hex)),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,1), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.whitesmoke, colors.Color(0.98,0.98,0.98)]),
    ('GRID', (0,0), (-1,-1), 0.25, colors.lightgrey),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
]))
flow.append(tbl)
flow.append(Paragraph("<b>Tools Used:</b> ServiceNow KB module, Confluence, JIRA, Cerberus, Visio", styles['KBFine']))

flow.append(Paragraph("Case Study — BSIT System Issue Escalation SOP", styles['KBH2']))
flow.append(Paragraph("<b>Problem Statement:</b> There was no consistent workflow for escalating system-wide bugs. Agents logged issues across tools with no traceability for L3 Engineering, causing duplicate effort and delayed fixes.", styles['KBBody']))

steps = [
    "<b>Initiate BHCSE JIRA Ticket</b> — capture customer impact details and environment.",
    "<b>Create Cerberus Ticket</b> — log customer-facing communications and update thread.",
    "<b>Triaging Threshold</b> — minimum of three verified accounts experiencing the same error before elevating to BSIT.",
    "<b>Linking Protocol</b> — associate all related JIRAs and Cerberus records to the primary BSIT case to ensure mass resolution and traceable root cause analysis.",
]
flow.append(ListFlowable([ListItem(Paragraph(s, styles['KBBody'])) for s in steps], bulletType='1', leftIndent=14))
flow.append(Spacer(1, 6))
flow.append(Paragraph("Reference Document: BSIT Process (PDF link available on portfolio page)", styles['KBFine']))

flow.append(Paragraph("Measured Impact", styles['KBH2']))
impact_data = [
    ["Metric", "Before", "After", "Improvement"],
    ["Repeat Client Service Calls", "Baseline", "↓", "30%"],
    ["Average Handle Time (AHT)", "Baseline", "↓", "25%"],
    ["Escalation Resolution Time", "Baseline", "↓", "25%"],
]
imp_tbl = Table(impact_data, hAlign='LEFT', colWidths=[2.5*inch, 1.1*inch, 1.1*inch, 1.6*inch])
imp_tbl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor(gold_hex)),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 10),
    ('GRID', (0,0), (-1,-1), 0.25, colors.lightgrey),
    ('ALIGN', (1,1), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,1), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.whitesmoke, colors.Color(0.98,0.98,0.98)]),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
]))
flow.append(imp_tbl)

flow.append(Paragraph("Lessons Learned & Next Steps", styles['KBH2']))
ll_points = [
    "Embed KCS review checkpoints in the onboarding curriculum.",
    "Automate AQC metrics via ServiceNow dashboards.",
    "Expand coaching framework to include field technicians and product teams.",
]
flow.append(ListFlowable([ListItem(Paragraph(p, styles['KBBody'])) for p in ll_points], bulletType='bullet', leftIndent=14))

flow.append(Paragraph("Summary of Outcomes", styles['KBH2']))
flow.append(Paragraph(
    "The KCS Coaching Framework and BSIT Process SOP transformed a fragmented support operation into a scalable, metrics-driven knowledge ecosystem — delivering measurable efficiency and confidence across the organization.",
    styles['KBBody']
))

flow.append(Spacer(1, 12))
flow.append(GoldRule(height=4))
flow.append(Paragraph("Lawrence Bloodsaw-Velasquez • Senior Technical Writer & Knowledge Management Specialist • The.Velasquez.Law@gmail.com • portfolio.ellvii.me", styles['KBFine']))

doc.build(flow)

html_path = "kcs_kb_article.html"
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>KCS Coaching & Process Documentation Framework — KB Article</title>
<style>
  :root {{
    --gold: {gold_hex};
    --ink: #111;
    --muted: #6b7280;
    --bg: #ffffff;
    --card: #f9fafb;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji";
    color: var(--ink);
    background: var(--bg);
    line-height: 1.6;
    margin: 0;
    padding: 0;
  }}
  .kb {{ max-width: 860px; margin: 40px auto; padding: 0 20px; }}
  .bar {{ height: 8px; background: var(--gold); border-radius: 0 0 8px 8px; }}
  h1 {{ font-size: 28px; margin: 18px 0 8px; }}
  .meta {{ color: var(--muted); font-size: 13px; margin-bottom: 20px; }}
  h2 {{ font-size: 20px; margin-top: 26px; margin-bottom: 8px; }}
  p {{ margin: 8px 0; }}
  .card {{ background: var(--card); border: 1px solid #e5e7eb; border-radius: 12px; padding: 16px; }}
  table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
  th, td {{ border: 1px solid #e5e7eb; padding: 10px; text-align: left; }}
  th {{ background: var(--gold); color: white; }}
  .btn {{ display: inline-block; padding: 10px 14px; border-radius: 10px; border: 1px solid var(--gold); color: var(--ink); text-decoration: none; font-weight: 600; }}
  .btn:hover {{ background: var(--gold); color: white; }}
  .footer {{ color: var(--muted); font-size: 12px; margin-top: 24px; border-top: 2px solid var(--gold); padding-top: 12px; }}
  ul, ol {{ padding-left: 20px; }}
  .tag {{ display: inline-block; background: #fff7e6; color: #7c5800; border: 1px solid var(--gold); padding: 2px 8px; border-radius: 999px; font-size: 12px; margin-right: 6px; }}
</style>
</head>
<body>
  <div class="kb">
    <div class="bar"></div>
    <h1>🧭 KCS Coaching & Process Documentation Framework</h1>
    <div class="meta">
      <strong>Article ID:</strong> KCS-0049 &nbsp;|&nbsp; <strong>Version:</strong> 1.2 &nbsp;|&nbsp; <strong>Last Updated:</strong> Oct 2025 &nbsp;|&nbsp; <strong>Author:</strong> Lawrence Bloodsaw-Velasquez
      <div style="margin-top:6px;">
        <span class="tag">ServiceNow</span><span class="tag">Confluence</span><span class="tag">JIRA</span><span class="tag">Cerberus</span><span class="tag">Visio</span>
      </div>
    </div>

    <div class="card">
      <h2>🧩 Summary</h2>
      <p>This article outlines how the <strong>KCS (Coaching) Framework</strong> was designed and implemented to transform fragmented support documentation into a unified knowledge ecosystem. It also showcases a key deliverable — the <strong>BSIT Escalation Process SOP</strong> — as a case study proving measurable operational impact.</p>
    </div>

    <h2>🔍 Background / The Challenge</h2>
    <ul>
      <li>Inconsistent knowledge article quality across business units</li>
      <li>Limited agent confidence in search results and KB reliability</li>
      <li>High onboarding friction for new agents</li>
      <li>Undefined escalation pathways for complex system issues</li>
    </ul>
    <p><strong>Business Impact:</strong> Slow resolution times, duplicated tickets, and incomplete engineering handoffs.</p>

    <h2>⚙️ Solution Overview — The KCS Coaching Framework</h2>
    <p><strong>Goal:</strong> Establish a culture of continuous knowledge improvement supported by metrics and peer accountability.</p>
    <table>
      <thead><tr><th>Component</th><th>Description</th></tr></thead>
      <tbody>
        <tr><td>Article Quality Checklist (AQC)</td><td>Objective rubric evaluating accuracy, structure, and findability.</td></tr>
        <tr><td>Peer Coaching Program</td><td>Senior agents mentor junior staff on style and taxonomy consistency.</td></tr>
        <tr><td>Performance &amp; Adoption Dashboard</td><td>Tracks reuse rate, AQC scores, and KCS participation per team.</td></tr>
        <tr><td>Standardized SOP Templates</td><td>Pre-approved formats for procedures, job aids, and escalations.</td></tr>
      </tbody>
    </table>
    <p><em>Tools Used:</em> ServiceNow KB module, Confluence, JIRA, Cerberus, Visio</p>

    <h2>🧠 Case Study — BSIT System Issue Escalation SOP</h2>
    <p><strong>Problem Statement:</strong> There was no consistent workflow for escalating system-wide bugs. Agents were logging issues in different tools with no traceability for L3 Engineering, causing duplicate effort and delayed fixes.</p>
    <ol>
      <li><strong>Initiate BHCSE JIRA Ticket</strong> — capture customer impact details and environment.</li>
      <li><strong>Create Cerberus Ticket</strong> — log customer-facing communications and update thread.</li>
      <li><strong>Triaging Threshold</strong> — minimum of three verified accounts experiencing the same error before elevating to BSIT.</li>
      <li><strong>Linking Protocol</strong> — associate all related JIRAs and Cerberus records to the primary BSIT case to ensure mass resolution and traceable root cause analysis.</li>
    </ol>
    <p>📄 <a class="btn" href="/assets/BSIT_Process.pdf" target="_blank">Download BSIT Process (PDF)</a></p>

    <h2>📈 Measured Impact</h2>
    <table>
      <thead><tr><th>Metric</th><th>Before</th><th>After</th><th>Improvement</th></tr></thead>
      <tbody>
        <tr><td>Repeat Client Service Calls</td><td>Baseline</td><td>↓</td><td>30%</td></tr>
        <tr><td>Average Handle Time (AHT)</td><td>Baseline</td><td>↓</td><td>25%</td></tr>
        <tr><td>Escalation Resolution Time</td><td>Baseline</td><td>↓</td><td>25%</td></tr>
      </tbody>
    </table>

    <h2>💡 Lessons Learned &amp; Next Steps</h2>
    <ul>
      <li>Embed KCS review checkpoints in the onboarding curriculum.</li>
      <li>Automate AQC metrics via ServiceNow dashboards.</li>
      <li>Expand coaching framework to include field technicians and product teams.</li>
    </ul>

    <h2>🏁 Summary of Outcomes</h2>
    <p>The KCS Coaching Framework and BSIT Process SOP transformed a fragmented support operation into a scalable, metrics-driven knowledge ecosystem — delivering measurable efficiency and confidence across the organization.</p>

    <div class="footer">
      Lawrence Bloodsaw-Velasquez • Senior Technical Writer &amp; Knowledge Management Specialist • <a href="mailto:The.Velasquez.Law@gmail.com">The.Velasquez.Law@gmail.com</a> • <a href="https://portfolio.ellvii.me" target="_blank" rel="noopener">portfolio.ellvii.me</a>
      <div style="margin-top:10px;">
        <a class="btn" href="/assets/KCS_Coaching_and_BSIT_KB.pdf" download>📄 Download PDF</a>
      </div>
    </div>
  </div>
</body>
</html>
"""
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Wrote:", pdf_path, html_path)
