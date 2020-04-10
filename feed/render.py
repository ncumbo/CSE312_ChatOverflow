from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf.pisa import pisa

class Render:
    def render(self, template, context_dict={}):
        temp = get_template(template)
        html = temp.render(context_dict)
        res = BytesIO()
        pdf = pisa.pisaDocument
