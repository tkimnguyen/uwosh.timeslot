from zope import interface, schema
from zope.formlib import form
from Products.CMFCore import utils as cmfutils
from Products.Five.browser import pagetemplatefile
from Products.Five.formlib import formbase


class ICloneDay(interface.Interface):
    numToCreate = schema.Int(title=u'Number to Create', description=u'The number of clones to create', required=True)
    
class CloneDayForm(formbase.PageForm):
    form_fields = form.FormFields(ICloneDay)
    result_template = pagetemplatefile.ZopeTwoPageTemplateFile('cloneday-results.pt')

    @form.action('Clone')
    def action_migrate(self, action, data):
        numToCreate = data['numToCreate']
        day = self.context
        signupSheet = day.aq_parent
        
        dayCopy = signupSheet.manage_copyObjects([day])
        for i in range(0, numToCreate):
            signupSheet.manage_pasteObjects(dayCopy)
            
        return self.result_template()
        
        
  