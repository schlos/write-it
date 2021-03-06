from django.template import Context, Template
from global_test_case import GlobalTestCase as TestCase
from contactos.models import Contact
from popit.models import Person


class ListContactsTemplateTag(TestCase):
    def setUp(self):
        super(ListContactsTemplateTag, self).setUp()
        self.contact = Contact.objects.get(id=1)

    def test_show_one_contact(self):
        '''When there is one contact it shows something {% show_contacts_for person writeitinstance %}'''
        t = Template('{% load nuntium_tags %}{% show_contacts_for person writeitinstance %}')
        c = Context({
            "person": self.contact.person,
            "writeitinstance": self.contact.writeitinstance
            })
        rendered = t.render(c)
        self.assertTrue(rendered)

    def test_it_shows_the_value_of_the_contact(self):
        '''It should show the contact value and the contact type'''
        t = Template('{% load nuntium_tags %}{% show_contacts_for person writeitinstance %}')
        c = Context({
            "person": self.contact.person,
            "writeitinstance": self.contact.writeitinstance
            })
        rendered = t.render(c)
        self.assertIn(self.contact.value, rendered)

    def test_join_with_commas(self):
        '''
        Join a list with commas
        '''
        t = Template('{% load nuntium_tags %}{{ people|join_with_commas }}')
        people = Person.objects.all().order_by('id')
        c = Context({
            "people": people
            })
        rendered = t.render(c)
        self.assertEquals(u'Pedro, Marcel and Felipe', rendered)
