from django.db import models


class Members(models.Model):
    # code_member = models.ForeignKey('members.Member', on_delete  = models.PROTECT, related_name = 'members')

    title       = models.CharField('Title'          , max_length=10            , blank=True)
    first_name  = models.CharField('First Name'     , max_length=70            , blank=True)
    last_name   = models.CharField('Last Name'      , max_length=70            , blank=True)
    position    = models.CharField('Position'       , max_length=50            , blank=True)
    phone       = models.CharField('Phone'          , max_length=35            , blank=True)
    mobile      = models.CharField('Mobile'         , max_length=35            , blank=True)
    email1      = models.EmailField('Email 1'       , max_length=50            , blank=True)
    date_joined = models.DateField(null=True)

    def __str__(self):
        return str(self.first_name) + '' + str(self.last_name)

    class Meta:
        db_table = "members"

