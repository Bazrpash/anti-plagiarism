import uuid
from django.db import models
from django.forms import ModelForm


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    first_and_last_name = models.CharField(max_length=100, blank=False, null=False)

    student_no = models.CharField(max_length=10, blank=True, null=True)
    uni_major = models.CharField(max_length=50, blank=True, null=True)
    uni_name = models.CharField(max_length=50, blank=False, null=False)

    prof = 'PROF'
    researcher = 'researcher'
    other_pos = 'OTHER_POS'
    POSITION_CHOICES = (
        (prof, "PROF"),
        (researcher, "researcher"),
        (other_pos, "OTHER_POS"),
    )
    uni_position = models.CharField(choices=POSITION_CHOICES, max_length=20, blank=True, null=True)

    is_visible = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_graduated = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    notes = models.TextField(default="", blank=True)

    def __str__(self):
        if self.first_and_last_name:
            return str(self.first_and_last_name)
        else:
            return str(self.id)


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'first_and_last_name', 'student_no', 'uni_major', 'uni_name',
                  'uni_position', 'is_visible', 'is_graduated', 'is_professor']
