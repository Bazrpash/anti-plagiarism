from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    first_and_last_name = models.CharField(max_length=100, blank=True, null=True)

    # TODO is student no. must be unique?
    student_no = models.CharField(max_length=10, blank=True, null=True)

    computer = 'CE'
    electric = 'EE'
    other_MAJ = 'OTHER_MAJ'
    MAJ_CHOICES = (
        (computer, "CE"),
        (electric, "EE"),
        (other_MAJ, "OTHER_MAJ"),
    )
    uni_major = models.CharField(choices=MAJ_CHOICES, max_length=20, blank=True, null=True)

    prof = 'PROF'
    researcher = 'researcher'
    other_pos = 'OTHER_POS'
    POSITION_CHOICES = (
        (prof, "PROF"),
        (researcher, "researcher"),
        (other_pos, "OTHER_POS"),
    )
    uni_position = models.CharField(choices=POSITION_CHOICES, max_length=20, blank=True, null=True)

    sharif = 'SUT'
    tehran = 'UOT'
    other_uni = 'OTHER_UNI'
    UNI_CHOICES = (
        (sharif, "SUT"),
        (tehran, "UOT"),
        (other_uni, "OTHER_UNI"),
    )
    uni_name = models.CharField(choices=UNI_CHOICES, max_length=40, blank=True, null=True)

    is_visible = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_graduated = models.BooleanField(default=False)
    id_professor = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    notes = models.TextField(default="", blank=True)

    def __str__(self):
        if self.first_and_last_name:
            return str(self.first_and_last_name)
        else:
            return '#' + str(self.id)
