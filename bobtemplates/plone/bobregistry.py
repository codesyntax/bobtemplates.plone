class RegEntry(object):
    def __init__(self):
        self.template = ''
        self.type = ''
        self.depend_on = None


def plone_addon():
    reg = RegEntry()
    reg.template = 'bobtemplates.plone:addon'
    reg.type = 'template'


def plone_buildout():
    reg = RegEntry()
    reg.template = 'bobtemplates.plone:buildout'
    reg.type = 'template'


def plone_theme_package():
    reg = RegEntry()
    reg.template = 'bobtemplates.plone:theme_package'
    reg.type = 'template'
    return reg


def theme():
    reg = RegEntry()
    reg.template = 'bobtemplates.plone:theme'
    reg.type = 'subtemplate'
    reg.depend_on = 'plone_addon'
    return reg


def content_type():
    reg = RegEntry()
    reg.template = 'bobtemplates.plone:content_type'
    reg.type = 'subtemplate'
    reg.depend_on = 'plone_addon'
    return reg


def vocabulary():
    reg = RegEntry()
    reg.template = 'bobtemplates.plone:vocabulary'
    reg.type = 'subtemplate'
    reg.depend_on = 'plone_addon'
    return reg
