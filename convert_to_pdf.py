#!/usr/bin/env python3
"""Convert Markdown to PDF using reportlab"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import re

# Input and output files
md_file = r"c:\Users\ZXY\Desktop\Training\CORPORATE_PROFESSIONALS_COURSE.md"
pdf_file = r"c:\Users\ZXY\Desktop\Training\CORPORATE_PROFESSIONALS_COURSE.pdf"

# Read the markdown file
with open(md_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Create PDF document
doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
elements = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#003366'),
    spaceAfter=12,
    fontName='Helvetica-Bold'
)

heading1_style = ParagraphStyle(
    'CustomHeading1',
    parent=styles['Heading1'],
    fontSize=16,
    textColor=colors.HexColor('#003366'),
    spaceAfter=10,
    spaceBefore=8,
    fontName='Helvetica-Bold'
)

heading2_style = ParagraphStyle(
    'CustomHeading2',
    parent=styles['Heading2'],
    fontSize=13,
    textColor=colors.HexColor('#005599'),
    spaceAfter=8,
    spaceBefore=6,
    fontName='Helvetica-Bold'
)

heading3_style = ParagraphStyle(
    'CustomHeading3',
    parent=styles['Heading3'],
    fontSize=11,
    textColor=colors.HexColor('#336699'),
    spaceAfter=6,
    spaceBefore=4,
    fontName='Helvetica-Bold'
)

normal_style = styles['Normal']
normal_style.fontSize = 10
normal_style.spaceAfter = 6

bullet_style = ParagraphStyle(
    'BulletStyle',
    parent=styles['Normal'],
    fontSize=10,
    leftIndent=20,
    spaceAfter=4
)

# Process markdown content
lines = content.split('\n')
i = 0

while i < len(lines):
    line = lines[i]
    
    # Skip empty lines (but keep spacing)
    if not line.strip():
        elements.append(Spacer(1, 0.1*inch))
        i += 1
        continue
    
    # H1 (Title)
    if line.startswith('# '):
        title_text = line.replace('# ', '').strip()
        elements.append(Paragraph(title_text, title_style))
        elements.append(Spacer(1, 0.2*inch))
        i += 1
        continue
    
    # H2
    if line.startswith('## '):
        heading_text = line.replace('## ', '').strip()
        elements.append(Paragraph(heading_text, heading2_style))
        elements.append(Spacer(1, 0.1*inch))
        i += 1
        continue
    
    # H3
    if line.startswith('### '):
        heading_text = line.replace('### ', '').strip()
        elements.append(Paragraph(heading_text, heading3_style))
        elements.append(Spacer(1, 0.08*inch))
        i += 1
        continue
    
    # H4
    if line.startswith('#### '):
        heading_text = line.replace('#### ', '').strip()
        elements.append(Paragraph(f"<b>{heading_text}</b>", heading3_style))
        elements.append(Spacer(1, 0.06*inch))
        i += 1
        continue
    
    # Bullet points
    if line.startswith('- ') or line.startswith('✅ ') or line.startswith('✓ '):
        bullet_text = re.sub(r'^[-✅✓]\s*', '', line).strip()
        elements.append(Paragraph(f"• {bullet_text}", bullet_style))
        i += 1
        continue
    
    # Regular paragraph
    if line.strip() and not line.startswith('|'):
        # Check if next lines are table
        if i + 1 < len(lines) and lines[i + 1].strip().startswith('|'):
            elements.append(Paragraph(line.strip(), normal_style))
            elements.append(Spacer(1, 0.08*inch))
            i += 1
            
            # Process table
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_row = [cell.strip() for cell in lines[i].split('|')[1:-1]]
                table_lines.append(table_row)
                i += 1
            
            if table_lines:
                # Create table
                table = Table(table_lines)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#003366')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 9),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
                    ('FONTSIZE', (0, 1), (-1, -1), 8),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
                ]))
                elements.append(table)
                elements.append(Spacer(1, 0.15*inch))
            continue
        else:
            para_text = line.strip()
            # Replace markdown bold and italic properly
            # Bold: **text** -> <b>text</b>
            para_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', para_text)
            para_text = re.sub(r'__(.*?)__', r'<b>\1</b>', para_text)
            # Italic: *text* -> <i>text</i>
            para_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', para_text)
            para_text = re.sub(r'_(.*?)_', r'<i>\1</i>', para_text)
            elements.append(Paragraph(para_text, normal_style))
    
    i += 1

# Build PDF
doc.build(elements)
print(f"✅ PDF created successfully: {pdf_file}")
