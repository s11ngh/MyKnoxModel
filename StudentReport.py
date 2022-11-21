"""Creates a PDF report for given student
    Library: ReportLab
    Use: studentreport method defined below
"""


from reportlab.pdfgen.canvas import Canvas
from myknoxclass import Student
import KnoxDatabase


def studentreport(self, student):
    if type(student) is not Student:
        raise TypeError("Student must be an instance of class student")

    newpdf = Canvas(student.name+"report.pdf")  # create pdf
    newpdf.setFont('Courier', 24)  # heading font
    newpdf.drawString(60, 730, 'Student Report: '+student.name)  # heading
    newpdf.line(60, 725, 360, 725)
    newpdf.drawString(90, 850, 'Knox ID Number: '+student.knoxID)
    newpdf.drawString(90, 950, 'Major: '+str(student.majordept))
    newpdf.drawString(90, 1050, 'Email: '+student.email)
    newpdf.drawString(90, 1150, 'Academic Record: ' +
                      str(student.academicrecord))
    newpdf.drawString(90, 1250, 'Advisor: '+str(student.advisor))
    newpdf.save()
