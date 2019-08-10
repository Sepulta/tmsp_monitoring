import os
import jinja2
from tmsp_monitoring.pulsar_object import PulsarSet

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(context)


overview_page_template_values = {
			'title':"Overview of pulsars",
	        'pulsar': PulsarSet
        }



def create_overview_page(template, template_values):
	with open('site/static/overview.html', 'w') as overview_static_file:
		overview_static_file.write(render(template, template_values))

create_overview_page('site/templates/overview.html', overview_page_template_values)

